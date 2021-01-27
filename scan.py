import subprocess,re,socket,json,requests,argparse,sys
from funs import *
banner()
parser = argparse.ArgumentParser()
parser.add_argument('-c',"--connections", help="scan all connections don't forget to set your API key(will take more time ) ",
                    action="store_true")
parser.add_argument('-p',"--programs", help="scan the programs Note: run as administrator",
                    action="store_true")
parser.add_argument('-f',"--fast", help="fast scanner",
                    action="store_true")
parser.add_argument('-ps',"--processing", help="scan processing on your device  don't forget to set your API key",
                    action="store_true")
parser.add_argument('-b',"--banner", help="show tool banner",
                    action="store_true")
args = parser.parse_args()


if (args.connections):
    full()
    ps()
if(args.programs):
    programs()
if(args.fast):
    fast()
if(args.processing):
    ps()

