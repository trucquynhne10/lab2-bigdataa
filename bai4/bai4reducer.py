import sys
import string

last_id_com = None
cur_name = "-"

for line in sys.stdin:
    line = line.strip()
    id_com, name_com, date, open_price, close_price = line.split(",")
    if not last_id_com or last_id_com != id_com:
        last_id_com = id_com
        cur_name = name_com
    # neu khong co ten cong ty trong file csv thi bo qua cong ty do
    elif id_com == last_id_com and cur_name != "-":
        name_com = cur_name
        print("%s,%s,%s,%s,%s" %
              (id_com, name_com, date, open_price, close_price))
