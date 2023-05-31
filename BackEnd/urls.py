from django.urls import path
from BackEnd import views

urlpatterns = [
    path('Indexpage/',views.Indexpage,name="Indexpage"),
    path('CategoryPage/',views.CategoryPage,name="CategoryPage"),
    path('CategorySave/',views.CategorySave,name="CategorySave"),
    path('DisplayCategory/',views.DisplayCategory,name="DisplayCategory"),
    path('EditCategory/<int:dataid>/', views.EditCategory, name="EditCategory"),
    path('DeleteCategory/<int:dataid>/',views.DeleteCategory,name="DeleteCategory"),
    path('UpdateCategory/<int:dataid>/', views.UpdateCategory, name="UpdateCategory"),
    path('ProductPage/', views.ProductPage, name="ProductPage"),
    path('ProductSave/', views.ProductSave, name="ProductSave"),
    path('ProductDisplay/', views.ProductDisplay, name="ProductDisplay"),
    path('EditProduct/<int:dataid>/',views.EditProduct,name="EditProduct"),
path('ProductUpdate/<int:dataid>/', views.ProductUpdate, name="ProductUpdate"),
path('ProductDelete/<int:dataid>/', views.ProductDelete, name="ProductDelete"),
    path('AdminloginPage/', views.AdminloginPage, name="AdminloginPage"),
    path('AdminLogin/',views.AdminLogin,name="AdminLogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('messageDisplay/', views.messageDisplay, name="messageDisplay"),
path('messageDelete/<int:dataid>/', views.messageDelete, name="messageDelete"),

]

