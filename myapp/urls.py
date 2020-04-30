from django.urls import path
from . import views


urlpatterns = [
    path('',views.ingredient_form,name='myapp-form_insert'),
    path('<int:id>/',views.ingredient_form,name='myapp-form_update'),
    path('list/',views.ingredient_list,name='myapp-list'),
    path('delete/<int:id>/',views.ingredient_delete,name='myapp-delete')
     

]