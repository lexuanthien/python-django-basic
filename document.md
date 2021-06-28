Django
1. Install
- Install Python
- Install Package Django: pip install django==2.2
- Create Project Django: django-admin startproject my_app_django_python
- CD project
- Run project web: python manage.py runserver
- Create application: python manage.py startapp NameApplication
- Register application on settings file: polls.apps.PollsConfig

2. Django with MySQL
- Run pip install mysqlclient  if Error
- Create Table in models.py
class users(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(max_length=30)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)

class posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    user_id = models.ForeignKey(users, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)

- Run create migration: python .\manage.py makemigrations
- Run create table DB: python .\manage.py migrate  
- Access 1 Table:
	python .\manage.py shell
	from polls.models import users (access users)
	users.objects.all() (get fied)
	Insert: users(name= "LeXuanThien", age= "23", address= "QUANGTRI", phone =  "0357789143").save()

3. Template
- Create forder 'templates/nameApp'
- Su dung lai template master
    {% block content %}
    {% endblock  %}
    and: {% extends 'polls/master.html' %}

4. Query DB
- Import Models: from .models import users, posts
- Get all fied table: users.objects.all() hoặc get_list_or_404(users, where)
- Get one fied: 
    use get_object_or_404
    from django.shortcuts import render, get_object_or_404
    and: get_object_or_404(users, id = 1) -> Lấy ra user có id là 1

    or: users.objects.get(id = 1)
    
- Khi params trong table có nhiều fied giống nhau thì sử dụng: posts.objects.filter(user_id_id = user_id) để lấy các fied giống nhau đó

5. Relationships models
- When use: user_id = models.ForeignKey(users, on_delete=models.CASCADE) on models.py
- Nếu cần lấy thông tin của bảng khác (từ thông tin bảng users -> lấy các bài đăng posts của user đó)
    Sử dụng: user.posts_set.all
    Với: - user là thông tin đã có, tức là dùng user.id để lấy các posts
         - posts là bảng posts
         - posts_set là nối thêm '_set' để lấy thông tin của mối quan hệ

6. Href: <a href="{% url 'details' user.id %}">ClickMe</a>

7. models.objects.
- all() : Lấy tất cả table
- filter() : Lấy các bản ghi phù hợp với điều kiện
- exclude() : Lấy các bản ghi KHÔNG phù hợp với điều kiện

8. Where
- Query with 'pk' là khóa chính (giống như id)
- Sử dụng:
    pk + __in (where pk in array)
    pk + __gt (where pk > )

9. Tim kiem voi keyword:
- __contains() : Phan biet chu hoa thuong
- icontains() : KO phan biet hoa thuong
- unaccented : (unaccent__icontains, unaccent__lower__trigram_similar)

10. Session
- Tạo: request.session['name_session'] = 'value_session'
- Lấy: - request.session.get('name_session')
       - request.session['name_session']
- Xóa: - request.session.pop('name_session')
       - del request.session['name_session']
- Đặt thời gian tồn tại cho session: request.session.set_expiry(100) (Chưa đặt được cho từng session riêng biệt)
11. api_view
- throttle_classes: ĐỂ GIỚI HẠN API CHỈ TRUY CẬP 1 LẦN TRONG 1 NGÀY
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle
class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/day'

@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])


<!-- Django REST Framwok -->
- request.data == request.POST == request.FILES
- request.query_params == request.GET

1. Generics View
- queryset: Sử dụng tên biến này thì data sẽ được lưu cache cho các yêu cầu tiếp theo
- serializer_class: serializers.py -> Class
