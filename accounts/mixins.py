from django.http import Http404
from django.shortcuts import  get_object_or_404
from products.models import Product

class FieldMixin():

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_superuser:
			self.fields = 	fields = [	"admin","title","slug","description","categories","price","image","status","stars"]

		elif request.user.is_admin:
			self.fields = 	fields = ["title","slug","description","categories","price","image","stars"]

		else:
			raise Http404("you havent access")
			


		return super().dispatch(request, *args, **kwargs)




class FormValidMixin():
	def form_valid(self , form):
		if self.request.user.is_superuser:
			form.save()

		else:
			self.obj = form.save(commit = False)
			self.obj.admin = self.request.user
			self.obj.status = 'd'


		return  super().form_valid(form)




class AdminAccessMixin():

	def dispatch(self, request,pk,*args, **kwargs):
		product = get_object_or_404(Product , pk = pk)

		if product.admin == request.user and product.status in ['d' , 'b']   or request.user.is_superuser :
			return super().dispatch(request, *args, **kwargs)

		else:
			raise Http404("you havent access")
			


		