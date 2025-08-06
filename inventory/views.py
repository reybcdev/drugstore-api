from rest_framework import viewsets
from .models import (
    Category, Supplier, Product, 
    Customer, Employee, Purchase, 
    PurchaseItem, Sale, SaleItem
)
from .serializers import (
    CategorySerializer, SupplierSerializer, ProductSerializer,
    CustomerSerializer, EmployeeSerializer, PurchaseSerializer,
    PurchaseItemSerializer, SaleSerializer, SaleItemSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category')
        supplier = self.request.query_params.get('supplier')
        
        if category:
            queryset = queryset.filter(category__id=category)
            
        if supplier:
            queryset = queryset.filter(supplier__id=supplier)
            
        return queryset

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseItemViewSet(viewsets.ModelViewSet):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
    
    def get_queryset(self):
        queryset = PurchaseItem.objects.all()
        purchase = self.request.query_params.get('purchase')
        
        if purchase:
            queryset = queryset.filter(purchase__id=purchase)
            
        return queryset

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    
    def get_queryset(self):
        queryset = SaleItem.objects.all()
        sale = self.request.query_params.get('sale')
        
        if sale:
            queryset = queryset.filter(sale__id=sale)
            
        return queryset
