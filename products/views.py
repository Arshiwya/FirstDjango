from django.shortcuts import render , get_list_or_404 , get_object_or_404
from   .models import Product , Category
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView , DetailView
from accounts.models import User
from accounts.mixins import AdminAccessMixin



pcategories = Category.objects.filter(status=True , parent=None)

def home(request):

    cat = Category.objects.get(title='mens')
    product_men = cat.product.published()

    
    cat2 = Category.objects.get(title='womens')
    product_women = cat2.product.published()


    cat3 = Category.objects.get(title='kids')
    product_kids = cat3.product.published()



    
    context = {
        "categories": pcategories,
        "product_men":product_men[:4],
        "product_women":product_women[:4],
        "product_kids" : product_kids[:4],
        "cat_men" :cat,
        "cat_women" : cat2,
        "cat_kids" :cat3,
         }

    return render(request ,'products/index.html' , context=context)



# # def products(request):




#     products_list = Product.objects.filter(status='p')
#     paginator =Paginator(products_list , 6 )
#     page = request.GET.get('p')
#     products =paginator.get_page(page)
#     context = {
#         "products" :products,
#         "categories" :pcategories
#     }

#     return  render(request, 'products/products.html' , context=context)



class ProductList(ListView):
   
    paginate_by = 6
    queryset = Product.objects.published()
    template_name = 'products/products_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = pcategories
        return context
    









# def category(request , slug):

#     cat = Category.objects.get(slug = slug)
#     subcats = cat.subcat.filter(status = True)
#     product_list = cat.product.all()
#     paginator = Paginator(product_list , 6)
#     page = request.GET.get('p')
#     products = paginator.get_page(page)

#     context={
#         "products" : products,
#         "categories": pcategories,
#         "category":get_object_or_404(Category , status = True , slug=slug),
#         "subcats":subcats
#     }


#     return render(request , 'products/categories.html' , context= context)




class CategoryProductList(ListView):
    paginate_by = 6
    template_name = 'products/categories.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category , status = True , slug=slug)
        
        return category.product.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = pcategories
        context["category"] = category
        return context


class ProductPreview(AdminAccessMixin , DetailView):
    template_name = 'products/single-product.html'
    def get_object(self):
        global product
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product , pk=pk)

        return get_object_or_404(Product , pk=pk)


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["admin"] = product.admin
        
        return context









        


    






def single_product(request , slug):
    product = get_object_or_404(Product , slug=slug , status='p')
    admin = product.admin
    print(admin)

    context = {
        "categories": pcategories,
        "admin" :admin,

        "product": product
    }

    return render(request , 'products/single-product.html' , context=context)












def adminpage(request , username):


    
    
    admin = User.objects.get(username = username)
    product_list = admin.admin.published()
    paginator = Paginator(product_list , 6)
    page = request.GET.get('p')
    products =paginator.get_page(page)
    context={
    "admin" : admin ,
    "categories": pcategories,
    "products" : products,

    }


    return render(request , 'products/admin_page.html' ,  context)
