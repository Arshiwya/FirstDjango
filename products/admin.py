from django.contrib import admin

from .models import Category , Product

admin.site.site_header = 'My Django Panel'


# admin panel actions

def make_published(modeladmin , request , queryset):

        rows_updated = queryset.update(status='p')
        if rows_updated == 1 :
            message_bit = " one product was published"

        else:
            message_bit = f'{rows_updated} products were published '

        modeladmin.message_user(request , message_bit)

    

make_published.short_description = 'make published'


def make_draft(modeladmin , request , queryset):

        rows_updated = queryset.update(status='d')
        if rows_updated == 1 :
            message_bit = " one product was drafted"

        else:
            message_bit = f'{rows_updated} products were drafted '

        modeladmin.message_user(request , message_bit)


# ============================================================================================














class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' ,'get_thumbnail', 'status', 'price', 'created' , 'cat_to_str' ]
    list_filter = ['status']
    search_fields = ['title' , 'slug']
    prepopulated_fields ={ 'slug' :('title' , )}
    actions = [make_published , make_draft]


    def cat_to_str(self , obj):
        return ' , '.join([cat.title for cat in obj.categories.published()])

    cat_to_str.short_description = 'categories'



admin.site.register(Product , ProductAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title' ,'get_thumbnail', 'status','parent' ]
    list_filter = ['status']
    search_fields = ['title' , 'slug']
    prepopulated_fields ={ 'slug' :('title' , )}



admin.site.register(Category , CategoryAdmin)
