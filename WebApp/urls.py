from django.urls import path
from WebApp import views

urlpatterns = [

    path('HomePage/',views.HomePage,name="HomePage"),
    path('ProductsPage/<catg>/', views.ProductsPage, name="ProductsPage"),
    path('SingleProduct/<int:dataid>/',views.SingleProduct,name="SingleProduct"),
    path('test/', views.test, name="test"),
    path('cntctPage/', views.cntctPage, name="cntctPage"),
    path('ContactSend/',views.ContactSend,name="ContactSend"),
    path('UserLoginPage/', views.UserLoginPage, name="UserLoginPage"),
    path('UserRegPage/', views.UserRegPage, name="UserRegPage"),
    path('SaveLogin/', views.SaveLogin, name="SaveLogin"),
    path('UserLogin/', views.UserLogin, name="UserLogin"),
    path('Save2Cart/', views.Save2Cart, name="Save2Cart"),
    path('CartPage/', views.CartPage, name="CartPage"),
path('CartDelete/<int:dataid>/', views.CartDelete, name="CartDelete"),
    path('CheckOutPage/', views.CheckOutPage, name="CheckOutPage"),
    path('OrderSave/', views.OrderSave, name="OrderSave"),
    path('MyOrders/', views.MyOrders, name="MyOrders"),

]



