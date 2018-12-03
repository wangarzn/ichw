#!/usr/bin/env python3

"""currency.py: 描述汇率计算并给出了测试函数.
Module-1 for currency exchange
This module provides a string parsing function to implement a 
simple currency exchange routine using an online currency service. 
The primary function in this module is exchange.

Unit test for module-1
When run as a script, this module invokes a procedure that 
test the various functions in the module a1.

__author__ = "Wang Qichao"
__pkuid__  = "1800011837"
__email__  = "1800011837@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
     """Returns: amount of currency received in the given exchange.
     
    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(currency_from,currency_to,amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    jstr1 = jstr.split(',')
    jstr1_1 = jstr1[1]
    for c in ['"',':',',']:
        jstr1_1 = jstr1_1.replace(c,"") 
    jstr1_2 = jstr1_1.split()
    jstr1_3 = jstr1_2[1]
    return jstr1_3
    

def test_exchange():
    """ 检验exchange函数能否得到正确的结果 ,如果得到正确结果return True否则return False
    """
    assert('2.1589225' == exchange('USD','EUR','2.5'))
           
           
def testAll():
    """test all cases,运行textchange函数，打印 All tests passed
    """
    test_exchange()
    print("All tests passed")
    
    
def main():
    """ 输入3个parameter,并运行测试函数 
    """
    currency_from = input()
    currency_to = input()
    amount_from = input()
    testAll()
    print(exchange(currency_from,currency_to,amount_from))
    
    
if __name__ == '__main__':
    main()
