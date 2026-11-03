
import unittest
from tests.factories import ProductFactory


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = ProductFactory()

    # Task 2a: READ
    def test_read_a_product(self):
        product = ProductFactory()
        found_product = ProductFactory.find(product.id)

        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.id, product.id)

    # Task 2b: UPDATE
    def test_update_a_product(self):
        product = ProductFactory()
        product.name = "Updated Product"
        product.price = 99.99
        product.update()

        updated_product = ProductFactory.find(product.id)

        self.assertEqual(updated_product.name, "Updated Product")
        self.assertEqual(updated_product.price, 99.99)

    # Task 2c: DELETE
    def test_delete_a_product(self):
        product = ProductFactory()
        product_id = product.id

        product.delete()

        deleted_product = ProductFactory.find(product_id)
        self.assertIsNone(deleted_product)

    # Task 2d: LIST ALL
    def test_list_all_products(self):
        ProductFactory()
        ProductFactory()

        products = ProductFactory.all()

        self.assertIsNotNone(products)
        self.assertGreaterEqual(len(products), 2)

    # Task 2e: FIND BY NAME
    def test_find_by_name(self):
        product = ProductFactory()
        product.name = "Laptop"
        product.update()

        found_product = ProductFactory.find_by_name("Laptop")

        self.assertIsNotNone(found_product)
        self.assertEqual(found_product.name, "Laptop")

    # Task 2f: FIND BY CATEGORY
    def test_find_by_category(self):
        product = ProductFactory()
        product.category = "Electronics"
        product.update()

        products = ProductFactory.find_by_category("Electronics")

        self.assertGreaterEqual(len(products), 1)
        self.assertEqual(products[0].category, "Electronics")

    # Task 2g: FIND BY AVAILABILITY
    def test_find_by_availability(self):
        product = ProductFactory()
        product.available = True
        product.update()

        products = ProductFactory.find_by_availability(True)

        self.assertGreaterEqual(len(products), 1)
        self.assertTrue(products[0].available)


if __name__ == "__main__":
    unittest.main()
