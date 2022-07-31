import yfinance as yf
import datetime

# get info about S&P 500 from yahoo finance
def get_sp_500_info():
    SP500 = yf.Ticker("^GSPC")
    print("Getting S&P 500 info...")
    print(SP500.info)

# get the S&P 500 data from yahoo finance for the last month
def get_sp_500_data():
    data = yf.download("^GSPC", start=datetime.datetime.now()-datetime.timedelta(days=30), end=datetime.datetime.now())
    return data

# store the data in a csv file
def store_sp_500_data():
    data = get_sp_500_data()
    data.to_csv("sp_500_data.csv")
    return data

if __name__ == "__main__":
    store_sp_500_data()
