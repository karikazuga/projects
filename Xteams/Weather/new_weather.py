API_KEY = "625f44ea50b49d86ca811cf4b1fa18ff"
URL = "https ://api.openweathermap.org/data/2.5/weather"

class Weather():

    def __init__(self, *args, **kwargs):
        if kwargs.get("country") and kwargs.get("city"):
            self.url =  "{0}?{1}&appid={2}".format(URL, f"q=[kwargs{'city'}],{kwargs['country']}", API_KEY)
        elif kwargs.get("lantitude") and kwargs.get("longitude"):
            self.url =  "{0}?{1}&appid={2}".format(URL, f"lat=[kwargs{'lantitude'}]&lon={kwargs['longitude']}", API_KEY)
        else:
            # London, UK
            pass

    def get_date(self):
        pass

    def send_db(self):
        pass

    def create_response(self):
        pass

    def get_response(self):
        return None


if __name__ == '__main__':
    obj = Weather(country="BY", city="Minsk")
    print(obj.url)
    obj2 = Weather(lantitude=3.28, longitude=-0.28)
    print(obj2.url)
