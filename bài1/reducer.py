import sys
import string

last_id_com = None
name = "-"

for line in sys.stdin:
    line = line.strip()
    id_com, name_com, open_price, close_price = line.split(",")
    if not last_id_com or last_id_com != id_com:
        last_id_com = id_com
        name = name_com
    elif id_com == last_id_com and name != "-":
        name_com = name
        print("%s,%s,%s,%s" % (id_com, name_com, open_price, close_price))
