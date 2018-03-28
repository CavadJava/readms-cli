from lxml import html
import argparse
import requests


class Manga:
    def __init__(self,url,date,name,chapter,title):
        self.url=url
        self.name=name
        self.chapter=chapter
        self.title=title
        self.date=date

    def __str__(self):
        return self.name+'-Chapter '+self.chapter+' '+self.title


HOST = 'https://readms.net'
NEW_RELEASES_XPATH = '//div[@class="side-nav hidden-xs"]/ul[@class="new-list"]/li[@class="active"]/a'


def get_new_releases():
    page=requests.get(HOST)
    tree=html.fromstring(page.content)
    results = tree.xpath(NEW_RELEASES_XPATH)
    new_releases=[]
    for r in results:
        details=[t.strip() for t in r.itertext()]
        manga=Manga(r.get('href'),details[0],details[1],details[2],details[3])
        new_releases.append(manga)
    return new_releases;


def download_manga(name, chapter):
    pass


def display(mangas):
    print('**********Latest Release**********')
    for manga in mangas:
        print(manga.name.ljust(25)+' Chapter-'+manga.chapter.ljust(3)+(' ('+manga.title+')'))


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='CLI tool to check and download latest manga on readms.net',
                                     formatter_class=argparse.RawTextHelpFormatter)
    help_desc="latest".ljust(15)+"- Get latest manga in readms"+"\ndownload".ljust(15)+" - Download manga; "
    parser.add_argument('command', help=help_desc)
    args=parser.parse_args()

    command=args.command

    if command=="latest":
        new_releases=get_new_releases()
        display(new_releases)
    elif command=="download":
        download_manga()
    else:
        parser.print_help()

