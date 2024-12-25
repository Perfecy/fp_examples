order = {
    "user_balance": 1000,
    "order_amount": 600,  
    "product_stock": 10,
    "order_qty": 1,
    "region": "far"  
}

class OrderProcessor:
    def __init__(self, order):
        self.order = order

    def run(self):
        self.check_balance()
        self.check_stock()
        self.calc_shipping()
        self.update_total()
        self.pay_order()
        return self.order

    def check_balance(self):
        if self.order["user_balance"] < self.order["order_amount"]:
            raise ValueError("Not enough money")

    def check_stock(self):
        if self.order["product_stock"] < self.order["order_qty"]:
            raise ValueError("Not enough stock")

    def calc_shipping(self):
        if self.order["region"] == "far":
            self.order["shipping_cost"] = 500
        else:
            self.order["shipping_cost"] = 0

    def update_total(self):
        self.order["order_amount"] += self.order["shipping_cost"]

    def pay_order(self):
        self.order["user_balance"] -= self.order["order_amount"]

processor = OrderProcessor(order)
updated_order = processor.run()
print(updated_order)



def check_balance(ctx):
    if ctx["user_balance"] < ctx["order_amount"]:
        raise ValueError("Not enough money")
    return ctx

def check_stock(ctx):
    if ctx["product_stock"] < ctx["order_qty"]:
        raise ValueError("Not enough stock")
    return ctx

def calc_shipping(ctx):
    # Допустим, если "region" == "far", доплата 500
    shipping_cost = 0
    if ctx["region"] == "far":
        shipping_cost = 500
    ctx["shipping_cost"] = shipping_cost
    return ctx

def update_total(ctx):
    ctx["order_amount"] += ctx["shipping_cost"]
    return ctx

def pay_order(ctx):
    # Эмулируем списание средств
    ctx["user_balance"] -= ctx["order_amount"]
    return ctx

def process_order(order_ctx):
    steps = [check_balance, check_stock, calc_shipping, update_total, pay_order]
    for step in steps:
        order_ctx = step(order_ctx)
    return order_ctx



updated_order = process_order(order)
print(updated_order)
