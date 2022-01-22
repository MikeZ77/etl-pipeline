"""Running the Xetra ETL application"""
import logging
import logging.config

import yaml

import os 

def main():
    """
    Entry point to run the xetra ETL job
    """
    # Parse the YAML file
    config_path = os.path.dirname(os.path.realpath(__file__)) + '/configs/xetra1_config.yml'
    config = yaml.safe_load(open(config_path))

    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info('This is a test.')

if __name__ == '__main__':
    main()