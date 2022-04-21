
from pyexpat import model
from unicodedata import name
from django.forms import IntegerField
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Ingredient, MenuItem
from django.views.generic import ListView, CreateView
from .forms import IngredientUpdateForm, MenuUpdateForm
from django.views.generic.edit import CreateView,UpdateView, DeleteView


# Create your views here.
def home(request):
    menu = MenuItem.objects.all()
    ingredient=Ingredient.objects.all()
    context={"title_field":"Restaurant Informations","menu_data":menu,"ingredient_data":ingredient}
    return render(request,r"F:\projects\djangodelights\djangodelights\home\templates\delights\home.html",context)


    
def create_menu(request):
    if request.method == "POST":
        menu = MenuItem()
        ing_obj = Ingredient.objects.filter(name=request.POST["ingredient"]).get()
        if(ing_obj.quantity != 0):
            menu.name = request.POST["name"]
            menu.price = request.POST["price"]
            ing_obj.save()
            menu.save()
            menu.ingredient.add(ing_obj)
            menu.save()
            ing_obj.quantity = ing_obj.quantity-1
            ing_obj.save()
        

        # UPDATING INGREDIENT AVAILEBLITY
        
    context={"title_field":"Menu Item Details","ingredient_list":Ingredient.objects.all()}
    return render(request,r"F:\projects\djangodelights\djangodelights\home\templates\delights\createmenu.html",context)


class MenuUpdate(UpdateView):

    model = MenuItem
    template_name=r"F:\projects\djangodelights\djangodelights\home\templates\delights\updatemenu.html"
    fields=["name", "price","ingredient"]
    class_form = MenuUpdateForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id']=self.object.id
        return context

class IngredientUpdate(UpdateView):

    model = Ingredient
    template_name=r"F:\projects\djangodelights\djangodelights\home\templates\delights\updateingredient.html"
    fields=["name", "price","quantity","unit"]
    class_form = IngredientUpdateForm

def delete_menu(request,pk):
    menu_instance = MenuItem.objects.filter(pk=pk).get()
    menu_instance.delete()
    return render(request,r"F:\projects\djangodelights\djangodelights\home\templates\delights\menudelete.html")



def create_ingredient(request):
    if request.method == "POST":
        ingredient = Ingredient()
        ingredient.name = request.POST["name"]
        ingredient.price = request.POST["price"]
        ingredient.quantity = request.POST["quantity"]
        ingredient.unit = request.POST["unit"]
        ingredient.save()


    return render(request,r"F:\projects\djangodelights\djangodelights\home\templates\delights\createingredient.html")

