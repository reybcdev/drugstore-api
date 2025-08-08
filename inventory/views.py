from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    Category, Supplier, Product, 
    Customer, Employee, Purchase, 
    PurchaseItem, Sale, SaleItem, StockAdjustment
)
from .serializers import (
    CategorySerializer, SupplierSerializer, ProductSerializer,
    CustomerSerializer, EmployeeSerializer, PurchaseSerializer,
    PurchaseItemSerializer, SaleSerializer, SaleItemSerializer,
    StockAdjustmentSerializer
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
        
        # Añadir filtros adicionales para la gestión de inventario
        min_stock = self.request.query_params.get('min_stock')
        max_stock = self.request.query_params.get('max_stock')
        search = self.request.query_params.get('search')
        
        if min_stock:
            queryset = queryset.filter(stock__gte=min_stock)
            
        if max_stock:
            queryset = queryset.filter(stock__lte=max_stock)
            
        if search:
            queryset = queryset.filter(name__icontains=search) | queryset.filter(sku__icontains=search)
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Devuelve productos con stock bajo (menos de 10 unidades)"""
        low_stock_products = Product.objects.filter(stock__lt=10)
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def adjust_stock(self, request, pk=None):
        """Ajustar el stock de un producto manualmente"""
        product = self.get_object()
        
        quantity = request.data.get('quantity', None)
        reason = request.data.get('reason', '')
        
        if quantity is None:
            return Response(
                {"error": "Debe proporcionar una cantidad para el ajuste"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            quantity = int(quantity)
            # Guardar el valor anterior para registro
            previous_stock = product.stock
            # Actualizar el stock
            product.stock += quantity
            product.save()
            
            # Crear un registro de ajuste de stock
            StockAdjustment.objects.create(
                product=product,
                quantity=quantity,
                reason=reason
            )
            
            return Response({
                "success": True,
                "product": product.name,
                "previous_stock": previous_stock,
                "adjustment": quantity,
                "new_stock": product.stock,
                "reason": reason
            })
        except ValueError:
            return Response(
                {"error": "La cantidad debe ser un número entero"},
                status=status.HTTP_400_BAD_REQUEST
            )

class StockAdjustmentViewSet(viewsets.ModelViewSet):
    queryset = StockAdjustment.objects.all()
    serializer_class = StockAdjustmentSerializer

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
