from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Carrito , ItemCarrito
# Create your views here.
def index(request):
    products = Producto.objects.all()  # Obtén todos los productos
    
    return render(request, 'Index.html', {'products': products}) # Pasa los productos al contexto del template

def ver_carrito(request):
    carrito_id = request.session.get("carrito_id")
    if carrito_id:
        carrito = get_object_or_404(Carrito, id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session["carrito_id"] = carrito.id

    return render(request, "carrito.html", {"carrito": carrito})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito_id = request.session.get("carrito_id")

    if carrito_id:
        carrito = get_object_or_404(Carrito, id=carrito_id)
    else:
        carrito = Carrito.objects.create()
        request.session["carrito_id"] = carrito.id

    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

    if not created:
        item.cantidad += 1
        item.save()

    return redirect("ver_carrito")

def eliminar_item(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    item.delete()
    return redirect("ver_carrito")