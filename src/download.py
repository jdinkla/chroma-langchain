import logging
import os
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def download(filename, url):
    if not os.path.exists(filename):
        logging.info(f'file {filename} does not exist, downloading')
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            logging.info('File downloaded successfully!')
        else:
            logging.error('File download failed.')
            exit
