from bs4 import BeautifulSoup
import json
import requests

# Makes an HTTP request to grab the price of a card
def grab_price(name, card_no):
    price = "0"
    if name.strip() != "" and card_no.strip() != "":
        # Make an HTTP request
        payload = {'q': "" + name + " " + card_no}
        req = requests.get("https://mavin.io/search", params=payload).text

        # Extract the data
        soup = BeautifulSoup(req, "html.parser")
        data = soup.find("script", type="application/ld+json").string
        response = json.loads(data)
    
        price = response["offers"]["price"]
    return price