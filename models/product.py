from dataclasses import dataclass


@dataclass
class Product:
    name: str
    details: str
    image_url: str
    wholesaler: str
    wholesale_price: float
    retail_price: float = 0.0
