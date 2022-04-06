from rest_framework import viewsets,response
from rest_framework.views import APIView
from .serializers import CartSerialzer, CustomerSerializer, PlacedOrderSerializer, ProductSerializer
from orm.models import Cart, Customers, Placed_orders, Products

class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customers.objects.all()
    serializer_class=CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductSerializer
    
class CartViewSet(viewsets.ModelViewSet):
    queryset=Cart.objects.all()
    serializer_class=CartSerialzer

class PlacedOrderViewSet(viewsets.ModelViewSet):
    queryset=Placed_orders.objects.all()
    serializer_class=PlacedOrderSerializer
    
class CustomerView(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Customers.objects.all()
        serialzer=CustomerSerializer(queryset, many=True)
        return response(serialzer.data)
    def post(self,request,*args,**kwargs):
        serializer=CustomerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
        return response(serializer.errors)
# class CustomerPerticularViewSet(viewsets.ModelViewSet):
#     queryset=Customers.objects.filter(customer_name='Nithin v v')
#     serializer_class=CustomerSerializer
    
# class PlacedOrderperticularViewSet(viewsets.ModelViewSet):
#     queryset=Placed_orders.objects.filter(placed_order_id='2')
#     serializer_class=PlacedOrderSerializer
    
# class PlacedOrderByIdViewSet(viewsets.ModelViewSet):
#     queryset=Placed_orders.objects.values('placed_order_id','placed_order_user_id')
#     serializer_class=PlacedOrderSerializer
    
    