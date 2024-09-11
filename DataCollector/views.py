from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .IndexedText import *


@csrf_exempt
def submit_texts(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        previous_text = data.get('previous')
        current_text = data.get('current')

        indexed_previous_text = IndexedText(previous_text)
        indexed_cur_text = IndexedText(current_text)

        if indexed_previous_text.number_of_sentences > 5:
            return JsonResponse({
                'status': 'fail',
                'message': 'Too many previous sentences!'
            })

        if indexed_cur_text.number_of_sentences > 1:
            return JsonResponse({
                'status': 'fail',
                'message': "Too many current sentences!"
            })

        indexed_previous_text_content_with_highlight = indexed_previous_text.get_indexed_text_with_highlight()
        indexed_cur_text_content_with_highlight = indexed_cur_text.get_indexed_text_with_highlight()

        return JsonResponse({
            'status': 'success',
            'message': 'Texts received successfully!',
            'indexed_text': {'prev_text': indexed_previous_text.get_indexed_text(),
                             'cur_text': indexed_cur_text.get_indexed_text()},
            'indexed_prev_text': indexed_previous_text_content_with_highlight,
            'indexed_cur_text': indexed_cur_text_content_with_highlight,
            'prev_possible_tokens': indexed_previous_text.get_possible_tokens(),
            'cur_possible_tokens': indexed_cur_text.get_possible_tokens()
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


@csrf_exempt
def save_mappings(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            mappings = data.get('mappings', [])
            indexed_prev_text = data.get('indexed_prev_text')
            indexed_cur_text = data.get('indexed_cur_text')
            mapping_list = []

            for mapping in mappings:
                prev_word = mapping.get('prev_word')
                cur_word = mapping.get('cur_word')
                mapping_data = mapping.get('mapping_data')
                mapping_list.append(mapping_data)

                print(f'Saving mapping: {prev_word} -> {cur_word} with data: {mapping_data}')

            return JsonResponse({'success': True})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'success': False, 'error': 'Method not allowed'}, status=405)


def homepage(request):
    return render(request, 'index.html')


def rom_data_collection(request):
    return render(request, 'ROMdataCollection.html')
