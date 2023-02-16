from django.shortcuts import render
from django.db.models import Q
from ekart.models import Products


# Create your views here.
def searchpro(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Products.objects.all().filter(Q(name__contains=query) | Q(pdesc__contains=query))
    return render(request, 'search.html', {'products': products, 'query': query})


