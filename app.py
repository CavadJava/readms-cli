import argparse


def get_latest_mangas():
    pass

def download_manga(name, chapter):
    pass


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description='CLI tool to check and download latest manga on readms.net',
                                     formatter_class=argparse.RawTextHelpFormatter)
    help_desc="list".ljust(15)+"- List latest manga in readms"+"\ndownload".ljust(15)+" - Download manga; "
    parser.add_argument('command', help=help_desc)
    args=parser.parse_args()

    command=args.command

    if command=="list":
        get_latest_mangas()
    elif command=="download":
        download_manga()

