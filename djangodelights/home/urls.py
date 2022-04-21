from django.urls import path, include
from . import views
from .models import MenuItem


urlpatterns = [
    path('',views.home,name="menucreate"),
    path('create_menu/',views.create_menu,name="menuform"),
    path('create_ingredient/',views.create_ingredient,name="menuform"),
    path("update_menu/<pk>",views.MenuUpdate.as_view(),name="updateM"),
    path("update_ing/<pk>",views.IngredientUpdate.as_view(),name="updateI"),
    path("delete_menu/<pk>",views.delete_menu,name="DeleteMenu")
]
