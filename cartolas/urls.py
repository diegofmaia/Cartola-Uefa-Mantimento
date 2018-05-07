from django.urls import path
from cartola.cartolas import views

app_name = 'cartolas'

urlpatterns = [
	path('', views.cartolas, name='cartolas'),
]
