# stock_analyzer.py

prices = [
    100, 102, 101, 105, 110,
    108, 112, 115, 111, 117,
    120, 119, 123, 125, 121,
    127, 130, 128, 132, 135,
    137, 136, 140, 142, 145,
    143, 147, 150, 149, 152
]


# 1. Maximum profit
def best_profit(prices):

    min_price = prices[0]
    max_profit = 0

    for price in prices:

        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit


# 2. Moving average
def moving_average(prices, window):

    averages = []

    for i in range(len(prices) - window + 1):

        avg = sum(prices[i:i+window]) / window

        averages.append(round(avg, 2))

    return averages


# 3. Find peaks
def find_peaks(prices):

    peaks = []

    for i in range(1, len(prices)-1):

        if prices[i] > prices[i-1] and prices[i] > prices[i+1]:
            peaks.append(i)

    return peaks


# 4. Find valleys
def find_valleys(prices):

    valleys = []

    for i in range(1, len(prices)-1):

        if prices[i] < prices[i-1] and prices[i] < prices[i+1]:
            valleys.append(i)

    return valleys


# 5. Longest uptrend
def longest_uptrend(prices):

    longest = 1
    current = 1

    for i in range(1, len(prices)):

        if prices[i] > prices[i-1]:
            current += 1
        else:
            current = 1

        if current > longest:
            longest = current

    return longest


# 6. Daily percentage changes
def daily_pct_change(prices):

    changes = []

    for i in range(1, len(prices)):

        pct = ((prices[i] - prices[i-1]) / prices[i-1]) * 100

        changes.append(round(pct, 2))

    return changes


# REPORT
print("----- STOCK ANALYSIS REPORT -----")

print("\nPrices:")
print(prices)

print("\nBest Profit:")
print(best_profit(prices))

print("\nMoving Average (window=3):")
print(moving_average(prices, 3))

print("\nPeaks:")
print(find_peaks(prices))

print("\nValleys:")
print(find_valleys(prices))

print("\nLongest Uptrend Length:")
print(longest_uptrend(prices))

print("\nDaily Percentage Changes:")
print(daily_pct_change(prices))