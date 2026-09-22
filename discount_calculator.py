def calculate_final_price(sum_of_all_prices):
    if sum_of_all_prices > 100:
        discount = 0.10
        discount_amount = sum_of_all_prices * discount
        the_final_price = sum_of_all_prices - discount_amount
        print(f"Your final price is {the_final_price:.2f}.")
    else:
        print(f"Your final price is: {sum_of_all_prices:.2f}.")

calculate_final_price(120)
calculate_final_price(80)
