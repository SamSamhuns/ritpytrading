import unittest
from ritpytrading import tenders


class TestTendersMethods(unittest.TestCase):
    def setUp(self):
        self._sample_tender_resp = [
            {
                "tender_id": 100,
                "period": 0,
                "tick": 0,
                "expires": 0,
                "caption": "string",
                "quantity": 0,
                "action": "BUY",
                "is_fixed_bid": True,
                "price": 0
            }
        ]

    def test_tenders_dict(self):
        method_dict = tenders.tender_response_handle(self._sample_tender_resp)
        class_dict = {self._sample_tender_resp[0]["tender_id"]: tenders.Tender(
            self._sample_tender_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
