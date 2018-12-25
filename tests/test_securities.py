import unittest
from ritpytrading import securities


class TestSecuritiesMethods(unittest.TestCase):
    def setUp(self):
        self._sample_securities_resp = [
            {
                "ticker": "string",
                "type": "SPOT",
                "size": 0,
                "position": 0,
                "vwap": 0,
                "nlv": 0,
                "last": 0,
                "bid": 0,
                "bid_size": 0,
                "ask": 0,
                "ask_size": 0,
                "volume": 0,
                "unrealized": 0,
                "realized": 0,
                "currency": "string",
                "total_volume": 0,
                "limits": [
                    {
                        "name": "string",
                        "units": 0
                    }
                ],
                "interest_rate": 0,
                "is_tradeable": True,
                "is_shortable": True,
                "start_period": 0,
                "stop_period": 0
            }
        ]

    def test_security_dict(self):
        method_dict = securities._security_response_handle(
            self._sample_securities_resp)
        class_dict = {self._sample_securities_resp[0]["ticker"]:
                      securities.Security(
            self._sample_securities_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
