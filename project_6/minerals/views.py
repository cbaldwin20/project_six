from django.shortcuts import get_object_or_404, render

from random import randint 

from .models import Mineral  
# Create your views here.


def minerals_list(request):
	"""gets all the minerals to display for the home page"""
	minerals = Mineral.objects.all()
	return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
	"""shows the details of a specific mineral"""
	if pk == '1000000':
		x = Mineral.objects.all()
		x = len(x)
		pk = randint(1, x)
	mineral = get_object_or_404(Mineral, pk=pk)
	return render(request, 'minerals/detail.html', {'mineral': mineral})