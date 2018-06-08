# coding:utf-8
# Create your views here.
# import ujson
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from form import USerInfo
from Blog.models import UserInfo


def index(request):
    """
    index
    :param request: 
    :return: 
    """
    message = 'Yes Login Success!'
    return render(request, 'blog/index.html', {'message': message})


def login(request):
    """
     login
    :param request: 
    :return: 
    """
    # return_content = 'This is a Test index ...'
    return render(request, 'blog/login.html')


@csrf_exempt
def logins(request):
    """
    login post data
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        form = USerInfo(request.POST)
        if form.is_valid():
            password = request.POST['password']
            account = request.POST['user']
            errors = {'user': [], 'password': []}
            if not UserInfo.objects.filter(account=account).exists():
                errors_message = 'username not exists!'
                errors['user'].append(errors_message)
                return render(request, 'blog/login.html', {'error': errors})
            if UserInfo.objects.get(account=account).passwd != password:
                errors_message = 'password error!'
                errors['password'].append(errors_message)
                return render(request, 'blog/login.html', {'error': errors})
            return HttpResponseRedirect('/blog/index/')
        else:
            errors = form.errors
            return render(request, 'blog/login.html', {'error': errors})
    else:
        # error = obj.errors
        form = USerInfo()

    return render(request, 'blog/login.html', {'form': form})
