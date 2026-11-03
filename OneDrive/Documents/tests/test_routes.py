
import unittest
import json
from service import app


class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()
        self.headers = {"Content-Type": "application/json"}

    def create_product(self):
        data = {
            "name": "Laptop",
            "description": "Test laptop",
            "price": 999.99,
            "category": "Electronics",
            "available": True
        }
        response = self.client.post(
            "/products",
            data=json.dumps(data),
            headers=self.headers
        )
        self.assertIn(response.status_code, [200, 201])
        return response.get_json()

    # Task 3a: READ
    def test_read_product(self):
        product = self.create_product()
        product_id = product["id"]

        response = self.client.get(f"/products/{product_id}")

        self.assertEqual(response.status_code, 200)

    # Task 3b: UPDATE
    def test_update_product(self):
        product = self.create_product()
        product_id = product["id"]

        data = {
            "name": "Updated Laptop",
            "price": 1200.00
        }

        response = self.client.put(
            f"/products/{product_id}",
            data=json.dumps(data),
            headers=self.headers
        )

        self.assertEqual(response.status_code, 200)

    # Task 3c: DELETE
    def test_delete_product(self):
        product = self.create_product()
        product_id = product["id"]

        response = self.client.delete(
            f"/products/{product_id}"
        )

        self.assertIn(response.status_code, [200, 204])

    # Task 3d: LIST ALL
    def test_list_all_products(self):
        self.create_product()

        response = self.client.get("/products")

        self.assertEqual(response.status_code, 200)

    # Task 3e: LIST BY NAME
    def test_list_products_by_name(self):
        self.create_product()

        response = self.client.get("/products?name=Laptop")

        self.assertEqual(response.status_code, 200)

    # Task 3f: LIST BY CATEGORY
    def test_list_products_by_category(self):
        self.create_product()

        response = self.client.get(
            "/products?category=Electronics"
        )

        self.assertEqual(response.status_code, 200)

    # Task 3g: LIST BY AVAILABILITY
    def test_list_products_by_availability(self):
        self.create_product()

        response = self.client.get(
            "/products?available=true"
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
