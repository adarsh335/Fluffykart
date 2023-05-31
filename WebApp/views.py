from django.shortcuts import render,redirect
from BackEnd.models import categoryDB,productDB
from WebApp.models import messageDB,loginDB,cartDB,checkoutDB
from django.contrib import messages

# Create your views here.

def HomePage(request):
    data =categoryDB.objects.all()
    return render(request,"home.html",{'data':data})
def ProductsPage(request,catg):
    products = productDB.objects.filter(Category_Name=catg)
    return render(request,"products.html", {'products':products})
def SingleProduct(request,dataid):
    data =productDB.objects.get(id=dataid)
    return render(request,"singleproduct.html",{'data':data})
def test(request):
    return render(request,"singletest.html")
def cntctPage(request):
    return render(request,"contacts.html")
def ContactSend(request):
    if request.method=="POST":
        mes = request.POST.get('message')
        nam = request.POST.get('name')
        ema = request.POST.get('email')
        sub = request.POST.get('subject')
        obj = messageDB(Message=mes,SenderName=nam,Mail=ema,Subject=sub)
        obj.save()
        return redirect(cntctPage)
def UserLoginPage(request):
    return render(request,"userlogin.html")
def UserRegPage(request):
    return render(request,"userreg.html")
def SaveLogin(request):
    if request.method=="POST":
        newuser = request.POST.get('username')
        pas = request.POST.get('password')
        obj = loginDB(uNAME=newuser,uPASS=pas)
        obj.save()
        messages.success(request, "Account Created")
        return redirect(UserLoginPage)
def UserLogin(request):
    if request.method=="POST":
        a = request.POST.get('username')
        b = request.POST.get('password')
        if loginDB.objects.filter(uNAME=a,uPASS=b).exists():
            request.session['username'] = a
            request.session['password'] = b
            messages.success(request, "Signed in successfully, Enjoy Shopping.")
            return redirect(HomePage)
        else:
            return redirect(UserLoginPage)
    else:
        return redirect(UserLoginPage)
def Save2Cart(request):
    if request.method=="POST":
        Pname = request.POST.get('ProductName')
        Pri = request.POST.get('priceperpiece')
        qty2 = request.POST.get('qty')
        tot = request.POST.get('totalprice')
        username = request.session.get('username')


        obj = cartDB(ProductName=Pname, Price=Pri,Quantity=qty2,TotalPrice=tot,UserName=username)
        obj.save()
        messages.success(request,"Product Added Successfully")


        return redirect(HomePage)

def CartPage(request):
    cartt=cartDB.objects.filter(UserName=request.session['username'])
    subtotal = sum(item.TotalPrice for item in cartt)

    context = {
        'cartt': cartt,
        'subtotal': subtotal
    }

    return render(request,"cartpage.html",context)
def CartDelete(request,dataid):
    data = cartDB.objects.filter(id=dataid)
    data.delete()
    messages.warning(request, "Item removed!")
    return redirect(CartPage)
def CheckOutPage(request):
    cart3 = cartDB.objects.filter(UserName=request.session['username'])
    total = sum(item.TotalPrice for item in cart3)

    print(cart3)  # Add this line to print the value of cart3

    context = {
        'cart3': cart3,
        'total': total
    }

    return render(request, "checkout.html", context)
def OrderSave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ph = request.POST.get('phone')
        ad = request.POST.get('address')
        pin = request.POST.get('zip')
        select = request.POST.get('selector')


        # Process the iterating product data
        username = request.session.get('username')
        products = request.POST.getlist('product')
        quantities = request.POST.getlist('quantity')
        subtotals = request.POST.getlist('subtotal')

        # Save the products in checkoutDB model
        for i in range(len(products)):
            obj = checkoutDB(
                Customer=na,
                Address=ad,
                Phone=ph,
                Pincode=pin,
                PaymentMode=select,
                UserName=username[i],
                ProductName=products[i],
                Quantity=quantities[i],
                TotalPrice=subtotals[i]
            )
            obj.save()
            messages.success(request, "Placed Successfully")

        return redirect(HomePage)

def MyOrders(request):
    data = checkoutDB.objects.all()
    return render(request,"myorders.html", {'data':data})










