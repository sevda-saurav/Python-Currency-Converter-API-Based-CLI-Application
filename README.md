# 💱 Currency Converter (Python)

A simple command-line Currency Converter built with Python that fetches live exchange rates from the FreeCurrencyAPI.

This project demonstrates:

* API integration
* Python modular project structure
* Working with external libraries (`requests`)
* Clean CLI-based user interaction

---

## 🚀 Features

* Convert currency between different countries
* Fetch live exchange rates from API
* Simple command-line interface
* Lightweight Python project

---

## 📂 Project Structure

```
currency-converter/
│
├── main.py              # Program entry point
├── converter.py         # Currency conversion logic
├── config.py            # API configuration (ignored in git)
├── requirements.txt     # Project dependencies
├── .gitignore
├── .env.example
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/currency-converter.git
```

Move into the project folder:

```
cd currency-converter
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## 🔑 API Setup

Create a file named `config.py` and add:

```
BASE_URL = "https://api.freecurrencyapi.com/v1/latest"
API_KEY = "your_api_key_here"
```

You can get a free API key from:

https://freecurrencyapi.com

---

## ▶️ Run the Application

```
python main.py
```

Example:

```
Currency Converter
------------------

Enter Amount: 100
From currency (USD, INR, EUR): USD
To currency (USD, INR, EUR): INR

Converted Amount: 8300.00 INR
```

---

## 🛠 Technologies Used

* Python
* Requests library
* REST API

---

## 👨‍💻 Author

Built as a Python learning project.
