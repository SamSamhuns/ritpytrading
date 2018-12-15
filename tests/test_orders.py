import unittest
from ritpytrading import orders


class TestOrderMethods(unittest.TestCase):
    def setUp(self):
        self._sample_order_resp = [
            {
                "order_id": 1221,
                "period": 1,
                "tick": 10,
                "trader_id": "trader49",
                "ticker": "CRZY",
                "type": "LIMIT",
                "quantity": 100,
                "action": "BUY",
                "price": 14.21,
                "quantity_filled": 10,
                "vwap": 14.21,
                "status": "OPEN"
            }
        ]

    def test_order(self):
        method_obj = orders.orders_response_handle(
            self._sample_order_resp[0], '/orders/{}')
        class_obj = orders.Order(self._sample_order_resp[0])
        self.assertEqual(method_obj, class_obj)

    def test_orders_dict(self):
        method_dict = orders.orders_response_handle(
            self._sample_order_resp, '/orders')
        class_dict = {self._sample_order_resp[0]["order_id"]: orders.Order(
            self._sample_order_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
