from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CategoryForm
from .models import Category

# Add a new category
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_categories')
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form})

# List all categories
def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})
