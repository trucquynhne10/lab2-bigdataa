import sys

set_id = set() # tạo set để lưu trữ id công ty
for line in sys.stdin:
    line = line.strip()
    id_com, name_com, value_open, value_close = line.split(",")
    # nếu công ty chưa được duyệt và có open < close thì in ra công ty đó
    if (id_com not in set_id and float(value_open) < float(value_close)):
        set_id.add(id_com)
        print("%s   %s" % (id_com, name_com))
