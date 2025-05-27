# Product Scraper

## Running Product Scraper

1. Change to the project directory

```bash
cd product_scraper
```

2. Create Python Virtual Environment

```bash
python3 -m venv .venv
```

3. Activate Python Virtual Environment

```bash
source .venv/bin/activate
```

4. Install app

```bash
pip install -r requirements.txt
```

5. Save Product webpages to `input_files/`

6. Run app to create CSV file with product info

```bash
python run.py
```

7. Find the CSV file at `output/output.csv`

## Adding a new wholesaler to Product Scraper

1. Download a product page from the new wholesaler

2. Attach the following to a ChatGPT chat

   - `run.py`
   - `wholesalers/dollarday.py`
   - HTML file product page from new wholesaler

3. Add the following prompt to the ChatGPT chat:

   ```
   Please write a new web scraper for the files like the attached HTML file. It should be similar to the attached python file which is an existing web scraper for dollardays
   ```

4. Copy and paste the new code written by ChatGPT into a new python file that should be saved in `wholesalers/`

5. Create a folder for the HTML files from the new wholesaler in `input_files/`. It needs to match the name of the python file you just created

6. You can now save product pages from the new wholesaler into its folder in `input_files/` and run the app
