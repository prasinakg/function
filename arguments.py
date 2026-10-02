def total_calc(bill_amount,tip_price):
    total= bill_amount*(1 + 0.01*tip_price)
    total= round(total,2)
    print(f"Please pay ${total}")

total_calc(150,20)