from django import forms
from .models import Items

class ItemForm(forms.ModelForm):
    class  Meta:
        db_table = 'newapp_items'
        model = Items
        fields = ['title' , 'completed']