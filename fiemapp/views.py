from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connections


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def catalogue(request):
        cursor=connections['default'].cursor()
        sel="SELECT * FROM products"
        cursor.execute(sel)
        p=cursor.fetchall()
        w={"pg":p}
        return render(request,"catalogue.html",w)

def dashboard(request):
    if 'aname' not in request.session:
        return redirect('/login/')
    else:
        return render(request,"dashboard.html")


def addproducts(request):
    if 'aname' not in request.session:
        return redirect('/login/')
    else:
        return render(request,"addproducts.html")

def insproducts(request):
    pt=request.POST['ptitle']
    pd=request.POST['pdetails']
    myfile=request.FILES['kimg']
    with open("/home/SundarbanDevbyAnkita/mysite/static/productimg/"+myfile.name,"wb+") as destination:
        for chunk in myfile.chunks():
            destination.write(chunk)

    cursor=connections['default'].cursor()
    ins="INSERT INTO products SET ptitle='"+str(pt)+"',pdetails='"+str(pd)+"',pimg='"+str(myfile.name)+"'"
    cursor.execute(ins)
    return HttpResponse(pt+" "+pd)

def listproduct(request):
    if 'aname' not in request.session:
        return redirect('/login/')
    else:
        cursor=connections['default'].cursor()
        sel="SELECT * FROM products"
        cursor.execute(sel)
        p=cursor.fetchall()
        w={"pg":p}
        return render(request,"listproduct.html",w)


def delproduct(request):
    cursor=connections['default'].cursor()
    did=request.GET['did']
    delp="DELETE FROM products WHERE pid='"+str(did)+"'"
    cursor.execute(delp)
    return redirect("/listproduct/")

def login(request):
    return render(request,"login.html")

def loginck(request):
    e=request.POST['email']
    p=request.POST['pass']
    cursor=connections['default'].cursor()
    sel="SELECT * FROM admin WHERE email='"+e+"' AND password='"+p+"'"
    cursor.execute(sel)
    p=cursor.fetchall()
    if(len(p)>0):
        request.session['aname']=p[0][1]
        return redirect("/dashboard/")
    else:
        return HttpResponse("Invalid Login")

def logout(request):
    del request.session['aname']
    return redirect('/login/')









