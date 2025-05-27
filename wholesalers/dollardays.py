from bs4 import BeautifulSoup
from pathlib import Path
from models.product import Product
import re


def parse(html_path: Path, wholesaler_name: str) -> list[Product]:
    soup = BeautifulSoup(html_path.read_text(), "html.parser")

    name = soup.find("h1").text.strip()

    details_div = soup.find("div", {"id": "product-dicbar"})
    details = details_div.get_text(separator="\n").strip() if details_div else ""

    image_meta = soup.find("meta", {"property": "og:image"})
    image_url = image_meta["content"] if image_meta else ""

    price_div = soup.find("div", class_="price")

    raw_price = (
        price_div.find("span", class_="caseprice").text.strip() if price_div else ""
    )
    match = re.search(r"\$([\d.]+)", raw_price)
    unit_price = float(match.group(1)) if match else 0.0

    return [
        Product(
            name=name,
            details=details,
            image_url=image_url,
            wholesaler=wholesaler_name,
            wholesale_price=unit_price,
        )
    ]
