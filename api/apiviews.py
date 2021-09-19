""" from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404 """
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

from .models import Producto, Categoria, Subcategoria
from .serializers import ProductoSerializer, CategoriaSerializer, SubcategoriaSerializer

""" class ProductoList(APIView):
    def get(self, request):
        prod = Producto.objects.all()[:20]
        data = ProductoSerializer(prod, many=True).data
        return Response(data)

class ProductoDetalle(APIView):
    def get(self,request,pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)   """

class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.using('test').all()
    serializer_class = ProductoSerializer

class ProductoDetalle(generics.RetrieveDestroyAPIView):
    queryset = Producto.objects.using('test').all()
    serializer_class = ProductoSerializer

class CategoriaSave(generics.CreateAPIView):
    serializer_class = CategoriaSerializer

class SubCategoriaSave(generics.CreateAPIView):
    serializer_class = SubcategoriaSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.using('test').all()
    serializer_class = CategoriaSerializer

class SubcategoriaList(generics.ListCreateAPIView):
    queryset = Subcategoria.objects.using('test').all()
    serializer_class = SubcategoriaSerializer 

class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.using('test').all()
    serializer_class = CategoriaSerializer

class SubCategoriaAdd(APIView):
    def post(self, request, cat_pk):
        descripcion = request.data.get("descripcion")
        data = {"categoria": cat_pk, "descripcion": descripcion}
        serializer = SubcategoriaSerializer(data=data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

@csrf_exempt
def enviar_email(request):
    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'remote.service.tuc@gmail.com',
    #     ['fernandez.pablo44@gmail.com'],
    #     fail_silently=False,
    # )

    pedido = {
        'numero': 1234,
        'fecha': '19/09/2021',
        'cliente': 'Pablo Fernández',
        'tienda': 'TOP BABY'
    }

    with open(settings.BASE_DIR.__str__() + "/templates/email_template.txt") as file:
        pedido_msj = file.read()

    msj = EmailMultiAlternatives(subject='NUEVO PEDIDO TIENDA ONLINE',from_email='remote.service.tuc@gmail.com', body=pedido_msj, to=['fernandez.pablo44@gmail.com'])
    html_template = get_template('email_template.html').render(pedido)
    msj.attach_alternative(html_template, 'text/html')
    msj.send()

    return JsonResponse({'mensaje': 'Hola'}, status=400)