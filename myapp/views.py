from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required  
from .models import Category, Product, Customer
from .forms import CategoryForm, ProductForm, CustomerForm, SignUpForm




def register_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'form.html', {'form': form, 'title': 'Регистрация аккаунта'})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home') 
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'form.html', {'form': form, 'title': 'Вход в аккаунт'})


def logout_view(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required(login_url='login')
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

@login_required(login_url='login')
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'form.html', {'form': form, 'title': 'Новая категория'})

@login_required(login_url='login')
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать категорию'})

@login_required(login_url='login')
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'confirm_delete.html', {'object': category})


@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required(login_url='login')
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required(login_url='login')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'form.html', {'form': form, 'title': 'Новый товар'})

@login_required(login_url='login')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать товар'})

@login_required(login_url='login')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'confirm_delete.html', {'object': product})


@login_required(login_url='login')
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

@login_required(login_url='login')
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer_detail.html', {'customer': customer})

@login_required(login_url='login')
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'form.html', {'form': form, 'title': 'Новый клиент'})

@login_required(login_url='login')
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'form.html', {'form': form, 'title': 'Редактировать клиента'})

@login_required(login_url='login')
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'confirm_delete.html', {'object': customer})