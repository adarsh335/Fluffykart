from django.shortcuts import render,redirect
from BackEnd.models import categoryDB,productDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from WebApp.models import messageDB

# Create your views here.
def Indexpage(request):
    return render(request,"index.html")
def CategoryPage(request):
    return render(request,"AddCategory.html")
def CategorySave(request):
    if request.method=="POST":
        cat = request.POST.get('category')
        des = request.POST.get('description')
        sub = request.POST.get('subcat')

        img = request.FILES['image']
        obj = categoryDB(CategoryName=cat, Description=des, SubCategory=sub, CategoryImage=img)
        obj.save()
        return redirect(CategoryPage)
def DisplayCategory(request):
    data = categoryDB.objects.all()
    return render(request,"DisplayCategory.html",{'data':data})
def EditCategory(request,dataid):
    data = categoryDB.objects.get(id=dataid)
    return render(request,"editcategory.html",{'data':data})
def DeleteCategory(request,dataid):
    data =categoryDB.objects.filter(id=dataid)
    data.delete()
    return redirect(DisplayCategory)
def UpdateCategory(request,dataid):
    if request.method=="POST":
        cat = request.POST.get('category')
        des = request.POST.get('description')
        sub = request.POST.get('subcat')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file =fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=categoryDB.objects.get(id=dataid).CategoryImage
        categoryDB.objects.filter(id=dataid).update(CategoryName=cat, Description=des, SubCategory=sub, CategoryImage=file)
        return redirect(DisplayCategory)
def ProductPage(request):
    data = categoryDB.objects.all()
    return render(request,"productpage.html",{'data':data})
def ProductSave(request):
    if request.method=="POST":
        cat = request.POST.get('category')
        pro = request.POST.get('proname')
        qun = request.POST.get('quantity')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        sub = request.POST.get('subcat')
        img = request.FILES['image']
        obj = productDB(Category_Name=cat,Product_Name=pro,Quantity=qun,Description=des,Price=pri,Sub_Category=sub,Product_Image=img)
        obj.save()
        return redirect(ProductPage)
def ProductDisplay(request):
    data = productDB.objects.all()
    return render(request,"productdisplay.html",{'data':data})
def EditProduct(request,dataid):
    data = categoryDB.objects.all()
    products = productDB.objects.get(id=dataid)
    return render(request, "editproduct.html", {'data':data,'products':products})
def ProductUpdate(request,dataid):
    if request.method=="POST":
        cat = request.POST.get('category')
        pro = request.POST.get('proname')
        qun = request.POST.get('quantity')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        sub = request.POST.get('subcat')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =productDB.objects.get(id=dataid).Product_Image
        productDB.objects.filter(id=dataid).update(Category_Name=cat,Product_Name=pro,Quantity=qun,Description=des,Price=pri,Sub_Category=sub,Product_Image=file)
        return redirect(ProductDisplay)

def ProductDelete(request,dataid):
    data = productDB.objects.filter(id=dataid)
    data.delete()
    return redirect(ProductDisplay)
def AdminloginPage(request):
    return render(request,"adminlogin.html")
def AdminLogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__exact=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(Indexpage)
            else:
                return redirect(AdminloginPage)
    else:
        return redirect(AdminloginPage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(AdminloginPage)
def messageDisplay(request):
    data = messageDB.objects.all()
    return render(request,"messagedisplay.html",{'data':data})
def messageDelete(request,dataid):
    data = messageDB.objects.filter(id=dataid)
    data.delete()
    return redirect(messageDisplay)





















