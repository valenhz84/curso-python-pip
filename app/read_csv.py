import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iter = zip(header, row)
            country_dict = {key: value for key, value in iter}
            data.append(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('files/data.csv')
    print(data[0])