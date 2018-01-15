import argparse
import datetime
import os
import urllib

import requests


ICON_TEMPLATE = 'https://files.coinmarketcap.com/static/img/coins/128x128/{0}.png'


DESTINATION_DIRECTORY_BASE_NAME = 'icons'
DEFAULT_LIMIT = 50
DEFAULT_VERBOSE = True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('-l', '--limit', type=int, default=DEFAULT_LIMIT)
    parser.add_argument('-o', '--output-dir', type=str, default=None)
    namespace = parser.parse_args()

    verbose = not namespace.quiet
    limit = namespace.limit
    if namespace.output_dir:
        destination_directory = namespace.output_dir
    else:
        date_part = datetime.datetime.utcnow().strftime('%Y%m%d%H')
        destination_directory = "{0}{1}{2}{3}{1}".format(os.getcwd(), os.sep, DESTINATION_DIRECTORY_BASE_NAME, date_part)
    os.makedirs(destination_directory)

    list_res = requests.get('https://api.coinmarketcap.com/v1/ticker', params={'limit': limit})
    currencies_list = list_res.json()

    downloader = urllib.URLopener()
    for rank, slug in enumerate(currency['id'] for currency in currencies_list):
        if verbose:
            print("{0}/{1}: {2}".format(rank + 1, limit, slug))
        destination_file = destination_directory + "{0}.png".format(slug)
        downloader.retrieve(ICON_TEMPLATE.format(slug), destination_file)
