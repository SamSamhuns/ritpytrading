import unittest
from ritpytrading import case


class TestCaseMethods(unittest.TestCase):
    def setUp(self):
        self._sample_case_resp = {
            "name": "string",
            "period": 0,
            "tick": 0,
            "ticks_per_period": 0,
            "total_periods": 0,
            "status": "ACTIVE",
            "is_enforce_trading_limits": True
        }

        self._sample_limits_resp = [
            {
                "name": "string",
                "gross": 0,
                "net": 0,
                "gross_limit": 0,
                "net_limit": 0,
                "gross_fine": 0,
                "net_fine": 0
            }
        ]

    def test_case(self):
        method_obj = case.case_response_handle(self._sample_case_resp, '/case')
        class_obj = case.Case(self._sample_case_resp)
        self.assertEqual(method_obj, class_obj)

    def test_case_limits(self):
        method_obj = case.case_response_handle(
            self._sample_limits_resp, '/limits')
        class_obj = case.CaseLimits(self._sample_limits_resp[0])
        self.assertEqual(method_obj, class_obj)


if __name__ == '__main__':
    unittest.main()
