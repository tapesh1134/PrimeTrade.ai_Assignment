# Live Cryptocurrency Data Fetcher and Analyzer

This project fetches live cryptocurrency data from the CoinGecko API, analyzes it, and saves the data into an Excel file. The data is updated every 5 minutes, providing real-time cryptocurrency market insights.

## Features

- **Fetch Live Cryptocurrency Data**: Fetches the top 50 cryptocurrencies by market capitalization from the CoinGecko API.
- **Data Analysis**:
  - Identifies the top 5 cryptocurrencies by market capitalization.
  - Calculates the average price of the top 50 cryptocurrencies.
  - Analyzes the highest and lowest 24-hour price changes among the top 50 cryptocurrencies.
- **Excel File Output**: Writes the fetched data to an Excel file, which is updated every 5 minutes.
- **Real-time Updates**: Continuously updates the data every 5 minutes using a background thread.

## Requirements

- Python 3.6 or higher.
- The following Python libraries:
  - `requests`
  - `pandas`
  - `openpyxl`

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/tapesh1134/PrimeTrade.ai_Assignment.git
cd PrimeTrade.ai_Assignment
