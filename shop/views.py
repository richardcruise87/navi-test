from django.http import HttpResponse
from .models import ShopName


def index(request):
    try:
        shop_name = ShopName.objects.order_by("-date_opened")[0]
    except ShopName.DoesNotExist:
        raise Http404("Shop name not set!")
    return HttpResponse(f"Welcome to the {shop_name.name} homepage!")