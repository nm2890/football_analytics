import pandas as pd 


def load_football_data() :
    '''
    load data from https://www.football-data.co.uk/
    '''

    df = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

    print(df.head())

if __name__ == '__main__' :
    load_football_data()