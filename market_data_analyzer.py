products=["Monitor", "smartphone",'watch']
price=[12000,10000,800 ]
inventory=[]
for i in range(len(products)):
    item={
        "name":products[i],
        "price": price[i]
    }
    inventory.append(item)
    
print(inventory)
    
