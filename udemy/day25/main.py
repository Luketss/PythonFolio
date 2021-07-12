import csv
import pandas

# squirtle_color = {
#         'gray' : 0,
#         'cinnamon' : 0,
#         'black': 0,
#     }
class Squirrel:
    def __init__(self, dataframe):
        self.dataframe = dataframe


    def set_all_colors(self):
        squirrel_color = set()

        for value in self.dataframe['Primary Fur Color']:
            squirrel_color.add(value)

        return squirrel_color
    

def main():
    df = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
    sq = Squirrel(df)

    squirrel = dict.fromkeys(sq.set_all_colors(), 0)

    for value in df['Primary Fur Color']:
        if value == 'Gray':
            squirrel['Gray'] += 1
  
        elif value == 'Cinnamon':
            squirrel['Cinnamon'] += 1

        elif value == 'Black':
            squirrel['Black'] += 1
    
    print(squirrel)

if __name__ == '__main__':
    main()
