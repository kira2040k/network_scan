import subprocess,re,socket,json,requests,argparse
from funs import *
parser = argparse.ArgumentParser()
parser.add_argument('-f',"--full", help="full scan youe device don't forget to set your API key(will take more time ) ",
                    action="store_true")
args = parser.parse_args()
if (args.full):
    full()
else:
    fast()
