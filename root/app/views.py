from django.shortcuts import render, redirect
from .models import Product


def homeView(request):
    data = Product.objects.all()
    context = {'products': data}
    return render(request, 'index.html', context)


def cartView(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.icon = request.POST.get('icon')
        product.name = request.POST.get('name')
        product.remove = request.POST.get('remove')
        product.price = request.POST.get('price')
        product.quantity = request.POST.get('quantity')
        product.total_price = request.POST.get('price') *  product.quantity
        product.save()
        return redirect('checkout')
    context = {'products': product}
    return render(request, 'shop.html', context)

def shopView(request):
    data = Product.objects.all()
    context = {'products': data}
    return render(request, 'shop.html', context)

