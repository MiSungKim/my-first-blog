
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns=[
        url(r'^$', views.post_list, name='post_list'),

        url(r'^join/$', views.signup, name='join'),

        url(r'^login/$', views.signin, name='login'),

]
