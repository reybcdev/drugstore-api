from django.core.management.base import BaseCommand
from inventory.models import (
    Category, Supplier, Product, 
    Customer, Employee
)

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')
        
        # Create Categories
        self.stdout.write('Creating categories...')
        categories = [
            {'name': 'Medications', 'description': 'Prescription and over-the-counter medications'},
            {'name': 'Personal Care', 'description': 'Personal hygiene and beauty products'},
            {'name': 'First Aid', 'description': 'First aid supplies and equipment'},
            {'name': 'Vitamins & Supplements', 'description': 'Dietary supplements and vitamins'},
        ]
        
        for category_data in categories:
            Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            
        # Create Suppliers
        self.stdout.write('Creating suppliers...')
        suppliers = [
            {
                'name': 'PharmaCorp Inc.',
                'contact_name': 'John Smith',
                'phone': '555-123-4567',
                'email': 'john@pharmacorp.com',
                'address': '123 Med Street, Pharmaville, PC 12345'
            },
            {
                'name': 'MediSupply Co.',
                'contact_name': 'Jane Doe',
                'phone': '555-987-6543',
                'email': 'jane@medisupply.com',
                'address': '456 Health Avenue, Medicity, MC 67890'
            },
        ]
        
        for supplier_data in suppliers:
            Supplier.objects.get_or_create(
                name=supplier_data['name'],
                defaults={
                    'contact_name': supplier_data['contact_name'],
                    'phone': supplier_data['phone'],
                    'email': supplier_data['email'],
                    'address': supplier_data['address']
                }
            )
            
        # Create Employees
        self.stdout.write('Creating employees...')
        employees = [
            {
                'name': 'Michael Johnson',
                'position': 'Pharmacist',
                'phone': '555-111-2222',
                'email': 'michael@drugstore.com'
            },
            {
                'name': 'Emily Davis',
                'position': 'Sales Associate',
                'phone': '555-333-4444',
                'email': 'emily@drugstore.com'
            },
        ]
        
        for employee_data in employees:
            Employee.objects.get_or_create(
                name=employee_data['name'],
                defaults={
                    'position': employee_data['position'],
                    'phone': employee_data['phone'],
                    'email': employee_data['email']
                }
            )
            
        # Create Customers
        self.stdout.write('Creating customers...')
        customers = [
            {
                'name': 'Robert Wilson',
                'phone': '555-555-1212',
                'email': 'robert@example.com',
                'address': '789 Customer Lane, Buytown, BT 45678'
            },
            {
                'name': 'Sarah Thompson',
                'phone': '555-666-7777',
                'email': 'sarah@example.com',
                'address': '101 Shopper Road, Clientville, CV 98765'
            },
        ]
        
        for customer_data in customers:
            Customer.objects.get_or_create(
                name=customer_data['name'],
                defaults={
                    'phone': customer_data['phone'],
                    'email': customer_data['email'],
                    'address': customer_data['address']
                }
            )
            
        # Create Products
        self.stdout.write('Creating products...')
        medications = Category.objects.get(name='Medications')
        personal_care = Category.objects.get(name='Personal Care')
        first_aid = Category.objects.get(name='First Aid')
        vitamins = Category.objects.get(name='Vitamins & Supplements')
        
        pharmacorp = Supplier.objects.get(name='PharmaCorp Inc.')
        medisupply = Supplier.objects.get(name='MediSupply Co.')
        
        products = [
            {
                'name': 'Ibuprofen 200mg',
                'description': 'Pain reliever and fever reducer',
                'category': medications,
                'supplier': pharmacorp,
                'price': 8.99,
                'cost': 4.50,
                'stock': 100,
                'sku': 'MED-IBU-200'
            },
            {
                'name': 'Moisturizing Lotion',
                'description': 'Daily moisturizer for all skin types',
                'category': personal_care,
                'supplier': medisupply,
                'price': 12.99,
                'cost': 6.25,
                'stock': 50,
                'sku': 'PC-LOT-001'
            },
            {
                'name': 'Adhesive Bandages',
                'description': 'Pack of 50 assorted sizes',
                'category': first_aid,
                'supplier': medisupply,
                'price': 5.49,
                'cost': 2.75,
                'stock': 75,
                'sku': 'FA-BAND-50'
            },
            {
                'name': 'Vitamin C 1000mg',
                'description': 'Immune support supplement, 60 tablets',
                'category': vitamins,
                'supplier': pharmacorp,
                'price': 15.99,
                'cost': 7.80,
                'stock': 30,
                'sku': 'VS-VITC-60'
            },
        ]
        
        for product_data in products:
            Product.objects.get_or_create(
                sku=product_data['sku'],
                defaults={
                    'name': product_data['name'],
                    'description': product_data['description'],
                    'category': product_data['category'],
                    'supplier': product_data['supplier'],
                    'price': product_data['price'],
                    'cost': product_data['cost'],
                    'stock': product_data['stock']
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))
