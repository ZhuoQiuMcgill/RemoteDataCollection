from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def rom_data_collection(request):
    return render(request, 'ROMdataCollection.html')
