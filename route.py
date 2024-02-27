import unittest
from myapp.models import Product
from myapp.services import ProductService

class TestProductService(unittest.TestCase):
    def setUp(self):
        # Initialize test data or perform setup actions
        self.product_service = ProductService()
        self.products = [
            Product(name="Product 1", category="Category A", availability="In Stock", price=10.99),
            Product(name="Product 2", category="Category B", availability="Out of Stock", price=15.99),
            Product(name="Product 3", category="Category A", availability="In Stock", price=20.99)
        ]
        for product in self.products:
            self.product_service.create_product(product)

    def tearDown(self):
        # Clean up after the test
        for product in self.products:
            self.product_service.delete_product(product.id)

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

    def test_list_all_products(self):
        # Test listing all products
        all_products = self.product_service.get_all_products()
        self.assertEqual(len(all_products), len(self.products), "Number of listed products should match the number of created products")

    def test_list_products_by_name(self):
        # Test listing products by name
        target_name = "Product 1"
        found_products = self.product_service.get_products_by_name(target_name)
        self.assertTrue(found_products, f"Products with name '{target_name}' should exist")
        for product in found_products:
            self.assertEqual(product.name, target_name, f"Product name should match '{target_name}'")

    def test_list_products_by_category(self):
        # Test listing products by category
        target_category = "Category A"
        found_products = self.product_service.get_products_by_category(target_category)
        self.assertTrue(found_products, f"Products with category '{target_category}' should exist")
        for product in found_products:
            self.assertEqual(product.category, target_category, f"Product category should match '{target_category}'")

    def test_list_products_by_availability(self):
        # Test listing products by availability
        target_availability = "In Stock"
        found_products = self.product_service.get_products_by_availability(target_availability)
        self.assertTrue(found_products, f"Products with availability '{target_availability}' should exist")
        for product in found_products:
            self.assertEqual(product.availability, target_availability, f"Product availability should match '{target_availability}'")

if __name__ == '__main__':
    unittest.main()
