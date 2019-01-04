#!/usr/bin/env python
# coding: utf-8   # necessary for python not to complain
                  # about ";¥;" in the strings 
"A base class, Currency, for inheriting any country's currency."
import sys, os
try:
    sys.path.insert(0, os.path.join(
        os.path.split(__file__)[0], '..'))
except NameError:
    sys.path.insert(0, "..") 
import lab_06_Comprehensions.hw06_1 as thousands

EPSILON = .0001  # close to zero 

class Tender:
    """A class to give nice names to the parts of the tender.
    """
    def __init__(self, tender_tuple):
        self.value, self.name = tender_tuple

class Currency(float):
    """Base class for all currencies.

    To add a currency, subclass and provide four attributes:
    symbol, exchange_rate (amount per dollar), a sequence of
    Tender objects sorted so that the largest Tender amount
    is first, and decimal_digits, which are the number of digits
    to the right of the decimal to display when printing the
    currency.
    """

    def __add__(self, other):
        """Exchanges the right-hand operand to the currency type
        of the left-hand operand and adds them, returning the type
        of the left-hand operand.
        """

        if type(self) == type(other):
            return self.__class__(float(self) + float(other))
        return self.__class__(float(self) + float(
            other.ExchangeFor(self.__class__)))

    def __eq__(self, other):
        if abs(self - other.ExchangeFor(self.__class__)) <= EPSILON:
            return True
        return False

    def ExchangeFor(self, OtherCurrencyClass):
        """Exchanges the self for the equivalent value in the
        OtherCurrencyClass.
        """
        dollars = self/self.exchange_rate
        other =  getattr(OtherCurrencyClass,
                         "exchange_rate") * dollars
        return OtherCurrencyClass(other)

    def MakeCurrency(self):
        """Returns a list of the bills and coins needed
        to make the amount."""
        if self < 0:
            return []
        return_parts = []
        amount = self
        for tender in self.tender:
            tender_name_to_use = tender.name
            how_many = 0
            how_many, amount = divmod(amount, tender.value)
            # For the smallest tender, if the amount left is
            # within EPSILON of that tender, one more is added.
            if (tender == self.tender[-1] and 
                tender.value - amount < EPSILON):
                how_many += 1
            if how_many:
                if how_many > 1:
                    if tender_name_to_use.endswith('y'):
                        tender_name_to_use = (
                            tender_name_to_use[:-1] + 'ies')
                    else:
                        tender_name_to_use = (
                            tender_name_to_use + 's')
                return_parts += ["%5d %s" % (how_many,
                                             tender_name_to_use)]
        return return_parts

    def __repr__(self):
        "self.__name__ does't work for finding the class name."
        
        return "%s('%f')" % (self.__class__.__name__, self)

    def __str__(self):
        """Returns a value that can be represented in the tender
        of the currency."""
        
        minimum_value = self.tender[-1].value
        value = int(self/minimum_value) * minimum_value
        
        thousands_str = thousands.SeparateThousands(
            value, self.decimal_digits)
        if thousands_str[0] == '-':
            return '-' + self.symbol + thousands_str[1:]
        return self.symbol + thousands_str

class Dollar(Currency):
    exchange_rate = 1.0
    symbol = '$'
    tender = [Tender(t) for t in [
        (value, symbol + str(value) + " Bill")
        for value in (1000, 100, 50, 20, 10, 5, 1)]
        + [(.50, 'Half Dollar'), (.25, 'Quarter'), (.10, 'Dime'),
           (.05, 'Nickel'), (.01, 'Penny')]]
    decimal_digits = 2

class Yen(Currency):
    exchange_rate = 81.1076  # 5/27/11 www.x-rates.com
    symbol = unichr(165)
    tender = [Tender(t) for t in [
        (value, symbol + thousands.SeparateThousands(value) 
		 + " Bill") for value in (10000, 5000, 2000, 1000)] 
        + [(value, symbol + thousands.SeparateThousands(value) 
			+ " Coin") for value in (500, 100, 50, 10, 
									 5, 1)]]
    decimal_digits = 0

class EgyptianPound(Currency):
    exchange_rate = 5.96810   # 5/27/11   www.oanda.com
    symbol = unichr(163)
    tender = [Tender(t) for t in [
        (200, symbol + '200 Bill'), (100, symbol + '100 Bill'),
    (50, symbol + '50 Bill'), (20, symbol + '20 Bill'),
    (10, symbol + '10 Bill'), (5, symbol + '5 Bill'),
    (1, symbol + '1 Bill'), (1, '1 Pound Coin'), 
    (0.5, '50 Piastres Coin'), (0.5, '50 Piastres Bill'), 
    (0.25, '25 Piastres Coin'), (0.25, '25 Piastres Bill'),
    (0.10, '10 Piastres Coin'), (0.05, '5 Piastres Coin')]]
    decimal_digits = 2

def TestValue(value):
    print 'value', value, ':'
    egyptian_pound = EgyptianPound(value)
    dollar = egyptian_pound.ExchangeFor(Dollar)
    yen = dollar.ExchangeFor(Yen)
    print (unicode(egyptian_pound), ":\n",
           unicode('\n'.join(egyptian_pound.MakeCurrency())))
    print dollar, ':\n', '\n'.join(dollar.MakeCurrency())
    print unicode(yen), ":\n", 	
    print unicode('\n'.join(yen.MakeCurrency()))
    another_pound = yen.ExchangeFor(EgyptianPound)
    try:
        assert another_pound == egyptian_pound
    except:
        print ("broke:", unicode(another_pound),
               unicode(egyptian_pound))
        print float(another_pound), float(egyptian_pound)
        raise
    # testing __repr__
    assert egyptian_pound == eval(repr(egyptian_pound))
    assert dollar == eval(repr(dollar))
    assert yen == eval(repr(yen))

    # testing +
    thrice = egyptian_pound + dollar + yen
    assert thrice ==  (egyptian_pound + egyptian_pound
                       + egyptian_pound)

def RandomTest(tries=2):
    import random
    for test in range(tries):
        value = random.random() * (10 **random.randrange(7))
        TestValue(value)

def main():
    for value in (1000, 100.01, 32.232):
        TestValue(value)
    RandomTest(2)

if __name__ == '__main__':
    main()
"""
$ hw14.py
value 1000 :
£1,000.00 :
    5 £200 Bills
$167.55 :
    1 $100 Bill
[lots deleted!]
$
"""
