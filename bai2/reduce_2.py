import sys
import string

last_id_com = None
cur_name = "-"

for line in sys.stdin:
    line = line.strip()
    id_com, name_com, year, month = line.split(",")
    if not last_id_com or last_id_com != id_com:
        last_id_com = id_com
        cur_name = name_com
    # nếu không có tên công ty trong file csv thì bỏ qua công ty đó
    elif id_com == last_id_com and cur_name != "-":
        name_com = cur_name
        print("%s,%s,%s,%s" % (id_com, name_com, year, month))
