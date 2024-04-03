import sys

for line in sys.stdin:
    line = line.strip()
    id_com, name_com, date, open_price, close_price = line.split(",")
    date = date.replace(" ","")
    if  date == "2005-10-20" or date == "2005-10-25":
        print("%s,%s,%s,%s,%s" % (id_com, name_com, date, open_price, close_price))
