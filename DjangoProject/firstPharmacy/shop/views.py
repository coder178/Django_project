from typing_extensions import Self
from django.http import JsonResponse
from django.shortcuts import redirect, render

from adminpage.models import Productdetails
from shop.models import Orderdetails

from shop.models import cartitems, userCart
from validate.models import Userinfo

# Create your views here.
def home(request):
    if request.session['username'] == "undefined":
        return redirect("/")
    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    products = Productdetails.objects.all()
    print(products)
    return render(request,"home.html",{"userinfo": userinfo, "products": products})
def buy(request):
    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    products = Productdetails.objects.all()
    return render(request,"buy.html",{"userinfo": userinfo, "products": products})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

def Addtocart(request,pid):
    if request.session['username'] == "undefined":
        return redirect("/")
    product = Productdetails.objects.filter(id = pid).first()
    qty = 1
    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    cart = userCart.objects.filter(userid = userinfo).first()
    pay = 0
    if cart==None:
        usercart = userCart(userid = userinfo,cart_total=pay)
        usercart.save()
    C = userCart.objects.filter(userid = userinfo).first()
    citem = cartitems.objects.filter(cartid=C.id,productid=product).first()
    if citem==None:  
        total = qty * product.price
        cartitem = cartitems(cartid = C.id,productid = product,quantity=qty,total = total)
        cartitem.save()
        product.stock = product.stock - 1
        product.save()
        C.cart_total = C.cart_total +  total
        C.save()
    return showcart(request)
def showcart(request):
    if request.session['username'] == "undefined":
        return redirect("/")
    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    cart = userCart.objects.get(userid = userinfo)
    Cartitems = cartitems.objects.filter(cartid = cart.id)
    return render(request,"cart.html",{"items": Cartitems,"cart":cart})
def removeitem(request,iid):
    Cartitem = cartitems.objects.filter(id = iid).first()
    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    cart = userCart.objects.get(userid = userinfo)
    product = Cartitem.productid
    product.stock = product.stock + 1
    product.save()
    Cartitem.delete()  
    cart.cart_total = cart.cart_total - Cartitem.total
    cart.save()
    return showcart(request)
def changeqty(request):
    if request.method == "POST":
        iid = request.POST['iid']
        qty = request.POST['qty']
        Cartitem = cartitems.objects.filter(id = iid).first()
        cid = Cartitem.cartid
        cart = userCart.objects.filter(id = cid).first()
        change = int(qty) - Cartitem.quantity 
        Cartitem.quantity = qty
        Cartitem.total = Cartitem.productid.price * int (qty)
        Cartitem.productid.stock =  Cartitem.productid.stock - change
        Cartitem.productid.save()
        Cartitem.save()
        Citem = cartitems.objects.filter(id = iid).first()
        cart.cart_total = cart.cart_total + (Citem.productid.price * change)
        cart.save()
        usercart = userCart.objects.filter(id = cid).first()
        return JsonResponse({"total": Citem.total,"payment":usercart.cart_total}, safe=False)
def generateBill(request):

    username = request.session['username']
    userinfo = Userinfo.objects.get(username = username)
    cart = userCart.objects.get(userid = userinfo)
    orderdetails = Orderdetails(userinf = userinfo,cartid = cart.id,payment = cart.cart_total)   
    orderdetails.save() 
    Cartitems = cartitems.objects.filter(cartid = cart.id)
    cart.delete()
    return render(request,"Bill.html",{"items": Cartitems,"order":orderdetails.payment,"User":userinfo})
