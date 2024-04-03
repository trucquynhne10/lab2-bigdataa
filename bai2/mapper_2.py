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
            year = "0"
            month = "0"
            line = line.strip()
            words = line.split(",")
            if (len(words) == 3 and words[2] != "NASDAQ"): #nếu không phải sàn NASDAQ thì bỏ qua
                continue
            if (len(words) == 3):
                id_com = words[0].lower()
                name_com = words[1]
            else:
                id_com = filename.split(".us.txt")[0]
                date = words[0].split("-")
                year = date[0]
                month = date[1]
            print('%s, %s, %s, %s' %
                  (id_com, name_com, year, month))
