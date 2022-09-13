from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin , FormValidMixin , AdminAccessMixin
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from products.models import Product
from django.urls import reverse_lazy



# Create your views here.


# @login_required
# def home(request):

# 	return render(request , 'registration/home.html')



class ProductList(LoginRequiredMixin , ListView):

	queryset = Product.objects.all()
	template_name = 'registration/home.html'





class ProductCreate(LoginRequiredMixin,FormValidMixin,FieldMixin  , CreateView):
	model = Product
	

	template_name = 'registration/product-create-update.html'




class ProductUpdate(AdminAccessMixin ,FormValidMixin,FieldMixin  , UpdateView):
	model = Product
	

	template_name = 'registration/product-create-update.html'	



class ProductDelete(DeleteView):

	model = Product
	success_url = reverse_lazy('accounts:home')
	template_name = 'registration/product-delete.html'