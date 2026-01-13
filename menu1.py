def add_iteem(cart,item, price):
  cart.append({item: price})
def remove_item(cart, item):
  for product in cart:
    if item in product:
      cart.remove(product)
      return
  raise Exception("Item not found")
def unique_items(cart):
  return set(list(item.keys())[0] for item in cart)
def bill_summary(cart):
  total_items = 0
  total_cost = 0
  for i in cart:
    cost = list(i.values()[0])
    total_cost = total_cost + cost
    total_items = total_items + 1
  return (total_items, total_cost)
