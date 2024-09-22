class order:
    def __init__(self,item_name,price):
        self.item_name=item_name
        self.price=price
    def __gt__():
        if od1.price>od2.price:
            print(od1.item_name,">",od2.item_name)
        else:
            print(od1.item_name,"<",od2.item_name)
    
od1=order("rice",400)
od2=order("ghee",300)
order.__gt__()