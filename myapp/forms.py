from django import forms
from .models import  Ingredient

class Ing_Form(forms.ModelForm):

    class Meta:
        model=Ingredient
        fields='__all__'


    def __init__(self,*args,**kwargs):
        super(Ing_Form,self).__init__(*args,**kwargs)
        self.fields['Ingredient_quantity'].required=False
