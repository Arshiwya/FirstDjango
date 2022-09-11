from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView
from products.models import Product

# Create your views here.


# @login_required
# def home(request):

# 	return render(request , 'registration/home.html')



class ProductList(LoginRequiredMixin , ListView):

	queryset = Product.objects.all()
	template_name = 'registration/home.html'
	


class ProductCreate(LoginRequiredMixin , CreateView):
	model = Product
	fields = [
	"admin",
"title",
"slug",
"description",
"categories",
"price",
"image",
"status",
"stars",

	]

	template_name = 'registration/product-create-update.html'