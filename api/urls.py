from django.urls import path
from rest_framework.routers import DefaultRouter
from api.apiviews import ProductoList, ProductoDetalle, \
    CategoriaList, \
     SubcategoriaList, CategoriaDetalle, ProductoViewSet, enviar_email
     
     #SubcategoriaList, CategoriaDetalle, SubCategoriaAdd, ProductoViewSet
    #  CategoriaSave, SubCategoriaSave, CategoriaList, \

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('v1/productos/',ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/',CategoriaList.as_view(), name='categoria_save'),
    #path('v1/subcategorias/',SubcategoriaList.as_view(), name='subcategoria_save')
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_detalle'),
    path('v1/categorias/<int:pk>/subcategorias/',SubcategoriaList.as_view(), name='categoria_detalle'), 
    path('v1/send_email/',enviar_email, name='enviar_email'), 
    # path('v1/categorias/<int:cat_pk>/', SubCategoriaAdd.as_view(), name='sc_add'),
]

urlpatterns += router.urls