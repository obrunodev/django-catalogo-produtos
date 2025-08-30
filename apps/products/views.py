from apps.products.forms import ProductForm
from apps.products.models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render


@login_required
def product_create(request):
    if request.method == 'GET':
        form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = user
            obj.save()
            return redirect('products:list')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)


@login_required
def product_list(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=q)
    paginator = Paginator(products, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'products/product_list.html', context)


@login_required
def product_update(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    if request.method == 'GET':
        form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:list')

    context = {'form': form}
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'GET':
        return render(
            request,
            'products/product_confirm_delete.html',
            {'product': product}
        )
    product.delete()
    return redirect('products:list')


def product_marketplace(request):
    q = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=q)
    context = {'products': products}
    return render(request, 'products/marketplace.html', context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product}
    return render(request, 'products/product_detail.html', context)
