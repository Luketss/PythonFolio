import csv
import pandas


def main():
    temperatures = []
    with open('weather_data.csv') as file:
        data = csv.reader(file)#creates a iterable csv object

        for index, row in enumerate(data):
            if index > 0:
                temperatures.append(row[1])
    print(temperatures)
if __name__ == '__main__':
    main()