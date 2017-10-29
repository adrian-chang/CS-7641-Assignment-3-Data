'''main.py

The driver to the entire assignment
'''
import argparse
import clean
import logging
from experiment_1 import Experiment_1

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

EXPERIMENT = {
  'experiment-1': Experiment_1
}

if __name__ == '__main__':
    # parse here
    parser = argparse.ArgumentParser(prog='main.py')
    subparsers = parser.add_subparsers(title='subcommands', dest='command')
    subparsers.add_parser('clean', help='clean the stats from original to final')
    subparsers.add_parser('experiment-1', help='run expierment 1 (clustering)')
    subparsers.add_parser('experiment-2', help='run expierment 2 (dimensonality-reduction)')
    args = parser.parse_args()

    # print something out!
    if not args.command:
        parser.print_help()
    
    command = args.command
    # clean is a one off
    if command == 'clean':
        log.info('Cleaning datasets')  
        clean.create_final_datasets()
    else:
        log.info('Running %s', command)
        EXPERIMENT[command]().run()        
