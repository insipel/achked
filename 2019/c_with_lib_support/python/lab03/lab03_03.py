#!/usr/bin/env python

def CalculateTotalCost(sales_price, sales_tax_rate = 8.25):
    print "Sales Price %.2f, Rate: %.2f" % (sales_price, sales_tax_rate)
    return ( sales_price + (sales_price * sales_tax_rate / 100))

def main():

    while True:
        try:
            price = float(raw_input("Enter your sales price: "))
            break
        except ValueError:
            print "Pls try again"

    while True:
        rate = raw_input("A particular sales tax rate? ")
        if not rate:
            sales_tax_rate = 8.25
            break
        else:
            try:
                sales_tax_rate = float(rate)
                break
            except ValueError:
                print "Pls try again"

    print "Total cost %.2f" % (CalculateTotalCost(price, sales_tax_rate))

main()

