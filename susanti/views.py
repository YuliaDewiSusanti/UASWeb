from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from dewi.models import Produk
from .keranjang import Susanti
from .forms import SusantiAddProductForm

@require_POST
def susanti_add(request, product_id):
    susanti = Susanti(request) # create a new cart object passing it the request object
    product = get_object_or_404(Produk, id=product_id)
    quantity = int(request.POST.get('quantity'))
    form = SusantiAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        susanti.add(product=product, quantity=quantity, update_quantity=cd['update'])
    return redirect('susanti_detail')

def susanti_remove(request, product_id):
    susanti = Susanti(request)
    product = get_object_or_404(Produk, id=product_id)
    susanti.remove(product)
    return redirect('susanti_detail')

def susanti_detail(request):
    susanti = Susanti(request)
    context = {
        'judul': 'Halaman Pemesanan Produk',
        'susanti':susanti
    }
    for item in susanti:
        item['update_quantity_form'] = SusantiAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'pemesanan.html',context)

