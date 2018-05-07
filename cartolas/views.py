from django.shortcuts import render
from .models import Cartolas 

def cartolas(request):
	cartolas = Cartolas.objects.all()
	template_name = 'cartolas.html' 
	context = {
		'cartolas': cartolas
		}
	return render(request, template_name, context)