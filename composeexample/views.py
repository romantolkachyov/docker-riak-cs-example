from django.shortcuts import render_to_response
from django.core.files.storage import get_storage_class


def index(request):
    storage = get_storage_class()()
    assert not storage.exists('test')
    return render_to_response('test.html')
