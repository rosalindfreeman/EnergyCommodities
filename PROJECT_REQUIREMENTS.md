# Project Requirements

The current repository supports:

- downloading historical price data from Yahoo Finance
- plotting price history
- calculating rolling averages
- computing a correlation matrix

The items below describe the additional work needed to complete the broader project vision.

## Goal

Analysing historical energy commodity prices and producing useful insights through statistics, visualization, and forecasting.

The finished project should help a user:

- understand historical price trends in energy markets
- identify patterns, seasonality, and volatility
- compare relationships between commodities such as oil and gas
- generate short-term price forecasts
- interact with the tool without editing source code

## Functional Requirements

### 1. Volatility Analysis

The system should calculate and present volatility metrics for each selected commodity.

Suggested outputs:

- volatility time-series plot
- summary table with mean volatility, max volatility, and recent volatility

### 2. Seasonality and Pattern Detection

The system should help users identify recurring patterns in the time series.

Minimum expected behaviour:

- support monthly and yearly aggregation views
- show whether certain months or periods tend to have stronger or weaker prices
- provide summary statistics by month, quarter, or day-of-week where relevant

Suggested outputs:

- monthly average price chart
- box plots by month
- seasonal decomposition or trend/seasonality summary where feasible

### 3. Forecasting

The system should forecast future prices for selected commodities using statistical or machine learning methods.

Minimum expected behaviour:

- support at least one forecasting model such as ARIMA
- optionally support a simpler regression-based baseline for comparison
- generate a forecast for a configurable number of future days, with 30 days as the default

Suggested outputs:

- forecast DataFrame with dates and predicted prices
- forecast chart
- optional confidence intervals if supported by the model

### 4. Flexible Time Range Selection

The system should allow the user to choose the analysis period without modifying the code.

Minimum expected behaviour:

- accept a user-provided start date
- accept a user-provided end date
- validate that the start date is earlier than the end date
- use the current date by default when no end date is supplied

### 5. Dynamic Ticker Input

The system should allow different commodity tickers to be selected at runtime.

Minimum expected behaviour:

- allow users to pass one or more ticker symbols when running the project
- allow a friendly display name for each ticker where possible
- handle invalid or unsupported tickers gracefully

Example supported use cases:

- compare Brent and Natural Gas
- compare WTI and Brent
- analyze only a single commodity

### 6. CLI-Style Interaction

The system should provide a simple command-line interface so a user can run analyses without editing Python files.

Minimum expected behaviour:

- allow command-line arguments for start date, end date, tickers, and forecast horizon
- allow users to choose which analyses to run
- show helpful usage text for invalid commands or missing arguments

Suggested command examples:

```powershell
python main.py --tickers BZ=F NG=F --start 2023-01-01 --end 2026-04-25
python main.py --tickers BZ=F NG=F --forecast-days 30
python main.py --tickers CL=F --volatility --seasonality
```

### 7. Improved Visual Reporting

The system should present the analysis in a clearer and more complete way than the current two basic line charts.

Minimum expected behaviour:

- generate separate charts for prices, rolling averages, volatility, and forecasts
- use readable labels, titles, and legends
- ensure charts work for both one commodity and multiple commodities

Optional enhancements:

- seaborn styling
- correlation heatmap
- export charts to image files

### 8. Error Handling and Validation

The system should fail clearly and helpfully when user input or downloaded data is invalid.

Minimum expected behaviour:

- detect empty downloads
- detect invalid ticker symbols
- detect invalid date formats
- report errors with user-friendly messages instead of raw stack traces where possible

### 9. Modular Project Structure

The original brief mentioned modular functions and clean architecture. To satisfy that, the project should be organized into clear responsibilities.

Suggested module split:

- data loading
- analysis functions
- forecasting functions
- plotting functions
- CLI entry point

This does not require a large framework, but it should avoid placing all logic in one script.

## Non-Functional Requirements

The completed project should also aim for the following quality goals:

- readable code with clear function and class responsibilities
- reproducible setup using `requirements.txt`
- documentation that explains setup, usage, and available analyses
- compatibility with local execution in VS Code on Windows

## Suggested Delivery Phases

To keep the project manageable, a sensible implementation order would be:

### Phase 1: Usability

- add CLI arguments
- add flexible date selection
- add dynamic ticker input
- improve validation and error messages

### Phase 2: Analysis

- add volatility calculations
- add correlation heatmap
- add seasonality views

### Phase 3: Forecasting

- add ARIMA-based forecasting
- add 30-day forecast output and chart
- add forecast configuration options


This project can be considered complete against the original brief when a user can:

- choose one or more energy commodity tickers at runtime
- choose the analysis date range at runtime
- view historical price charts and rolling averages
- run volatility and seasonality analysis
- compute correlation between commodities
- forecast future prices for a chosen horizon
- run the workflow from the command line using documented commands
- understand setup and usage from the repository documentation alone
