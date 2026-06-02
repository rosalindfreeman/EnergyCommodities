import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


class EnergyPriceEngine:
    def __init__(self, tickers):
        """
        tickers: dict like {"Oil": "BZ=F", "Gas": "NG=F"}
        """
        self.tickers = tickers
        self.data = None

    def fetch_data(self, start_date, end_date, interval="1d"):
        """
        Pull historical data from Yahoo Finance.
        """
        all_data = {}

        for name, ticker in self.tickers.items():
            df = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                interval=interval,
                progress=False,
            )
            if "Close" not in df.columns:
                raise ValueError(f"Close price not found for ticker {ticker}.")

            close_data = df["Close"]

            # Newer yfinance versions may return a one-column DataFrame here.
            # Convert it to a Series so pandas can combine the results cleanly.
            if isinstance(close_data, pd.DataFrame):
                if close_data.shape[1] != 1:
                    raise ValueError(
                        f"Expected one Close column for ticker {ticker}, "
                        f"got {close_data.shape[1]}."
                    )
                close_data = close_data.iloc[:, 0]

            all_data[name] = close_data.rename(name)

        self.data = pd.DataFrame(all_data).dropna()
        return self.data

    def plot_prices(self):
        if self.data is None:
            raise ValueError("No data loaded. Run fetch_data first.")

        plt.figure(figsize=(12, 6))
        for col in self.data.columns:
            plt.plot(self.data.index, self.data[col], label=col)

        plt.title("Energy Prices Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def rolling_analysis(self, window=30):
        if self.data is None:
            raise ValueError("No data loaded. Run fetch_data first.")

        rolling = self.data.rolling(window=window).mean()

        plt.figure(figsize=(12, 6))
        for col in rolling.columns:
            plt.plot(rolling.index, rolling[col], label=f"{col} MA({window})")

        plt.title(f"Rolling Average ({window} days)")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.tight_layout()
        plt.show()

    def correlation(self):
        if self.data is None:
            raise ValueError("No data loaded. Run fetch_data first.")

        corr = self.data.corr()
        print("\nCorrelation Matrix:\n")
        print(corr)
        return corr
