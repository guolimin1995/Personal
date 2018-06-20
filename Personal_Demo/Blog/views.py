# coding:utf-8
# Create your views here.
# import ujson
import markdown
from django.shortcuts import render, get_object_or_404, HttpResponse
from models import Post, Category
from comments.forms import CommentForm
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from form import USerInfo
# from Blog.models import UserInfo


def index(request):
    """index page"""
    post_list = Post.objects.all().order_by('-created_time')
    ret_dict = {'post_list': post_list}
    return render(request, 'blog/index.html', ret_dict)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', {'post_list': post_list})


# 刷新验证码
def refresh_captcha(request):
    if request.GET.get('newsn') == '1':
        csn = CaptchaStore.generate_key()
        cimageurl = captcha_image_url(csn)
        return HttpResponse(cimageurl)

# def index(request):
#     """
#     index
#     :param request:
#     :return:
#     """
#     message = 'Yes Login Success!'
#     return render(request, 'blog/index.html', {'message': message})
#
#
# def login(request):
#     """
#      login
#     :param request:
#     :return:
#     """
#     # return_content = 'This is a Test index ...'
#     return render(request, 'blog/login.html')
#
#
# @csrf_exempt
# def logins(request):
#     """
#     login post data
#     :param request:
#     :return:
#     """
#     if request.method == 'POST':
#         form = USerInfo(request.POST)
#         if form.is_valid():
#             password = request.POST['password']
#             account = request.POST['user']
#             errors = {'user': [], 'password': []}
#             if not UserInfo.objects.filter(account=account).exists():
#                 errors_message = 'username not exists!'
#                 errors['user'].append(errors_message)
#                 return render(request, 'blog/login.html', {'error': errors})
#             if UserInfo.objects.get(account=account).passwd != password:
#                 errors_message = 'password error!'
#                 errors['password'].append(errors_message)
#                 return render(request, 'blog/login.html', {'error': errors})
#             return HttpResponseRedirect('/blog/index/')
#         else:
#             errors = form.errors
#             return render(request, 'blog/login.html', {'error': errors})
#     else:
#         # error = obj.errors
#         form = USerInfo()
#
#     return render(request, 'blog/login.html', {'form': form})
