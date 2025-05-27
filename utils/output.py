import csv
from models.product import Product
from pathlib import Path


def write_csv(products: list[Product], path: Path):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "name",
                "details",
                "image_url",
                "wholesaler",
                "wholesale_price",
                "retail_price",
            ],
        )
        writer.writeheader()
        for p in products:
            writer.writerow(p.__dict__)
