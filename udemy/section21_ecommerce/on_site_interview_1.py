# You have been given a list of historical stock prices for a single day for Amazon stock.
# The index of the list represents a timestamp, so the element at index 0 is the initial price
# of the stock, the element at index 1 is the next recorded price of the stock for that day,
# Your task is to write a function that will return the maximum profit possible from the
# purchase and sale of a single share of Amazon stock on that day. Keep in mind to try to
# make this as efficient as possible
# prices = [12, 11, 15, 3, 10]

def profit_greedy(stock: list):
    n = len(stock)

    result = 0

    for i in range(n):
        for j in range(i, n):
            if stock[i] < stock[j]:
                result = max(result, stock[j] - stock[i])
    
    return result

def profit(stock: list):
    min_profit_price = stock[0]
    result = 0

    for price in stock:
        min_profit_price = min(min_profit_price, price)
        comparison_profit = price - min_profit_price

        result = max(result, comparison_profit)
    
    return result

def profit_edge_cases(stock: list):
    if len(stock) < 2:
        raise Exception("Need at least 2 stock prices")

    min_stock_price = stock[0]
    result = stock[1] - stock[0]

    for price in stock[1:]:
        comparison_profit = price - min_stock_price

        result = max(result, comparison_profit)

        min_stock_price = min(min_stock_price, price)
    
    return result

print(profit_greedy([12, 11, 15, 3, 10]))
print(profit([12, 11, 15, 3, 10]))