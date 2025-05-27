import importlib
from pathlib import Path
from models.product import Product
from utils.output import write_csv

INPUT_DIR = Path("input_files")
OUTPUT_PATH = Path("output/output.csv")


def import_scraper(wholesaler_name: str):
    try:
        module = importlib.import_module(f"wholesalers.{wholesaler_name}")
        return module.parse
    except ImportError:
        raise ValueError(f"❌ No scraper found for wholesaler '{wholesaler_name}'")


def main():
    print("🔍 Starting product scraping...\n")
    all_products = []

    for folder in INPUT_DIR.iterdir():
        if not folder.is_dir():
            continue

        wholesaler = folder.name.lower()
        print(f"\n📦 Processing wholesaler: {wholesaler.upper()}")

        try:
            parse_func = import_scraper(wholesaler)
        except ValueError as e:
            print(e)
            continue

        html_files = list(folder.glob("*.html"))
        print(f"   - Found {len(html_files)} HTML files")

        for html_file in html_files:
            try:
                print(f"     → Parsing: {html_file.name}")
                products = parse_func(html_file, wholesaler)

                for p in products:
                    p.retail_price = round(p.wholesale_price * 2, 2)

                all_products.extend(products)
            except Exception as e:
                print(f"     ⚠️ Failed to parse {html_file.name}: {e}")

    print("\n💾 Writing output to:", OUTPUT_PATH)
    write_csv(all_products, OUTPUT_PATH)
    print(f"✅ Done. {len(all_products)} products saved.\n")


if __name__ == "__main__":
    main()
