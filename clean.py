'''clean.py

Make the datasets correct for the experiment
'''
import pandas as pd
import logging 
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
logger = logging.getLogger(__name__)

def create_final_datasets():
    ''' Munge the datasets
    '''
    create_wine_dataset()
    create_political_party_dataset()
    
def create_wine_dataset():
    '''Create the final wine dataset
    '''
    logger.info('Cleaning wine datasets')
    wine_red = pd.read_csv('./data/winequality-red-original.csv', sep=';')
    wine_red['red'] = 1
    wine_white = pd.read_csv('./data/winequality-white-original.csv', sep=';')
    wine_white['red'] = 0
    logger.info('Red wine dataframe shape %s', wine_red.shape)
    logger.info('White wine dataframe shape %s', wine_white.shape)
    logger.info('Randomly selecting wines to match red')
    wine_white_final = wine_white.sample(wine_red.shape[0], random_state=0)
    wine_final = wine_red.append(wine_white_final)
    wine_final.columns = ['_'.join(col.split(' ')) for col in wine_final.columns]
    logger.info('Final wine set information \n %s', wine_final.describe(include='all'))
    logger.info('Writing final wine csv to ./data/wine-red-white-final.csv')
    wine_final.to_csv('./data/wine-red-white-final.csv', index=False)

def create_political_party_dataset():
    '''Create the final political party dataset
    '''
    logger.info('Cleaning political party dataset')
    votes = pd.read_csv('./data/house-votes-84.data')
    votes.columns = ['party', 'handicapped', 'water', 'adoption_budget', 'physician', 'el_salavador', 'religious', 
      'anti_satellite', 'nicaraguan', 'mx_missile', 'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free', 'export']
    def numbers_cols(row):
        final_row = []
        for col in votes.columns:
            col_val = row[col]
            if col == 'party':
                if col_val == 'republican':
                    final_row.append(0)
                else:
                    final_row.append(1)
            elif col_val == 'y':
                final_row.append(1)
            elif col_val == 'n':
                final_row.append(-1)
            else:
                final_row.append(0)
        return final_row
    votes = votes.apply(numbers_cols, axis=1)
    votes = votes.reindex_axis(['handicapped', 'water', 'adoption_budget', 'physician', 'el_salavador', 'religious', 
      'anti_satellite', 'nicaraguan', 'mx_missile', 'immigration', 'synfuels', 'education', 'superfund', 'crime', 'duty_free', 'export', 'party'], axis=1)
    logger.info('Final political party information \n %s repub = %s dem = %s', votes.describe(include='all'), 
      (votes['party'] == 0).sum(), (votes['party'] == 1).sum())
    logger.info('Writing political party csv to ./data/political-party-final.csv')
    votes.to_csv('./data/political-party-final.csv', index=False)
