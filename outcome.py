import csv
with open('4hto2min.csv', mode='r') as csv_file:
# with open('1hto30sec.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        correct = 0
        for row in csv_reader:
            if line_count == 0:
                line_count = line_count + 1
            if(row["predicted_trend"] == row["actual_trend"]):
                correct = correct + 1
            line_count = line_count + 1
        total = line_count - 1
        accuracy = ( correct / total ) * 100
        print(f"correct {correct} total {total} accuracy {accuracy}")
        csv_file.close()