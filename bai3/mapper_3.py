import os
stocks_dir = 'Stocks'
filenames = os.listdir(stocks_dir)

for filename in filenames:
    file_path = os.path.join(stocks_dir, filename)
    with open(file_path, 'r') as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue
            id_com = ""
            name_com = "-"
            open_price = "0"
            close_price = "0"
            date = "2000-01-01"
            line = line.strip()
            items = line.split(",")
            # neu khong phai san NYSE thi bo qua
            if (len(items) == 3 and items[2] != "NYSE"):
                continue
            if (len(items) == 3):
                id_com = items[0].lower()
                name_com = items[1]
            else:
                id_com = filename.split(".us.txt")[0]
                date = items[0]
                open_price = items[1]
                close_price = items[4]
            print('%s, %s, %s, %s, %s' %
                  (id_com, name_com, date, open_price, close_price))
