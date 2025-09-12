#Matthew Tyler
#09/12/25
#Total Purchase
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    print('Hello welcome to Kwik Trip')
    # Write a program that asks for each item, 
    bread = 5
    milk = 4
    eggs = 6
    Purchase = input("Would you like to purchase 'eggs', 'milk', or 'bread'?")
    if Purchase == 'bread':
        subtotal = bread
    elif Purchase == 'eggs':
            subtotal = eggs
    elif Purchase == 'milk':
            subtotal = milk
    else:
        print('we don't have that here, have a good day')
        return

    
    total = subtotal * 1.07    
    # then displays the subtotal of the sale, 
    print('The subtotal today is', subtotal)
    # the amount of sales tax, and the total.
    print('And the total after tax is', total)
    # Assume the sales tax is 7 percent.

calculate_total_purchase()
