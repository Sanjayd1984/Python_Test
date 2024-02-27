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
