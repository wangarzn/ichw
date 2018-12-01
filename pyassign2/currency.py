#!/usr/bin/env python3

"""currency.py: 描述汇率计算并给出了测试函数.

__author__ = "Wang Qichao"
__pkuid__  = "1800011837"
__email__  = "1800011837@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
    """Module for currency exchange.This module provides several string parsing functions to implement a 
    simple currency exchange routine using an online currency service. 
    The primary function in this module is exchange.
    """
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
    """ 检验exchange函数能否得到正确的结果 
    """
    assert('2.1589225' == exchange('USD','EUR','2.5'))
           
           
def testAll():
    """模块2：检验函数,test all cases
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
