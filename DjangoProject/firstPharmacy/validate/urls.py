"""firstPharmacy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path
from . import views as v_views
from shop import views as s_views
from adminpage import views as a_views

urlpatterns = [
    path('',v_views.login,name="login"),
    path('signup/',v_views.signup,name="signup"),
    path('login/',v_views.login,name="login"),
    path('login/loguser',v_views.loguser,name="loguser"),
    path('login_admin/',v_views.adminlogin,name="adminlogin"),
    path('login_admin/logadmin',v_views.logadmin,name="logadmin"),
    path('loguser',v_views.loguser,name="loguser"),
    path('signup/adduser',v_views.adduser,name="adduser"),
    path('home/',s_views.home,name="home"),
    path('about/',s_views.about,name="about"),
    path('buy/',s_views.buy,name="buy"),
    path('contact/',s_views.contact,name="contact"),
    path('adminpage/',a_views.adminpage,name="adminpage"),
    path('addproductform/',a_views.addproductform,name="addproductform"),
    path('addproductform/addproduct',a_views.addproduct,name="addproduct"), 
    path('logout/',v_views.logout,name="logout"),   
    path('products/',a_views.products,name="Products"),
    path('users/',a_views.users,name="Users"), 
    path('Addtocart/<int:pid>',s_views.Addtocart,name="Addtocart"), 
    path('showcart/',s_views.showcart,name="Addtocart"), 
    path('removeitem/<int:iid>',s_views.removeitem,name="removeitem"), 
    path('Addtocart/changeqty',s_views.changeqty,name="incrementqty"),
    path('generateBill/',s_views.generateBill,name="generateBill"),
    path('updateproductform/<int:pid>',a_views.updateproductform,name="updateproductform"), 
    path('updateproductform/updateproduct/<int:pid>',a_views.updateproduct,name="updateproduct"), 


] 


