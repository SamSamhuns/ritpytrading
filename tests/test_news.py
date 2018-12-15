import unittest
from ritpytrading import news


class TestNewsMethods(unittest.TestCase):
    def setUp(self):
        self._sample_news_resp = [
            {
                "news_id": 0,
                "period": 0,
                "tick": 0,
                "ticker": "string",
                "headline": "string",
                "body": "string"
            }
        ]

    def test_news_dict(self):
        method_dict = news.news_response_handle(self._sample_news_resp)
        class_dict = {self._sample_news_resp[0]["news_id"]: news.News(
            self._sample_news_resp[0])}
        self.assertEqual(method_dict, class_dict)


if __name__ == "__main__":
    unittest.main()
