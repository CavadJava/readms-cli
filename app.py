from lxml import html
import argparse
import requests
import sys

HOST = 'https://readms.net'
NEW_RELEASES_XPATH = '//ul[@class="new-list"]/li[@class="active"]/a/'


def get_new_releases():
    page=requests.get(HOST)
    tree=html.fromstring(page.content)
    results=tree.xpath(NEW_RELEASES_XPATH+'text()'+'|'+NEW_RELEASES_XPATH+'attribute::href')
    new_releases={}
    for i in range(0, len(results), 2):
        new_releases[results[i+1].strip()]=results[i].strip()
    return new_releases;


def download_manga(name, chapter):
    pass


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='CLI tool to check and download latest manga on readms.net',
                                     formatter_class=argparse.RawTextHelpFormatter)
    help_desc="latest".ljust(15)+"- Get latest manga in readms"+"\ndownload".ljust(15)+" - Download manga; "
    parser.add_argument('command', help=help_desc)
    args=parser.parse_args()

    command=args.command

    if command=="latest":
        new_releases=get_new_releases()
        for key in new_releases.keys():
            print(key)
    elif command=="download":
        download_manga()
    else:
        parser.print_help()

