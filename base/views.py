from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from base.models import  Product,Sategory,Category,Destination


def home_page(request,Category_slug=None,Sategory_slug=None,Destination_slug=None,price_slug=None):
	category = None
	sategory=None
	name=None
	sategories=Sategory.objects.all()
	destinations=Destination.objects.all()
	products = Product.objects.all()
	
	context = {
		'products': products,
		'sategories':sategories,
		'destinations':destinations,
	}
	if Sategory_slug:
		sategory= get_object_or_404(Sategory, slug=Sategory_slug )
		products = Product.objects.filter(sategory=sategory)
		context={
		'products':products,
		'destinations':destinations,
		}
		return render(request, 'base/details.html', context)
	
	return render(request, 'base/home.html', context)

	

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug)
	#cart_product_form = CartAddProductForm()
	context = {
		 'product': product,
		#'cart_product_form': cart_product_form
	}
	return render(request, 'base/productdet.html', context)