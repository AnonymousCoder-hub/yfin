from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import pandas as pd
from datetime import datetime

app = FastAPI()

# Add CORS middleware - THIS MAKES IT ACCESSIBLE FROM ANYWHERE
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows ALL domains
    allow_credentials=True,
    allow_methods=["*"],  # Allows ALL HTTP methods
    allow_headers=["*"],  # Allows ALL headers
)

@app.get("/stock/{ticker}")
def get_stock_data_by_duration(ticker: str, duration: str = "1d"):
    """
    Fetches stock data for a given ticker and duration.

    Args:
        ticker: The stock ticker symbol (e.g., "TCS.NS" for Tata Consultancy Services).
        duration: The duration for historical data (e.g., "1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"). Defaults to "1d".

    Returns:
        A JSON object containing the stock data (Open, High, Low, Close, Volume) for the specified duration.
        Returns an error message if the ticker is invalid or no data is found.
    """
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period=duration)

        if hist.empty:
            raise HTTPException(status_code=404, detail=f"No data found for ticker: {ticker} with duration: {duration}")

        # Convert the historical data to a list of dictionaries for JSON output
        stock_data = hist.reset_index().to_dict('records')

        return stock_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stock/{ticker}/date/{date}")
def get_stock_data_by_date(ticker: str, date: str):
    """
    Fetches stock data for a given ticker and specific date.

    Args:
        ticker: The stock ticker symbol (e.g., "TCS.NS" for Tata Consultancy Services).
        date: The specific date in YYYY-MM-DD format.

    Returns:
        A JSON object containing the stock data for the specified date.
        Returns an error message if the ticker or date is invalid or no data is found for the date.
    """
    try:
        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')

        stock = yf.Ticker(ticker)
        # yfinance 'history' end date is exclusive, so we need to add one day to include the specified date
        start_date = date
        end_date = (datetime.strptime(date, '%Y-%m-%d') + pd.Timedelta(days=1)).strftime('%Y-%m-%d')

        hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
             raise HTTPException(status_code=404, detail=f"No data found for ticker: {ticker} on date: {date}")

        stock_data = hist.reset_index().to_dict('records')

        return stock_data[0] # Return only the data for the specific date

    except ValueError:
         raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stock/{ticker}/range/{start_date}/{end_date}")
def get_stock_data_by_range(ticker: str, start_date: str, end_date: str):
    """
    Fetches stock data for a given ticker within a date range.

    Args:
        ticker: The stock ticker symbol (e.g., "TCS.NS" for Tata Consultancy Services).
        start_date: The start date of the range in YYYY-MM-DD format.
        end_date: The end date of the range in YYYY-MM-DD format.

    Returns:
        A JSON object containing the stock data for the specified date range.
        Returns an error message if the ticker or dates are invalid or no data is found for the range.
    """
    try:
        # Validate date formats
        datetime.strptime(start_date, '%Y-%m-%d')
        datetime.strptime(end_date, '%Y-%m-%d')

        stock = yf.Ticker(ticker)
        # yfinance 'history' end date is exclusive, so we need to add one day to include the end_date
        end_date_inclusive = (datetime.strptime(end_date, '%Y-%m-%d') + pd.Timedelta(days=1)).strftime('%Y-%m-%d')

        hist = stock.history(start=start_date, end=end_date_inclusive)

        if hist.empty:
             raise HTTPException(status_code=404, detail=f"No data found for ticker: {ticker} within date range: {start_date} to {end_date}")

        stock_data = hist.reset_index().to_dict('records')

        return stock_data

    except ValueError:
         raise HTTPException(status_code=400, detail="Invalid date format. Please use YYYY-MM-DD for both start and end dates.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
