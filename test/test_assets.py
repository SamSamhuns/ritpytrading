import unittest
from ritpytrading import assets


class TestAssetsMethods(unittest.TestCase):
    def setUp(self):
        self._sample_assets_resp = [
            {
                "ticker": "AAPL",
                "type": "equity",
                "description": "Apple Inc",
                "total_quantity": 10000,
                "available_quantity": 5000,
                "lease_price": 120,
                "convert_from": [
                    {
                        "ticker": "string",
                        "quantity": 0
                    }
                ],
                "convert_to": [
                    {
                        "ticker": "string",
                        "quantity": 0
                    }
                ],
                "containment": {
                    "ticker": "string",
                    "quantity": 0
                },
                "ticks_per_conversion": 0,
                "ticks_per_lease": 0,
                "is_available": True,
                "start_period": 0,
                "stop_period": 0
            }
        ]

    def test_asset(self):
        method_obj = assets.assets_response_handle(
            self._sample_assets_resp, ticker='AAPL')
        class_obj = assets.Asset(self._sample_assets_resp[0])
        self.assertEqual(method_obj, class_obj)

    def test_assets_dict(self):
        method_dict = assets.assets_response_handle(self._sample_assets_resp)
        class_dict = {self._sample_assets_resp[0]["ticker"]: assets.Asset(
            self._sample_assets_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
