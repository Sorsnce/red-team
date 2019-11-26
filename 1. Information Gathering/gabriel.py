import argparse
import json

print("""\
   _____         _            _        _ 
  / ____|       | |          (_)      | |
 | |  __   __ _ | |__   _ __  _   ___ | |
 | | |_ | / _` || '_ \ | '__|| | / _ \| |
 | |__| || (_| || |_) || |   | ||  __/| |
  \_____| \__,_||_.__/ |_|   |_| \___||_|
""")

def main_ui(args):
    # set up command completion
    try:
        import readline
    except ImportError:
        print("Module 'readline' not available.")
    else:
        import rlcompleter
        if 'libedit' in readline.__doc__:
            readline.parse_and_bind('bind ^I rl_complete')
        else:
            readline.parse_and_bind('tab: complete')
        # for possible future use to format command completion output
        #readline.set_completion_display_matches_hook(display_hook)
    # process toggle flag arguments
    flags = {
        'check': args.check if not args.stealth else False,
        'analytics': args.analytics if not args.stealth else False,
        'marketplace': args.marketplace if not args.stealth else False,
    }
    # launch the interactive session
    

description = "Gabriel is a new tool in development"
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-w', help='load/create a workspace', metavar='workspace', dest='workspace', action='store')
parser.add_argument('-r', help='load commands from a resource file', metavar='filename', dest='script_file', action='store')
parser.add_argument('--no-version', help='disable version check', dest='check', default=True, action='store_false')
parser.add_argument('--no-analytics', help='disable analytics reporting', dest='analytics', default=True, action='store_false')
parser.add_argument('--no-marketplace', help='disable remote module management', dest='marketplace', default=True, action='store_false')
parser.add_argument('--stealth', help='disable all passive requests (--no-*)', dest='stealth', default=False, action='store_true')
parser.add_argument('--version', help='displays the current version', action='version', version='0.1')
args = parser.parse_args()
main_ui(args)
