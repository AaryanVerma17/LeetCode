class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = items[0][1]
        biggest_factor = 0
        for item in items:
            if item[1] < cheapest:
                cheapest = item[1]
            if item[0] > biggest_factor:
                biggest_factor = item[0]
        factor_count = [0] * (biggest_factor + 1)
        for item in items:
            factor = item[0]
            factor_count[factor] += 1
        deals = []
        for item in items:
            factor = item[0]
            price = item[1]
            if price >= cheapest * 2:
                continue
            free_count = -1
            multiple = factor
            while multiple <= biggest_factor:
                free_count += factor_count[multiple]
                multiple += factor
            if free_count > 0:
                deals.append([price, free_count])
        deals.sort()
        total_items = 0
        for deal in deals:
            price = deal[0]
            count = deal[1]
            can_buy = min(count, budget // price)
            total_items += can_buy * 2
            budget -= can_buy * price
        total_items += budget // cheapest
        return total_items