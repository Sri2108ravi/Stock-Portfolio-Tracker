# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Get number of stocks
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (AAPL/TSLA/GOOGL/AMZN/MSFT): ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        price = stock_prices[stock_name]
        investment = price * quantity

        total_investment += investment

        print("Stock Price:", price)
        print("Investment Value:", investment)

    else:
        print("Invalid stock name!")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value:", total_investment)

# Save result in text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("Total Investment Value: " + str(total_investment))

print("\nResult saved successfully in portfolio.txt")