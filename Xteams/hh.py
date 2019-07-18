import requests
from bs4 import BeautifulSoup

class Job():
    def get_html(self):
        ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
        response = requests.get("https://hh.ru", headers=ua)
        self.html = response.text

    def get_div(self):
        html = BeautifulSoup(self.html,"lxml")
        self.div = html.find_all("div", {"class": "vacancies-of-the-day"})

if __name__ == '__main__':
    job = Job()
    job.get_html()
    # print(job.html)
    job.get_div()
    print(dir(job.div))
