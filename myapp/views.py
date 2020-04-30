from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import Ing_Form
from .models import Ingredient

def ingredient_list(request):
    context={'ing_list':Ingredient.objects.all()}
    return render(request,'myapp/ingredient_list.html',context)



def ingredient_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form=Ing_Form()
        else:
            ingredient=Ingredient.objects.get(pk=id)
            form=Ing_Form(instance=ingredient)
        return render(request,'myapp/ing_form.html',{'form':form})
    else:
        if id == 0:
            form=Ing_Form(request.POST)
        else:
            ingredient=Ingredient.objects.get(pk=id)
            form=Ing_Form(request.POST,instance=ingredient)

        if form.is_valid():
            form.save()
        return redirect('/list')


def ingredient_delete(request,id ):
    ingredient=Ingredient.objects.get(pk=id)
    ingredient.delete()
    return redirect('/list')
    