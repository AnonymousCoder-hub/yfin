# Indian Stocks API

A simple FastAPI application to retrieve basic stock data for Indian stocks using the `yfinance` library, deployable on Vercel.

## Deployment on Vercel

Follow these steps to deploy this API on Vercel:

1.  **Link your Git Repository:** Connect your Git repository (e.g., GitHub, GitLab, Bitbucket) containing the API code to Vercel.
2.  **Configure Project:** When setting up the project on Vercel, ensure the following:
    *   **Root Directory:** If your code is not in the root of the repository, specify the correct root directory.
    *   **Build Command:** Set the build command to: `uvicorn main:app --host 0.0.0.0 --port $PORT`
    *   **Output Directory:** This can usually be left blank or set to `.`.
    *   **Development Command:** This can usually be left blank.
3.  **Deploy:** Click the "Deploy" button. Vercel will build and deploy your application.

Once deployed, Vercel will provide you with a unique URL for your API.

## API Usage

The API now has three endpoints to get stock data:

1.  `GET /stock/{ticker}`: Get historical data for a given duration.
2.  `GET /stock/{ticker}/date/{date}`: Get data for a specific date.
3.  `GET /stock/{ticker}/range/{start_date}/{end_date}`: Get data for a date range.

-   **`ticker`**: The stock ticker symbol (e.g., `TCS.NS` for Tata Consultancy Services). Indian stock tickers on yfinance usually end with `.NS`.
-   **`duration` (Optional for endpoint 1)**: A query parameter for the first endpoint to specify the duration for historical data. Accepted values include: `1d`, `5d`, `1mo`, `3mo`, `6mo`, `1y`, `2y`, `5y`, `10y`, `ytd`, `max`. The default duration is `1d`.
-   **`date` (For endpoint 2)**: The specific date in `YYYY-MM-DD` format.
-   **`start_date` and `end_date` (For endpoint 3)**: The start and end dates of the range in `YYYY-MM-DD` format.

### Examples

1.  **Get latest data for Reliance Industries (RELIANCE.NS) using duration:**
