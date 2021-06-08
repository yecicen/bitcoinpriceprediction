import csv

def getData():
    data = []
    with open('data/messari.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["timestamp"]} price: {row["price"]} volume {row["volume"]}.')
            special_data = ["messari",row["timestamp"],row["price"],row["volume"] ]
            data.append(special_data)
            line_count += 1
    with open('data/nomics.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["timestamp"]} price: {row["price"]} volume {row["volume"]}.')
            special_data = ["nomics",row["timestamp"],row["price"],row["volume"] ]
            data.append(special_data)
            line_count += 1
    with open('data/coinmarketcap.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(f'\t{row["timestamp"]} price: {row["price"]} volume {row["volume"]}.')
            special_data = ["coinmarketcap",row["timestamp"],row["price"],row["volume"] ]
            data.append(special_data)
            line_count += 1
    return data