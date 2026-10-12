price = input('Enter price without discount: ' )
discount = input('Enter the discount in %: ' )
int(price)
int(discount)
Price_with_discount = price - (price * discount / 100)
Reduction = price - Price_with_discount
print('You ended up paying, Price_with_discount and saved, Reduction')