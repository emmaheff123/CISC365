def stock_dnc(prices, left = 0, right = None):
    if right is None:
        right = len(prices) - 1

    if right-left + 1 <= 5:
        min_price = prices[left]
        min_day = left
        max_profit = 0
        buy_day = sell_day = left

        for i in range (left, right + 1):
            if prices[i] < min_price:
                min_price = prices[i]
                min_day = i
            if prices [i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                buy_day, sell_day = min_day, i
        return buy_day, sell_day, max_profit
    
    mid = (left + right) // 2

    left_buy, left_sell, left_profit = stock_dnc(prices, left, mid)
    right_buy, right_sell, right_profit = stock_dnc(prices, mid + 1, right)

    min_left = min(prices[left:mid + 1])
    min_left_day = prices.index(min_left, left, mid + 1)

    max_right = max (prices[mid + 1: right + 1])
    max_right_day = prices.index(max_right, mid + 1, right + 1)

    cross_profit = max_right - min_left

    if left_profit >= right_profit and left_profit >= cross_profit:
        return left_buy, left_sell, left_profit
    elif right_profit >= left_profit and right_profit >= cross_profit:
        return right_buy, right_sell, right_profit
    else:
        return min_left_day, max_right_day, cross_profit

