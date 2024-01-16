from .keranjang import Susanti

def keranjang(request):
    return {'keranjang': Susanti(request)}