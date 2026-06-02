# Energy Commodities Demo

This is a small Python project that downloads historical energy commodity prices from Yahoo Finance and shows:

- price history plots
- 30-day rolling average plots
- a correlation matrix for oil and gas prices

The current demo uses:

- Brent Crude Oil: `BZ=F`
- Natural Gas: `NG=F`

The demo currently starts at `2023-01-01` and uses the current date on your machine as the end date, so each run attempts to fetch the latest available market data.

## Project Overview

This project is a starter Python application for exploring historical energy commodity prices, especially Brent crude oil and natural gas.

The broader goal is to help understand energy market behaviour by:

- identifying price trends over time
- comparing commodities such as oil and gas
- measuring correlation
- preparing for future forecasting and volatility analysis
- visualizing insights that support decision-making

The original project description also mentioned a wider toolset and future ambition, including:

- data collection from financial APIs
- time series visualization
- volatility and correlation analysis
- price forecasting using machine learning or statistical models such as ARIMA
- flexible time range selection
- dynamic ticker input
- modular functions
- optional CLI-style interaction

## Current Implementation

The code in this repository currently supports:

- downloading historical price data from Yahoo Finance using `yfinance`
- storing closing prices in a pandas DataFrame
- plotting price history over time
- calculating and plotting rolling averages
- computing a correlation matrix between commodities

In other words, this repository currently covers the data download, charting, and basic comparison parts of the wider project idea.

## Planned Future Features

The original project description includes features that are not implemented yet in the current code:

- volatility analysis
- seasonality analysis
- forecasting with ARIMA or regression models
- dynamic user input for different ticker symbols
- CLI-style interaction
- future price forecasting such as the next 30 days

## How The Code Is Organized

- `main.py` runs the demo workflow
- `energy_price_engine.py` contains the main `EnergyPriceEngine` class
- `requirements.txt` lists the Python packages needed by the project

## Project Files

- [main.py](C:\Users\Martin\Workspaces\Projects\Rosa\EnergyCommodities\main.py)
- [energy_price_engine.py](C:\Users\Martin\Workspaces\Projects\Rosa\EnergyCommodities\energy_price_engine.py)
- [requirements.txt](C:\Users\Martin\Workspaces\Projects\Rosa\EnergyCommodities\requirements.txt)

## What You Need

- Python installed
- VS Code installed
- Internet access when you run the script, because price data is downloaded from Yahoo Finance

## How To Run It

Open a terminal in:

`C:\Users\Martin\Workspaces\Projects\Rosa\EnergyCommodities`

Then run these commands.

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install the required packages

```powershell
pip install -r requirements.txt
```

### 4. Run the project

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

Close the first chart window to allow the next chart window to appear.

## Running In VS Code

If you open this folder in VS Code:

1. Open the integrated terminal.
2. Run the commands above.
3. Select the Python interpreter from `.venv` if VS Code asks.
4. Run `main.py`.

## Notes

- `seaborn` and `statsmodels` are included because they were listed in the original project description, but this starter version does not use them yet.
- The code currently focuses on downloading, plotting, rolling averages, and correlation analysis.
- Forecasting and volatility analysis can be added later as the next step.
