# 🇮🇳 yfin — Indian Stocks API

yfin is a lightweight FastAPI-based REST API for retrieving Indian stock market data using the yfinance library.

It is designed for frontend apps, learning projects, stock simulators, and dashboards.

## 🚀 Live Deployment

Base URL:
https://yfin.vercel.app

## 🚀 One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/AnonymousCoder-hub/yfin)

## ✨ Features

- Indian stock market data
- FastAPI backend
- Historical and range-based queries
- No authentication required
- Vercel deployable
- Open-source

## 📦 API Endpoints


- GET /stock/{ticker}?duration=1d

- GET /stock/{ticker}/date/{date}

- GET /stock/{ticker}/range/{start_date}/{end_date}


## 🏷 Parameters

ticker: Stock symbol (example: TCS.NS)

duration (optional):
1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max

date format:
YYYY-MM-DD

## 🧪 Examples

- /stock/RELIANCE.NS?duration=1d
- /stock/TCS.NS/date/2024-01-10
- /stock/INFY.NS/range/2024-01-01/2024-01-31

## 🛠 Tech Stack

- Python
- FastAPI
- yfinance
- Uvicorn
- Vercel

## ⚠️ Disclaimer

For educational use only. Not financial advice.

## 🤝 Contributing

Fork the repo, create a branch, commit, and open a PR.

## ⭐ Support

If this helps you, star the repository.
