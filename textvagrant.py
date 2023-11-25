class item():
    def __init__(self, product, price, gst, quantity):
        self.product = product
        self.price = price
        self.gst = gst
        self.quantity = quantity
        pass


# intialization of objects
item_array = [item("Leather wallet", 1100, 18, 1), item(
    "Umbrella", 900, 12, 4), item("Cigarette", 200, 28, 3), item("Honey", 100, 0, 2)]
maxgst = 0.0

for itemi in item_array:
    total_price = itemi.price*itemi.quantity
    gst_price = total_price*itemi.gst/100
    # print(itemi.price)
    if itemi.price >= 500:
        # update when price is above 500
        itemi.price = itemi.price-(.05*itemi.price)
    itemi.price = itemi.price+(gst_price/itemi.quantity)
    if maxgst < gst_price:
        # maximum gst to be found
        maxgst = gst_price
        max_gst_product = itemi.product
    # print("Gst for ", itemi.product, "is", itemi.price, "and", gst_price)
    gst_price = 0

total_amt = 0
for itemi in item_array:
    total_amt = (itemi.price*itemi.quantity)+total_amt

# print(maxgst)
print("Product for which we paid the most gst is ",
      max_gst_product, "and the amount was", maxgst)
print("Total amount paid is ", total_amt)
