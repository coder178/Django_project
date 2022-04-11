from django.http import HttpResponse
from django.shortcuts import redirect, render


from validate.models import Userinfo

# Create your views here.
def index(request):
    return render(request,"index.html")
def signup(request):
    return render(request,"signup_page.html")
def login(request):
    return render(request,"login.html")
def adminlogin(request):
    return render(request,"admin_login.html")
def adduser(request):
    if request.method=="POST":
            
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        address = request.POST['address']

        if Userinfo.objects.filter(username = uname).exists():
            context = {"duplicate_user": "Username already taken!!!"}
            print(context)
            return render(request, "signup.html", context)
        
        userinfo = Userinfo.objects.create(firstname = fname,lastname = lname,username = uname ,email = email, gender = gender, password = password,address = address)
        userinfo.save()
        return redirect("login")

    return HttpResponse("dkckn")



def loguser(request):
   if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
    
        user = Userinfo.objects.filter(username=username,password=password).first()
        
      
        if username == "admin" and password == "admin":  
            return redirect('/adminpage')
        if user:  
            request.session['username'] = user.username
            return redirect('/home')
        else:
            return render(request, "login.html", {"login_error":"Invalid credential"})
def logout(request):
    request.session['username'] = "undefined"
    return redirect('/login')

def logadmin(request):
   if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
    
        if username == "admin" and password == "admin":  
            return redirect('/adminpage')
        else:
            return render(request, "admin_login.html", {"login_error":"Invalid credential"})