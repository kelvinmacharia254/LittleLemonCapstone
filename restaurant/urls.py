from django.urls import path

from restaurant import views

urlpatterns = [
    path('', views.index, name='sayHello'),
    path('items',views.MenuItemView.as_view(), name='menu_list'),
    path('items/<int:pk>', views.SingleMenuItemView.as_view(), name='single_menu_item'),
]