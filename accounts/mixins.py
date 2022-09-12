from django.http import Http404

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