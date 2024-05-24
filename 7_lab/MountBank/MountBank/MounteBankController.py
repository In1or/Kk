import requests


class MounteBankController:
    def __init__(self):
        self.__base_url = "http://localhost:4545"
        self.__currency_rate_url = "/currency-rate"
        
    def get_currency_rate(self):
        try:
            response = requests.get(self.__base_url + self.__currency_rate_url)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"Other error occurred: {err}")
        else:
            return (response.json())
            
