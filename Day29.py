#https://www.codewars.com/kata/catalog/train/python

import re
def catalog(s, article):
    """ 
    function to search for arcticle in a catalog and return name, price and quantity of respective article
    """
    result = []
    name_pattern = r"<name>(.*?)</name>"
    price_pattern = r"<prx>(.*?)</prx>"
    quan_pattern = r"<qty>(.*?)</qty>"
    prod_lines = []
    for prod in s.split("\n"):
        if article in prod:
            prod_lines.append(prod)
    if prod_lines == []:
        return "Nothing"
    else:
        for prod in prod_lines:
            name = re.findall(name_pattern, prod)
            price = re.findall(price_pattern, prod)
            quantity = re.findall(quan_pattern, prod)
            line = name[0]+" > "+"prx: $"+price[0]+" qty: "+quantity[0]
            result.append(line)
        result = "\r\n".join(result)
        return result
