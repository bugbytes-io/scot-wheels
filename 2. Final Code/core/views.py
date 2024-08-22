from django.shortcuts import render
from core.models import Car
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    transmission = request.GET.getlist("transmission")
    cars = Car.objects.filter(is_available=True)
    if transmission:
        cars = cars.filter(transmission__in=transmission)

    paginator = Paginator(cars, 5)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "car_count": cars.count()}
    if "HX-Request" in request.headers:
        return render(request, "cotton/car_list.html", context)
    return render(request, "index.html", context)
