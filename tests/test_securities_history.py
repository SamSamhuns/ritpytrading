import unittest
from ritpytrading import securities_history


class TestSecHistoryMethods(unittest.TestCase):
    def setUp(self):
        self._sample_sec_history_resp = [
            {
                "tick": 11,
                "open": 4.12,
                "high": 4.21,
                "low": 4.1,
                "close": 4.15
            }
        ]

    def test_sec_history_dict(self):
        method_dict = securities_history.sec_history_response_handle(
            self._sample_sec_history_resp)
        class_dict = {self._sample_sec_history_resp[0]["tick"]:
                      securities_history.Security_History(
            self._sample_sec_history_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
