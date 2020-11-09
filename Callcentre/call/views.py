from django.shortcuts import render

def home(request):
    return render(request,'index.html',{})

def Login(request):
    return render(request,'login.html',{})

def layoutstatic(request):
    return render(request,'layout-static.htm',{})

def layoutsidenavlight(request):
    return render(request,'layout-sidenav-light.html',{})

def register(request):
    return render(request,'register.html',{})

def password(request):
    return render(request,'password.html',{})

def Error401(request):
    return render(request,'401.html',{})

def Error404(request):
    return render(request,'404.html',{})

def Error500(request):
    return render(request,'500.html',{})

def charts(request):
    return render(request,'charts.html',{})

def tables(request):
    return render(request,'tables.html',{})

def Disclaimer(request):
    return render(request,'Disclaimer.html',{})