import unittest
from CATEGORY.models import Product  # Adjust the import to your project's structure
from CATEGORY import db

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Set up a test database or any required initial state
        db.create_all()  # Ensure the database and tables are created
        self.product1 = Product(name="Test Product 1", description="This is a test product 1", price=9.99, stock=10, category="Electronics")
        self.product2 = Product(name="Test Product 2", description="This is a test product 2", price=19.99, stock=20, category="Electronics")
        self.product3 = Product(name="Test Product 3", description="This is a test product 3", price=29.99, stock=30, category="Books")
        db.session.add(self.product1)
        db.session.add(self.product2)
        db.session.add(self.product3)
        db.session.commit()

    def tearDown(self):
        # Clean up the database after each test
        db.session.remove()
        db.drop_all()

    def test_find_by_category(self):
        # Find products by category in the database
        electronics_products = Product.query.filter_by(category
