from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(
            title="French fries",
            slug="french-fries",
            description="Soft and crispy, served as a side dish.",
            active=True
        )
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer_fields(self):
        serializer_data = self.category_serializer.data

    def test_category_serializer_content(self):
        serializer_data = self.category_serializer.data

        self.assertEqual(serializer_data["title"], "French fries")
        self.assertEqual(serializer_data["slug"], "french-fries")
        self.assertEqual(serializer_data["description"], "Soft and crispy, served as a side dish.")
        self.assertEqual(serializer_data["active"], True)