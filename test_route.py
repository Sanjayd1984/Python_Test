import pytest
from sanjay_test_Module import Product  

@pytest.fixture
def sample_product():
    return Product(id=1, name="Test Product", price=10.0, category="Test Category", availability=True)

def test_read_product(sample_product):
    # Test case to verify the read operation
    product_id = sample_product.id
    retrieved_product = Product.read(product_id)  # Assuming I have a read method in your Product class
    assert retrieved_product == sample_product
----------------------------------------
import unittest
from myapp.models import Product
from myapp.services import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        # Initialize test data or perform setup actions
        self.product_service = ProductService()
        self.product = Product(name="Test Product", category="Test Category", availability="In Stock", price=10.99)
        self.product_service.create_product(self.product)

    def tearDown(self):
        # Clean up after the test
        self.product_service.delete_product(self.product.id)

    def test_delete_product(self):
        # Test deleting a product
        initial_count = len(self.product_service.get_all_products())
        self.product_service.delete_product(self.product.id)
        final_count = len(self.product_service.get_all_products())
        self.assertEqual(final_count, initial_count - 1, "Product count should decrease by 1 after deletion")

if __name__ == '__main__':
    unittest.main()
---------------------------
import unittest
from myapp.models import Product
from myapp.services import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        # Initialize test data or perform setup actions
        self.product_service = ProductService()
        self.products = [
            Product(name="Test Product 1", category="Test Category", availability="In Stock", price=10.99),
            Product(name="Test Product 2", category="Test Category", availability="Out of Stock", price=15.99),
            Product(name="Test Product 3", category="Test Category", availability="In Stock", price=20.99)
        ]
        for product in self.products:
            self.product_service.create_product(product)

    def tearDown(self):
        # Clean up after the test
        for product in self.products:
            self.product_service.delete_product(product.id)

    def test_list_all_products(self):
        # Test listing all products
        all_products = self.product_service.get_all_products()
        self.assertEqual(len(all_products), len(self.products), "Number of listed products should match the number of created products")

if __name__ == '__main__':
    unittest.main()
--------------------------------------------------------
import unittest
from myapp.models import Product
from myapp.services import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        # Initialize test data or perform setup actions
        self.product_service = ProductService()
        self.products = [
            Product(name="Test Product 1", category="Test Category", availability="In Stock", price=10.99),
            Product(name="Test Product 2", category="Test Category", availability="Out of Stock", price=15.99),
            Product(name="Test Product 3", category="Test Category", availability="In Stock", price=20.99)
        ]
        for product in self.products:
            self.product_service.create_product(product)

    def tearDown(self):
        # Clean up after the test
        for product in self.products:
            self.product_service.delete_product(product.id)

    def test_find_product_by_name(self):
        # Test finding a product by name
        target_name = "Test Product 2"
        found_product = self.product_service.find_product_by_name(target_name)
        self.assertIsNotNone(found_product, f"Product with name '{target_name}' should exist")
        self.assertEqual(found_product.name, target_name, f"Found product name should match '{target_name}'")

if __name__ == '__main__':
    unittest.main()
	-------------------------------------------------
	
	import unittest
from myapp.models import Product
from myapp.services import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        # Initialize test data or perform setup actions
        self.product_service = ProductService()
        self.products = [
            Product(name="Test Product 1", category="Category A", availability="In Stock", price=10.99),
            Product(name="Test Product 2", category="Category B", availability="Out of Stock", price=15.99),
            Product(name="Test Product 3", category="Category A", availability="In Stock", price=20.99)
        ]
        for product in self.products:
            self.product_service.create_product(product)

    def tearDown(self):
        # Clean up after the test
        for product in self.products:
            self.product_service.delete_product(product.id)

    def test_find_product_by_category(self):
        # Test finding products by category
        target_category = "Category A"
        found_products = self.product_service.find_products_by_category(target_category)
        self.assertTrue(found_products, f"Products with category '{target_category}' should exist")
        for product in found_products:
            self.assertEqual(product.category, target_category, f"Product category should match '{target_category}'")

    def test_find_product_by_availability(self):
        # Test finding products by availability
        target_availability = "In Stock"
        found_products = self.product_service.find_products_by_availability(target_availability)
        self.assertTrue(found_products, f"Products with availability '{target_availability}' should exist")
        for product in found_products:
            self.assertEqual(product.availability, target_availability, f"Product availability should match '{target_availability}'")

    def test_read_product(self):
        # Test reading a product
        product_id = self.products[0].id
        retrieved_product = self.product_service.read_product(product_id)
        self.assertIsNotNone(retrieved_product, "Retrieved product should not be None")
        self.assertEqual(retrieved_product.id, product_id, "Retrieved product ID should match the requested product ID")

    def test_update_product(self):
        # Test updating a product
        product_id = self.products[0].id
        updated_product_data = {"name": "Updated Product", "price": 25.99}
        self.product_service.update_product(product_id, **updated_product_data)
        updated_product = self.product_service.read_product(product_id)
        for key, value in updated_product_data.items():
            self.assertEqual(getattr(updated_product, key), value, f"Updated product {key} should match {value}")

    def test_delete_product(self):
        # Test deleting a product
        product_id = self.products[0].id
        initial_count = len(self.product_service.get_all_products())
        self.product_service.delete_product(product_id)
        final_count = len(self.product_service.get_all_products())
        self.assertEqual(final_count, initial_count - 1, "Product count should decrease by 1 after deletion")

if __name__ == '__main__':
    unittest.main()

