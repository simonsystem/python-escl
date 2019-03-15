import sys
import os
from argparse import ArgumentParser
from getpass import getpass
from .api import scan

parser = ArgumentParser(description='eSCL Scanning Utility')
parser.add_argument('url', help='url to the web interface of your scanner')
parser.add_argument('--size', '-s', metavar='TYPE', choices=['a4', 'letter'], default='a4', help='size of scanned region')
parser.add_argument('--compression', '-z', metavar='NUM', type=int, default=35, help='compression factor for image creating')
parser.add_argument('--brightness', '-b', metavar='NUM', type=int, default=1000, help='brightness of document')
parser.add_argument('--contrast', '-c', metavar='NUM', type=int, default=1000, help='contrast of document')
parser.add_argument('--color-mode', '-m', metavar='MODE', choices=['Grayscale8', 'RGB24'], default='RGB24', help='color mode of document')
parser.add_argument('--document-format-ext', '-e', metavar='MIME', choices=['application/pdf', 'image/jpeg'], default='application/pdf', help='type of the created file')
parser.add_argument('--verify', metavar='PATH', nargs='?', const=True, help='verify ssl connection by CA bundle file')
parser.add_argument('--cert', metavar='PATH', nargs='?', const=True, help='establish ssl connection with this cert file')
parser.add_argument('--username', '-u', metavar='NAME', default='admin', help='basic auth username')
parser.add_argument('--password', '-p', metavar='SECRET', nargs='?', const=True, help='basic auth password')
parser.add_argument('--output', '-o', metavar='PATH', default='-', help='write output to file')

def pipe(buffer, *args, **kwargs):
    r = scan(*args, **kwargs)
    for chunk in r.iter_content(2048):
        buffer.write(chunk)

def main():
    args = vars(parser.parse_args())
    output = args['output']
    del args['output']
    if args['password'] is True:
        args['password'] = getpass('Password: ')
    if output == '-':
        sys.stderr.write("Scanning from %s to stdout...%s" % (args['url'], os.linesep))
        pipe(sys.stdout, **args)
    else:
        with open(output, 'wb') as file:
            sys.stderr.write("Scanning from %s to %s...%s" % (args['url'], file.name, os.linesep))
            pipe(file, **args)
