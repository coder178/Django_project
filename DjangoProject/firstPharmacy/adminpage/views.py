from itertools import product
from django.shortcuts import redirect, render

from adminpage.models import Productdetails
from shop.views import showcart
from validate.models import Userinfo



# Create your views here.
def adminpage(request):
    users = Userinfo.objects.all()
    products = Productdetails.objects.all()
    return render(request, "admin.html",{"users": users, "products": products})
def addproductform(request):
    return render(request, "addproduct_form.html")
def updateproductform(request,pid):
    product = Productdetails.objects.filter(id = pid).first()
    return render(request, "edit_product.html",{"product":product})
def addproduct(request):
    if request.method == "POST":
        productname = request.POST['pname']
        description = request.POST['productdes']
        productpic = request.FILES['productpic']
        productPrice = request.POST['productprice']
        productStock = request.POST['productstock']
        productinfo = Productdetails.objects.create(productname = productname,description= description,price = productPrice,productimg = productpic,stock = productStock)
        productinfo.save()
        return redirect('/adminpage') 
def products(request):
    products = Productdetails.objects.all()
    return render(request, "products.html",{"products": products})
def users(request):
    users = Userinfo.objects.all()
    return render(request, "users.html",{"users": users})
def updateproduct(request,pid):
    product = Productdetails.objects.filter(id = pid).first()
    if request.method == "POST":
        productname = request.POST['pname']
        description = request.POST['productdes']
        productpic = request.FILES['productpic']
        productPrice = request.POST['productprice']
        productStock = request.POST['productstock']
        product.productname = productname
        product.description = description
        product.productimg = productpic
        product.price = productPrice
        product.stock = productStock
        product.save()
        return redirect('/products') 