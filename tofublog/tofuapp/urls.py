from django.conf.urls import url
from tofuapp import views


app_name = 'tofuapp'

urlpatterns = [
   url('lulu/', views.lulu, name='lulu'),
   url('tofu/', views.tofu, name='tofu'),
   url('lucas/', views.lucas, name='lucas'),
   url('register/', views.register, name='register'),
   url('user_login', views.user_login, name='user_login'),
   url('aflogin/', views.aflogin, name='aflogin')
]
