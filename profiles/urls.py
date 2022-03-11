from django.urls import path
from . import views

urlpatterns = [
    path('me', views.profile, name='me'),
    #path('edit_profile', views.edit_profile, name='edit_profile'),
    #path('delete_profile', views.delete_profile, name='delete_profile'),
    #path('order_history/<order_number>', views.order_history, name='order_history'),
]