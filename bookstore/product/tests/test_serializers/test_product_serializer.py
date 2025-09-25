from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import ProductSerializer


class TestProductSerializer(TestCase):
    def setUp(self) -> None:
        self.category_1 = CategoryFactory(title="technology")
        self.category_2 = CategoryFactory(title="school")

        self.product_1 = ProductFactory(
            title="Mouse",
            description="Wireless mouse with battery included.",
            price=100,
            active=True,
            category=[self.category_1],
        )

        self.product_2 = ProductFactory(
            title="Notebook",
            description="10-subject hardcover notebook.",
            price=25,
            active=True,
            category=[self.category_2],
        )

        self.product_serializer = ProductSerializer(self.product_1)
        self.product_serializer = ProductSerializer(self.product_2)

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["title"], "Mouse")
        self.assertEqual(serializer_data["description"], "Wireless mouse with battery included.")
        self.assertEqual(serializer_data["price"], 100)
        self.assertEqual(serializer_data["active"], True)
        self.assertEqual(serializer_data["category"][0]["title"], "technology")

    def test_product_serializer(self):
        serializer_data = self.product_serializer.data
        self.assertEqual(serializer_data["title"], "Notebook")
        self.assertEqual(serializer_data["description"], "10-subject hardcover notebook.")
        self.assertEqual(serializer_data["price"], 25)
        self.assertEqual(serializer_data["active"], True)
        self.assertEqual(serializer_data["category"][0]["title"], "school")