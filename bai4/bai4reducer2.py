import sys
import string

id_ = None
buyPrice = 0
highest = 0
cur_name = "-"
dividend = 0
for line in sys.stdin:
    line = line.strip()
    id_com, name_com, date, value_open, highestPrice = line.split(",")
    if id_ == None or id_ != id_com:
        id_ = id_com
        buyPrice = value_open
        cur_name = name_com
    elif id_com == id_ and cur_name != " -":
        highest = highestPrice
    if float(highest) - float(buyPrice) > 0:
        dividend = float(highest) - float(buyPrice)
        print("%s	%s" % (id_com, name_com, dividend))
