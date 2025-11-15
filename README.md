# Price Tracker Script

This project is a **Python-based price tracking script** that checks product prices on multiple e-commerce websites and sends an email notification when the price drops below a specified threshold.

## 📌 Features
- Tracks prices from:
  - **Hepsiburada**
  - **Amazon Turkey**
  - **N11**
  - **ÇiçekSepeti**
  - **Trendyol**
- Sends email notifications when the price falls below your defined limit.
- Uses `requests`, `BeautifulSoup`, and `lxml` for web scraping.
- Includes a loop that checks prices every **5 minutes (300 seconds)**.

---

## 📁 Project Structure
```
├── price_tracker.py   # Main Python script
└── README.md          # Documentation
```

---

## 🚀 Installation
### 1. Clone the repository
```bash
git clone https://github.com/kullanici_adi/price-tracker.git
cd price-tracker
```

### 2. Install required packages
```bash
pip install requests beautifulsoup4 lxml pandas
```

---

## ⚙️ Configuration
Before running the script, edit the following parts inside `price_tracker.py`:

### **1. Email information**
Replace these lines with your real email and password:
```python
email_adres = 'your_email'
sifre = 'your_password'
```

### **2. Products to track**
The script uses a pandas DataFrame:
```python
df = pd.DataFrame(columns=['urun_adi','URL','min_fiyat','site'])
```
You can add new products like:
```python
df.loc[len(df.index)] = ["monitor", "https://example.com", 5000, "amazon"]
```

---

## ▶️ Running the Script
Start tracking prices with:
```bash
python price_tracker.py
```
The script will:
- Scrape each website
- Compare prices
- Send an email when a price drops
- Repeat every **5 minutes**

---

## ⚠️ Important Notes
- Some websites may block scraping, so use custom headers as configured.
- Websites may change their HTML structure, breaking the scraper.
- Make sure less-secure apps or app-password is enabled for your email provider.
- Overusing scraping may violate a site's terms — use responsibly.

---

## 🛠️ Technologies Used
- **Python 3**
- **Requests** – HTTP client
- **BeautifulSoup & lxml** – HTML parsing
- **pandas** – Data management
- **smtplib** – Email sending

---

## 📬 Contributing
Contributions and improvements are welcome! Feel free to open a pull request.

---

## 📄 License
This project is licensed under the MIT License.
