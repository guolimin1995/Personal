# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    index test
    :param request: 
    :return: 
    """
    return_content = 'This is a Test index ...'
    return HttpResponse(return_content)
