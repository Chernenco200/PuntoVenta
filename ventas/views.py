from django.shortcuts import render

# Create your views here.
def ventas(request):
	context = {}
	return render(request, 'ventas.html', context)

def clientes(request):
	context = {}
	return render(request, 'clientes.html', context)