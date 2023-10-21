import json
import requests
import bs4

print("Hello! This program is created to parse car listings on kolesa.kz")
min_price = input("minimum price of cars: ")
max_price = input("maximum price of cars: ")

# Creating the URL address with input data and sending a request
url = f"https://kolesa.kz/cars/?price[from]={min_price}&price[to]={max_price}"
response = requests.get(url)

# Getting HTML content from the URL
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Finding car listings on the page
car_listings = soup.find_all("div", class_="a-elem")

cars = []

# Extracting car data
for listing in car_listings:
    title = listing.find("a", class_="a-el-info-title").text.strip()
    price = listing.find("span", class_="price").text.strip()
    location = listing.find("span", class_="list-region").text.strip()
    
    car = {
        "title": title,
        "price": price,
        "location": location
    }
    
    cars.append(car)

# Creating a JSON file in the working directory
with open("kolesa_cars.json", "w", encoding="utf-8") as out:
    json.dump(cars, out, ensure_ascii=False, indent=4)
