import sys

set_id = set() # tạo set để lưu trữ id công ty
for line in sys.stdin:
    line = line.strip()
    id_com, name_com, year, month = line.split(",")
    # nếu công ty chưa được duyệt và có open < close thì in ra công ty đó
    if (id_com not in set_id and (year == '2005' and month in ['01', '02'])):
        set_id.add(id_com)
        print("%s   %s" % (id_com, name_com))
