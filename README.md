# Price Dedector
A Python-based price tracking tool that monitors product prices across multiple e-commerce platforms and sends an email notification when the price drops below a defined threshold.

---
## 🚀 Features
- Tracks prices from multiple online stores:
  - **Hepsiburada**
  - **Amazon Turkey**
  - **N11**
  - **ÇiçekSepeti**
  - **Trendyol**
- Sends email notification when the price falls below your minimum value
- Checks prices every **5 minutes**
- Uses a Pandas DataFrame for product management

---
## 📦 Installation
### 1. Clone the repository
```bash
git clone https://github.com/osmanvarisli/price_dedector.git
cd price_dedector
```

### 2. Install required packages
```bash
pip install requests beautifulsoup4 lxml pandas
```

---
## ⚙️ Configuration
### **Set up your email information**
Edit the following lines inside `price_dedector.py`:
```python
email_adres = 'your_email'
sifre = 'your_password'
```
> **Note:** You may need to use an app password depending on your email provider.

### **Add products to track**
Products are stored in a Pandas DataFrame:
```python
df.loc[len(df.index)] = ["monitor", "https://example-url.com", 5000, "amazon"]
```
Fields:
- **urun_adi** → Product name
- **URL** → Product page URL
- **min_fiyat** → Price threshold
- **site** → One of the supported site names

---
## ▶️ Running the Script
```bash
python price_dedector.py
```
The script will:
- Fetch each product page
- Read the current price
- Compare price vs threshold
- Send an email if needed
- Repeat the process every **300 seconds**

---
## ⚠️ Important Notes
- Site HTML structures may change and break the scraper.
- Excessive scraping may lead to temporary IP blocking.
- Price extraction XPath selectors may require maintenance.

---
## 🛠️ Technologies Used
- Python 3
- Requests
- BeautifulSoup4
- LXML
- Pandas
- SMTPLib

---
## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---
## 📄 License
This project is released under the **MIT License**.
