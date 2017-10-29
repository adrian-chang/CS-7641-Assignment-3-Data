''' experiment.py

Root of an experiment
'''
import logging
import pandas as pd
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

class Experiment:

    def __init__(self, loc):
        ''' Constructor

         Params:
            loc: string where to store results
        '''
        self._wine_attributes, self._wine_classifications = self._load_dataset()
        self._politican_attributes, self._politication_classifications = self._load_dataset('politican')

        self._output = './results/{}/'.format(loc)
        if not os.path.exists(self._output):
            log.info('Making results directory')
            os.makedirs(self._output)

    def _load_dataset(self, dataset='wine'):
        '''Load a dataset
        '''
        if dataset == 'wine':
            log.info('Loading wine dataset')
            dataset = pd.read_csv('./data/wine-red-white-final.csv')
            class_target = 'red'
            classifications = dataset[class_target]
            attributes = dataset.drop(class_target, axis=1)
        else:
            log.info('Loading politican dataset')
            dataset = pd.read_csv('./data/political-party-final.csv')
            class_target = 'party'
            classifications = dataset[class_target]
            attributes = dataset.drop(class_target, axis=1)

        return classifications.as_matrix(), attributes.as_matrix()

