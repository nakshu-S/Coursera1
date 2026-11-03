def test_update_a_product(self):
    """Test updating a product"""
    product = ProductFactory()

    product.name = "Updated Product"
    product.price = 99.99

    product.update()

    updated_product = ProductFactory.find(product.id)

    self.assertEqual(updated_product.name, "Updated Product")
    self.assertEqual(updated_product.price, 99.99)