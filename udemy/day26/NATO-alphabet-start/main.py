import pandas as pd

class Nato:
    def __init__(self, path):
        self.path_to_file = path 

    def get_nato_df(self):
        data_frame = pd.read_csv(self.path_to_file, index_col=0)
        nato_dict = {index:row.code for(index, row) in data_frame.iterrows()}

        return nato_dict

    def phonetical(self, nato_dict):
        inputed_code = input('Type your message: ').upper()

        coded_message = [nato_dict[letter] for letter in inputed_code]
        print(coded_message)


if __name__ == '__main__':
    nato = Nato('np.csv')
    nato_dict = nato.get_nato_df()
    nato.phonetical(nato_dict)