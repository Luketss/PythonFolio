import csv
import pandas

def read_using_csv():
    temperatures = []
    with open('weather_data.csv') as file:
        data = csv.reader(file)#creates a iterable csv object

        for index, row in enumerate(data):
            if index > 0:
                temperatures.append(row[1])
    print(temperatures)

def main():
    pandas.read_csv()

if __name__ == '__main__':
    main()