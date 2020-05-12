from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
  path('login/', login_views, name='login'),
  # url(r'^register/$', register_views, name='reg'),
  path('check_uphone/', check_uphone_views),
  path('', index_views),
  path('check_login/', check_login_views),
  path('logout/', logout_views),
  path('test/', test_views),
  path('load_type_goods/', type_goods_views),
  path('add_cart/', add_cart_views),
  path('register/', register_views, name='reg'),
  path('cart_server/', cartserver_views),
  path('cart/', cart_views),
]
