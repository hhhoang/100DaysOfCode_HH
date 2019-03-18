# https://www.codewars.com/kata/ease-the-stockbroker/train/python
""" Clients place orders to a stockbroker as strings. The order can be simple or multiple.
Type of a simple order: Quote/white-space/Quantity/white-space/Price/white-space/Status
where Quote is formed of non-whitespace character, 
Quantity is an int, 
Price a double (with mandatory decimal point "." ), 
Status is represented by the letter B (buy) or the letter S (sell).

Example:
"GOOG 300 542.0 B"
A multiple order is the concatenation of simple orders with a comma between each.
Example:
"ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"
or (C)
"ZNGA 1300 2.66 B,CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"

To ease the stockbroker your task is to produce a string of type
"Buy: b Sell: s" where b and s are 'double' formatted with no decimal (rounded to integers), 
b representing the total price of bought stocks and s the total price of sold stocks.

Example:
"Buy: 294990 Sell: 0"
Unfortunately sometimes clients make mistakes. When you find mistakes in orders, you must pinpoint these badly formed orders and produce a string of type:
"Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"
where nb is the number of badly formed simple orders, b representing the total price of bought stocks with correct simple order and s the total price of sold stocks with correct simple order.

Examples:
"Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"
"Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;" """

def balance_statement(lst):
    print(lst)
    buy = 0
    sell = 0
    badOrders = []
    orders = lst.split(", ")
    if len(orders) == 0:
        results = "Buy: " + str(int(buy)) + " Sell: " + str(int(sell))
    else:
        for order in orders:
            order = order.split(" ")
            if len(order) == 4:
              # ToDO: if order[1] == 250.0 int(order[1]) will give ValueError
                if int(order[1]) and float(order[2]) and "B" in order[3]:
                    buy += int(order[1])*float(order[2])
                elif int(order[1]) and float(order[2]) and "S" in order[3]:
                    sell += int(order[1])*float(order[2])
                else:
                    badOrders.append(order)
            
    badOrderString = ""
    for i in badOrders:
        badOrderString += str(i) + " ;"
    if len(badOrders) == 0:
        results = "Buy: " + str(int(round(buy))) + " Sell: " + str(int(round(sell)))
    else:
        results = "Buy: " + str(round(buy)) + " Sell: " + str(round(sell)) + "; Badly formed " + str(len(badOrders)) + badOrderString
    return results
