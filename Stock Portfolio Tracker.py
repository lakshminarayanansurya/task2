# Hardcoded dictionary with stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350
}

# Dictionary to store user-entered stock quantities
user_stocks = {}

# User input loop
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            user_stocks[stock] = user_stocks.get(stock, 0) + quantity
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Stock not found in our price list.")

# Calculate total investment
total_investment = 0
print("\nInvestment Summary:")
for stock, qty in user_stocks.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} x ${stock_prices[stock]} = ${value}")
    total_investment += value

print(f"\nTotal Investment Value: ${total_investment}")

# Optionally save to file
save = input("Do you want to save this summary? (yes/no): ").lower()
if save == "yes":
    file_type = input("Choose file format (txt/csv): ").lower()
    filename = "investment_summary." + file_type
    with open(filename, "w") as f:
        if file_type == "txt":
            for stock, qty in user_stocks.items():
                f.write(f"{stock}: {qty} x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
            f.write(f"\nTotal Investment Value: ${total_investment}")
        elif file_type == "csv":
            f.write("Stock,Quantity,Price,Total\n")
            for stock, qty in user_stocks.items():
                f.write(f"{stock},{qty},{stock_prices[stock]},{stock_prices[stock] * qty}\n")
            f.write(f",,,{total_investment}")
    print(f"Saved summary to {filename}")
