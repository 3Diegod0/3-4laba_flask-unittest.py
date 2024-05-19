import unittest
from flask2 import app
from flask2 import get_exchange_rate


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_exchange_rate_valid(self):
        base_currency = 'USD'
        target_currency = 'EUR'
        result = get_exchange_rate(base_currency, target_currency)
        self.assertIsInstance(result, float)

    def test_get_exchange_rate_invalid_base(self):
        base_currency = 'INVALID'
        target_currency = 'EUR'
        result = get_exchange_rate(base_currency, target_currency)
        self.assertEqual(result, "Ошибка: Неверно указана валюта. Пожалуйста, проверьте правильность ввода.")

    def test_get_exchange_rate_invalid_target(self):
        base_currency = 'USD'
        target_currency = 'INVALID'
        result = get_exchange_rate(base_currency, target_currency)
        self.assertEqual(result, "Ошибка: Неверно указана валюта. Пожалуйста, проверьте правильность ввода.")


if __name__ == '__main__':
    unittest.main()