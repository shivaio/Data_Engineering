import argparse

def parse_url_to_download(args):
    url = args

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help=" URL of NPTEL Course")
    args = parser.parse_args()
    parse_url_to_download(args)


