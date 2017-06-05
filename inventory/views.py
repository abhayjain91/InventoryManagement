from django.shortcuts import render
from rest_framework.decorators import api_view

from inventory.models import Inventory


def index(request):
    return render(request, 'index.html')


def get_inventories(request):
    inventories = Inventory.objects().order_by("-_id")
    return render(request, "list_inventories.html", {"inventories": inventories})


@api_view(['POST'])
def add_inventory(request):
    return
