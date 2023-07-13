from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Categoria, Proveedor
def inicio(request):
    return render(request, 'home.html')

def productos(request):
    productos = Producto.objects.all()
    proovedor = Proveedor.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productos.html', {'productos':productos, 'proveedor':proovedor, 'categorias':categorias})

def productoFormulario(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        proveedor_id = request.POST.get('proveedor')
        if categoria_id == 'nueva':
            # Seleccionó una nueva categoría, con lo cual primero lo guardo.
            nueva_categoria = Categoria(nombre=request.POST['nueva_categoria'])
            nueva_categoria.save()
            categoria_id = nueva_categoria.id #Guardo el id de la categoria generada, para poder referenciarla posteriormente.
        if proveedor_id == 'nueva':
            nuevo_proveedor = Proveedor(nombre=request.POST['nuevo_proveedor'])
            nuevo_proveedor.save()
            proveedor_id = nuevo_proveedor.id
        producto = Producto.objects.create(nombre=request.POST['nombre'],precio=request.POST['precio'],stock=request.POST['stock'],categoria_id=categoria_id, proveedor_id=proveedor_id)
        producto.save()
        return render(request, 'home.html')
    proveedores = Proveedor.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'productoFormulario.html', {'categorias':categorias})
