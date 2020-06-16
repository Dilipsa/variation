from django.shortcuts import render, redirect
from .forms import ProductForm, CategoryForm
from .models import Product, Category


def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/product-list')
    form = ProductForm()
    return render(request, 'create_variation.html', {'form': form})


def product_list_view(request):
    obj = Product.objects.all()
    return render(request, 'variation_list.html', {'obj': obj})


def add_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.cleaned_data.get('category')
            object = Category.objects.all()
            if not category in object:
                form.save()
                return redirect('/category-list')
            else:
                print("cannot be duplicate")
            return redirect('/add-category')
    form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})


def category_list_view(request):
    category = Category.objects.all()
    return render(request, 'category_list.html', {'category': category})
