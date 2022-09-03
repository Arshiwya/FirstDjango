from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from  django.conf.urls.static import static
from .views import home , ProductList , CategoryProductList , single_product 

app_name = 'products'

urlpatterns = [

   path('' , home , name = 'home'),
   path('category/<slug:slug>/' , CategoryProductList.as_view() , name = 'category_page'),
   path('all/', ProductList.as_view() , name ='products'),
   path('single/<slug:slug>/' , single_product  , name = 'single-product')

]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
