from django.test import TestCase

from order.factories import OrderFactory, ProductFactory
from order.serializers import OrderSerializer


class TestOrderSerializer(TestCase):
    def setUp(self) -> None:
        self.product_1 = ProductFactory(title="Notebook", price=25.00)
        self.product_2 = ProductFactory(title="Colored pencils", price=20.00)

        self.order = OrderFactory(product=(self.product_1, self.product_2))
        self.order_serializer = OrderSerializer(self.order)

    def test_order_serializer(self):
        serializer_data = self.order_serializer.data

        # Verifica os campos esperados
        expected_fields = {"product", "total"}
        self.assertEqual(set(serializer_data.keys()), expected_fields)

        # Verifica os conteúdos dos produtos
        self.assertEqual(serializer_data["product"][0]["title"], self.product_1.title)
        self.assertEqual(serializer_data["product"][1]["title"], self.product_2.title)

        # Verifica o total calculado
        self.assertEqual(float(serializer_data["total"]), 45.00)