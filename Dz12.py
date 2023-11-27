import requests
from bs4 import BeautifulSoup
def get_weather_forecast(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        temperature_elements = soup.select('.DailyContent--temp--_8DL5')
        day_elements = soup.select('.DailyContent--daypartName--3G5Y8')

        for day, temp in zip(day_elements, temperature_elements):
            print(f"{day.get_text(strip=True)}: {temp.get_text(strip=True)}")

    else:
        print(f"Помилка {response.status_code}. Спробуйте пізніше.")

weather_url = "https://weather.com/weather/weekend/l/USCA1115:1:US"
get_weather_forecast(weather_url)
