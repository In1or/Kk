from MounteBankController import MounteBankController
import unittest


class CurrencyConversionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__MountBank_controller = MounteBankController()
        self.__exchange_rate = self.__MountBank_controller.get_currency_rate()
        
        self.__WRONG_CURRENCY_MSG = "Ошибка: Неизвестная валюта."
        
        self.__rates = {
            'RUB': {'RUB': 1, 'USD': 1/float(self.__exchange_rate['USD']), 'EUR': 1/float(self.__exchange_rate['EUR'])},
            'USD': {'RUB': float(self.__exchange_rate['USD']), 'USD': 1, 'EUR': float(self.__exchange_rate['USD'])/float(self.__exchange_rate['EUR'])},
            'EUR': {'RUB': float(self.__exchange_rate['EUR']), 'USD': float(self.__exchange_rate['EUR'])/float(self.__exchange_rate['USD']), 'EUR': 1}
        }    
    
    def test_convert_rubles_to_dollars(self):
        self.__conversion_result = self.Convert("RUB", "USD", 1000)
        
        self.assertEqual(13.42, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from rubles to dollars ")
    
    def test_convert_rubles_to_euros(self):
        self.__conversion_result = self.Convert("RUB", "EUR", 1000)
        
        self.assertEqual(11.07, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from rubles to euros ")


    def test_convert_dollars_to_rubles(self):
        self.__conversion_result = self.Convert("USD", "RUB", 1000)

        self.assertEqual(74500.00, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from dollars to rubles ")

    def test_convert_dollars_to_euros(self):
        self.__conversion_result = self.Convert("USD", "EUR", 1000)
        
        self.assertEqual(825.03, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from dollars to euros ")


    def test_convert_euros_to_rubles(self):
        self.__conversion_result = self.Convert("EUR", "RUB", 1000)

        self.assertEqual(90300.00, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from euros to rubles ")

    def test_convert_euros_to_dollars(self):
        self.__conversion_result = self.Convert("EUR", "USD", 1000)

        self.assertEqual(1212.08, float("{:.2f}".format(self.__conversion_result)), msg="Error when converting currency from euros to dollars")    

    def Convert(self, first, second, amount):
        if first not in self.__rates or second not in self.__rates:
            return self.__WRONG_CURRENCY_MSG

        converted_amount = amount * self.__rates[first][second]
        return converted_amount
