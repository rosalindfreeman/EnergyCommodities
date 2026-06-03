# Energy Commodities Demo

This is a Python project that downloads historical energy commodity prices from Yahoo Finance and shows:

- price history plots
- 30-day rolling average plots
- a correlation matrix for oil and gas prices

The current demo uses:

- Brent Crude Oil: `BZ=F`
- Natural Gas: `NG=F`

The demo currently starts at `2023-01-01` and uses the current date on your machine as the end date, so each run attempts to fetch the latest available market data.

## Project Overview

The broader goal is to help understand energy market behaviour by:

- identifying price trends over time
- comparing commodities such as oil and gas
- measuring correlation
- preparing for future forecasting and volatility analysis
- visualizing insights that support decision-making

## Current Implementation

The code in this repository currently supports:

- downloading historical price data from Yahoo Finance using `yfinance`
- storing closing prices in a pandas DataFrame
- plotting price history over time
- calculating and plotting rolling averages
- computing a correlation matrix between commodities

In other words, this repository currently covers the data download, charting, and basic comparison parts of the wider project idea.

## How The Code Is Organized

- `main.py` runs the demo workflow
- `energy_price_engine.py` contains the main `EnergyPriceEngine` class
- `requirements.txt` lists the Python packages needed by the project

## What You Need

- Python installed
- VS Code installed
- Internet access when you run the script, because price data is downloaded from Yahoo Finance


Then run these commands.


### 3. Run the project

```powershell
python main.py
```

## What You Should See

When the script runs successfully, it should:

1. Download historical daily prices for oil and gas.
2. Print the first few rows of the dataset in the terminal.
3. Print a correlation matrix.
4. Open a chart showing the price history.
5. Open a second chart showing the 30-day rolling average.

