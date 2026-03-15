import pandas as pd
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class FullEcommerceScraper:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless") # Jalankan tanpa jendela
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # User-Agent yang lebih modern untuk menghindari blokir
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.results = []

    def get_last_page(self, url):
        """Mencari tahu berapa jumlah total halaman yang ada"""
        try:
            self.driver.get(url)
            time.sleep(3)
            # Mencari elemen pagination text (misal: "1/50")
            pagination_text = self.driver.find_element(By.CLASS_NAME, "list-tool-pagination-text").text
            last_page = int(pagination_text.split('/')[-1])
            return last_page
        except:
            return 1

    def scrape_all_pages(self, base_url):
        last_page = self.get_last_page(base_url)
        print(f"[*] Engine Ready. Total pages detected: {last_page}")

        for page in range(1, last_page + 1):
            print(f"[>] Processing Page {page} of {last_page}...")
            current_url = f"{base_url}&page={page}"
            self.driver.get(current_url)
            
            # Tunggu sampai container produk muncul
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "item-container"))
                )
            except:
                print(f"[!] Page {page} took too long to load. Skipping...")
                continue

            # Scroll ke bawah perlahan agar elemen malas (lazy load) muncul
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
            time.sleep(random.uniform(2, 4)) # Delay acak agar menyerupai manusia

            items = self.driver.find_elements(By.CLASS_NAME, "item-container")
            
            for item in items:
                try:
                    # Mengambil Title
                    title_element = item.find_element(By.CLASS_NAME, "item-title")
                    name = title_element.text
                    link = title_element.get_attribute("href")
                    
                    # Mengambil Brand (Failsafe jika logo tidak ada)
                    try:
                        brand = item.find_element(By.CLASS_NAME, "item-brand").find_element(By.TAG_NAME, "img").get_attribute("title")
                    except:
                        brand = "Generic / Unknown"

                    # Mengambil Harga & Rating
                    try:
                        price = item.find_element(By.CLASS_NAME, "price-current").text.replace('\n', '').replace('$', '').strip()
                    except:
                        price = "0"
                        
                    try:
                        rating = item.find_element(By.CLASS_NAME, "item-rating").get_attribute("title")
                    except:
                        rating = "No Rating"

                    self.results.append({
                        'Page': page,
                        'Product_Name': name,
                        'Brand': brand,
                        'Price_Raw': price,
                        'Rating': rating,
                        'URL': link
                    })
                except:
                    continue 

            print(f"[+] Successfully captured {len(self.results)} total items so far.")
            
            # Anti-Ban Protection: Setiap 5 halaman, istirahat lebih lama
            if page % 5 == 0:
                print("[!] Anti-ban break: Cooling down for 10 seconds...")
                time.sleep(10)

    def export_data(self, filename="Newegg_Full_Catalog.xlsx"):
        df = pd.DataFrame(self.results)
        # Data Preprocessing sederhana sebelum simpan
        df['Price_Clean'] = df['Price_Raw'].str.extract(r'(\d+[\.,]\d+)').replace('[\.,]', '', regex=True)
        
        df.to_excel(filename, index=False)
        print(f"\n[!!!] FINISHED. Total Records: {len(df)}")
        print(f"[!] Data saved to {filename}")
        self.driver.quit()

if __name__ == "__main__":
    # URL target (Tanpa parameter page di akhir)
    BASE_URL = "https://www.newegg.com/p/pl?d=gaming+laptop&N=100006740"
    
    scraper = FullEcommerceScraper()
    scraper.scrape_all_pages(BASE_URL)
    scraper.export_data()