from bs4 import BeautifulSoup
from pathlib import Path
from models.product import Product
import re


def parse(html_path: Path, wholesaler_name: str) -> list[Product]:
    soup = BeautifulSoup(html_path.read_text(), "html.parser")

    # Product name
    name_tag = soup.find("meta", property="og:title")
    name = name_tag["content"].strip() if name_tag else "Unknown Product"

    # Product description (details)
    desc_tag = soup.find("meta", property="og:description")
    details = desc_tag["content"].strip() if desc_tag else ""

    # Product image
    image_tag = soup.find("meta", property="og:image")
    image_url = image_tag["content"].strip() if image_tag else ""

    # Price (from schema.org structured data)
    price_tag = soup.find("meta", property="product:price:amount")
    price = float(price_tag["content"]) if price_tag else 0.0

    return [
        Product(
            name=name,
            details=details,
            image_url=image_url,
            wholesaler=wholesaler_name,
            wholesale_price=price,
        )
    ]
