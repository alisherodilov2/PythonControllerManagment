# items_controller.py
from django.shortcuts import render
from newapp.forms import ItemForm
from newapp.models import Items

def item_list(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm()
    items = Items.objects.all()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'home.html', context)

def item_detail(request, id):
    item = Items.objects.get(id=id)
    return render(request, 'show.html', {'item': item})
