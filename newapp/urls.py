# urls.py
from django.urls import path
from newapp.controllers import items_controller 

urlpatterns = [
    path('/', items_controller.item_list, name="item_list"),
    path('/item/<int:id>/', items_controller.item_detail, name='item_show'),
]
