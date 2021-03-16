from django.contrib import admin
from .models import Category, Product, Sategory, Destination
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','image']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
class ProductAdmin(admin.ModelAdmin):
	"""docstring for Category"""
	list_display = ['name', 'slug','image']
	prepopulated_fields = {'slug': ('name',)}
admin.site.register( Product,ProductAdmin)

class SategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug','image']
admin.site.register(Sategory,SategoryAdmin)

class DestinationAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']	
admin.site.register(Destination,DestinationAdmin)