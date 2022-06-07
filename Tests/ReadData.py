import json
from pathlib import Path
import os


class ReadData:

    # Opening JSON file
    path = '../Config/data.json'

    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    home_path = Path('../Config')

    # print(home_path)
    f = open(path)

    # returns JSON object as # a dictionary
    data = json.load(f)

    base_url = data['base_url']
    login_title = data['login_title']
    # chrome_driver_path = data['chrome_driver_path']
    # firefox_driver_path = data['firefox_driver_path']

    # Closing file
    f.close()
