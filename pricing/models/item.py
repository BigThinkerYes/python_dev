from typing import Dict
import re    # regular expressions
import requests
import uuid
from bs4 import BeautifulSoup
from models.model import Model


class Item(Model):
    collection = "items"

    def __init__(self, url: str, tag_name: str, query: Dict, _id: str = None):
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        # if or if not statement
        self._id = _id or uuid.uuid4().hex # for mongoDB id

    def __repr__(self):
        return f"<Item {self.url}>"

    def load_price(self) -> float:
        response = requests.get(self.url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        element = soup.find(self.tag_name, self.query)
        string_price = element.text.strip()

        # r is used for regular expressions  \d means a number
        pattern = re.compile(r"(\d+,?\d*\.\d\d)")
        match = pattern.search(string_price)
        found_price = match.group(1)
        without_commas = found_price.replace(",", "")  # remove commas
        self.price = float(without_commas)
        return self.price

    # mongo starts here getting properties from the database
    def json(self) -> Dict:
        return{
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query
        }
