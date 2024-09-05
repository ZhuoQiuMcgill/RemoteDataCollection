from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .IndexedText import *


@csrf_exempt  # 暂时禁用 CSRF 检查以简化开发（生产环境中要小心使用）
def submit_texts(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        previous_text = data.get('previous')
        current_text = data.get('current')

        indexed_previous_text = IndexedText(previous_text)
        indexed_previous_text_content_with_highlight = indexed_previous_text.get_indexed_text_with_highlight()
        print(f'Indexed Previous Text:\n{indexed_previous_text_content_with_highlight}')

        indexed_cur_text = IndexedText(current_text)
        indexed_cur_text_content_with_highlight = indexed_cur_text.get_indexed_text_with_highlight()
        print(f'Indexed Current Text:\n{indexed_cur_text_content_with_highlight}')

        return JsonResponse({'status': 'success',
                             'message': 'Texts received successfully!',
                             'indexed_prev_text': indexed_previous_text_content_with_highlight,
                             'indexed_cur_text': indexed_cur_text_content_with_highlight
                             })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def homepage(request):
    return render(request, 'index.html')


def rom_data_collection(request):
    return render(request, 'ROMdataCollection.html')
