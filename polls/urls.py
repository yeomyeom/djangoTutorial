from django.urls import path

from . import views
# 2 mysite에서 명령받은 파일에서 views 안에 index라는 함수를 부름
# 이동작은 뷰를 불러냄
urlpatterns = [
    path('', views.index, name='index'),
]
