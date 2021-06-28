import re
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404
from django.urls import reverse

from django.conf import settings
from django.shortcuts import redirect

# Cho phep truy cap (Khi post thif ko dc truy cap)
from django.views.decorators.http import require_http_methods

# import models
from .models import user, post

from django.contrib.auth import authenticate, login

# Upload file
# from .form import UploadFileForm


# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    data = {
        'name': 'LE XUAN THIEN',
        # get all table
        'users': user.objects.all(),
        # get user with id = 1, chua get ra 1 cai dau tien khi co nhieu gia tri
        # 'user': get_object_or_404(users, name = 'LeXuanThien', age = 18)
        # or
        # 'user': user.objects.get(name = 'LeXuanThien', age = 18)
    }
    return render(request, 'polls/index.html', data)

def show(request, user_id):
    # Session
    # Create: request.session['test_python_sesion'] = 'Content Session'
    # Time Expiry: request.session.set_expiry(100)
    # Delete: request.session.pop('test_python_sesion')
    # if(request.session['test_python_sesion']):
    #     return HttpResponse(request.session['test_python_sesion'])
    # else:
    #     return HttpResponse('ok')


    # CHuyen huong
    # return redirect('/create')
    try:
        a = user.objects.get(pk=user_id)
    except user.DoesNotExist:
        raise Http404("user ko ton tai")
    return render(request, 'polls/show.html', {'user': a})

    # return HttpResponse(user.objects.raw('SELECT * FROM polls_user WHERE id = %s', [1]))

    # Tao ban ghi voi create()
    # user.objects.get(id = user_id).post_set.create(title="Xin chao cac ban toi la",description="John's second story", content='Content ne')
    
    data = {
        #  Sử dụng hàm filter()
        # 'posts': posts.objects.filter(user_id = user_id),

        # Sử dụng hàm get_list_or_404
        # 'posts': get_list_or_404(post, user_id = user_id)

        # Sử dụng mối quan hệ để lấy
        # 'posts': user.objects.get(id = user_id).post_set.all(),

        # 'posts': user.objects.get(id = user_id).author.all(),
        # Sử dụng related_name = "author" ben Models thì sẽ khong dung duoc post_set

        # Gửi thông tin của user có used_id đó qua view rồi bên view dùng mối quan hệ để lấy các bài posts
        'user': user.objects.get(id = user_id)
    }
    return render(request, 'polls/show.html', data)

def create(request):
    return render(request, 'polls/create.html')

@require_http_methods(["POST"]) #CHI POST MOI DC TRUY CAP
def store(request):
    # C1:
    # if not request.POST['title'] or not request.POST['description'] or not request.POST['content'] or not request.POST['user']:
    # else:

    # C2:
    # if '' in [ request.POST['title'],  request.POST['description'],  request.POST['content'],  request.POST['user']]:
    #     return HttpResponse('rong')
    # else:
    #     return HttpResponse('Ko rong')

    if(len(request.POST['title']) == 0 or len(request.POST['description']) == 0 or len(request.POST['content']) == 0 or len(request.POST['user']) == 0):
        return render(request, 'polls/create.html', {
            'message': "Cannot be left blank !",
        })
        # Ko thay doi duoc url display

        # return HttpResponseRedirect(reverse('polls:create'), {
        #     'message': "Cannot be left blank !",
        # })
        # Khong truyen duoc var message
    else:
        idUsers = []
        for item in user.objects.all():
            idUsers.append(item.id)
        
        if(int(request.POST['user']) in idUsers):
            data = post()
            data.title = request.POST['title']
            data.description = request.POST['description']
            data.content = request.POST['content']

            # C1
            user_id = user.objects.get(pk=request.POST['user'])
            data.user = user_id

            # C2
            # data.user_id = request.POST['user']
            
            data.save()
            return HttpResponseRedirect(reverse('polls:details', args=(request.POST['user'])))
            # Redirect (use funtion HttpResponseRedirect,reverse and args)
        else:
            return render(request, 'polls/create.html', {
                'message': "User ID khong ton tai trong DB",
            })

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponse('Thanh cong')
#     else:
#         form = UploadFileForm()
#     return render(request, 'polls/upload.html', {'form': form})

# def handle_uploaded_file(f):
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('da login')
            else:
                return HttpResponse('Ko login')
        else:
            return render(request, 'polls/login.html')