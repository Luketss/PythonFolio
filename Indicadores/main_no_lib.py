import csv

class Csv:

    def __init__(self, file_path):
        self.__file_path = file_path

    def extract_csv_data(self):
        close_price = []
        open_price = []
        with open(self.__file_path) as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if 'NaN' not in row:
                    open_price.append(row[1])
                    close_price.append(row[2])
                    #print(', '.join(row))
        return open_price, close_price

class Candle:
    
    def __init__(self, open_value, close_value):
        self.open_value = open_value
        self.close_value = close_value

class Indicador:

    def __init__(self, numero_periodos, desvio_padrao=0)
        self.numero_periodos = numero_periodos
        self.desvio_padrao = desvio_padrao
    
    def calculate_simple_moving_average(self):
        pass

def main():
    arquivo_csv = Csv('bitstamp.csv')

    open_price, close_price = arquivo_csv.extract_csv_data()

    candles = Candle(open_price, close_price)

if __name__ == '__main__':
    main()
