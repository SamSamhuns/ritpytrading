from ..ritpytrading import assets
import unittest


class TestAssetsMethods(unittest.TestCase):

    def test_asset(self):
        sample_json_resp = [
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
        self.assertEqual(sample_json_resp, assets.assets_response_handle(
            sample_json_resp, ticker='AAPL'))

    def test_assets_dict(self):
        pass

    def test_assets_json(self):
        pass


if __name__ == "__main__":
    unittest.main()
