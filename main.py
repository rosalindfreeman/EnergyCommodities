from datetime import date

from energy_price_engine import EnergyPriceEngine


def main():
    tickers = {
        "Oil": "BZ=F",
        "Gas": "NG=F",
    }
    start_date = "2023-01-01"
    end_date = date.today().isoformat()

    engine = EnergyPriceEngine(tickers)

    print(f"Downloading historical prices for Oil and Gas from {start_date} to {end_date}...")
    data = engine.fetch_data(start_date, end_date)

    print("\nLoaded data preview:\n")
    print(data.head())

    engine.correlation()
    engine.plot_prices()
    engine.rolling_analysis(window=30)


if __name__ == "__main__":
    main()
