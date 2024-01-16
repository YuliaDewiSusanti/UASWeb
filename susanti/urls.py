from django.urls import path
from . import views

urlpatterns = [
    path('', views.susanti_detail, name='susanti_detail'),
    path('add/<product_id>', views.susanti_add, name='susanti_add'),
    path('remove/<product_id>', views.susanti_remove, name='susanti_remove'),
]