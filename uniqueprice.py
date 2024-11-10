from collections import defaultdict


def unique_first_price(prices):
    price_count = defaultdict(int)

    # Step 1: Count occurrences of each price
    for price in prices:
        price_count[price] = price_count.get(price, 0) + 1  # defaultdict initializes with 0, so we just add 1

    # Step 2: Find the first unique price in the original list
    for i, price in enumerate(prices):
        if price_count[price] == 1:
            return i  # Return the index of the first unique price

    # If no unique price exists, return -1
    return -1


# Call the function with a list of prices
print(unique_first_price([1, 1, 2, 5]))  # This should return 3, as '5' is the first unique price
