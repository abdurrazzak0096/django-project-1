
from django.shortcuts import redirect, render
from productApp.models import Product
from productApp.forms import ProductForm,SignUpForm

from django.core.paginator import Paginator 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def listproduct(request):
    products= Product.objects.all().order_by('id') 
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context= { 'products':products}

    return render (request,'productApp/listproduct.html',context)


def createProduct(request):

    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listproduct')
    else:
        form=ProductForm()
    context={'form':form}
    return render(request,'productApp/ProductForm.html',context)

def editProduct(request, id):
    
    if request.method =="POST":
        product= Product.objects.get(pk=id)
        form= ProductForm(request.POST or None, request.FILES,instance= product)
        if form.is_valid():
            form.save()
            return redirect('listproduct')
    else:
        product= Product.objects.get(pk=id)
        form=ProductForm(request.POST or None, instance=product)

    context={'title': 'Edit', 'form':form,'product':product}
    return render (request, "productApp/ProductForm.html", context)


def viewProduct(request,id):

    product= Product.objects.get(pk=id)
    form= ProductForm(request.POST or None, instance=product)

    context={'title': 'view', 'form':form, "product": product}
    return render (request, "ProductApp/viewProduct.html",context)

def destroyProduct(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request,("Data Deleted Successfully ..."))
    return redirect('listproduct')


def register(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)


        if user_form.is_valid(): 
            user = user_form .save()
            user.save() 

            #Login after Register
            username1 = user_form.cleaned_data[ 'username']
            password1 = user_form.cleaned_data[ 'password1']

            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)

            
              #messages.success(request,("you have been Registerd..."))

            return redirect('home')

    else:
        user_form = SignUpForm()

    return render (request, 'auth/register.html',{'user_form':user_form, 'title':'Register'})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login success..")
            return redirect('home')
        else:
            messages.error(request,"Error loging in try again...")
            return redirect('login_user')
    else:
        return render(request,"auth/login.html",{'title':'Log In'})    

def logout_user(request):
    logout(request)
    return redirect('home')








