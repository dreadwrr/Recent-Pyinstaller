import argparse
import sys
from dirwalker import main_entry as dirwalker_main
from ffsearch import main_entry as ffsearch_main
from rntchanges import main as rntchanges_main
from recentchangessearch import main as recentchanges_main
from recentchangessearchparser import parse_recent_args


def build_subparser(script):
    parser = argparse.ArgumentParser(
        description="Run recentchanges from cmdline 6 required 5 optional"
    )
    subparsers = parser.add_subparsers(dest="args", required=True)

    arg_e = subparsers.add_parser(script, help="Run main search with hybrid analysis")
    parse_recent_args(arg_e)  # use the parser for recentchangessearch

    r_args = parser.parse_args()

    if r_args.args == script:
        recent_args = [
            r_args.argone, r_args.argtwo, r_args.USR, r_args.PWD, r_args.argf, r_args.method,
            r_args.iqt, r_args.db_output, r_args.POST_OP, r_args.scan_idx, r_args.showDiff, r_args.argwsl,
            r_args.dspPATH
        ]
        return recent_args
    else:
        print("Parser fault for recentchangessearch. exit")
        sys.exit(1)


def dispatch_internal(argv):

    if len(argv) < 2:
        return False
    if len(argv) > 4:
        script = argv[1].lower()
        args = argv[2:]

        DISPATCH_MAP = {
            "dirwalker.py": {
                "scan": 7,
                "build": 6,
                "downloads": 9,
            },
            "recentchangessearch.py": recentchanges_main,
            "ffsearch.py": ffsearch_main
        }

        entry = DISPATCH_MAP.get(script)

        if isinstance(entry, dict):  # dirwalker

            cmd = args[0]
            if cmd not in entry:
                print(
                    f"Invalid parameter for dirwalker; expected one of: "
                    f"{'/'.join(entry.keys())}, got {cmd}"
                )

                sys.exit(1)
            min_args = entry[cmd]
            if len(args) < min_args:
                print(f"Not enough args for '{cmd}', expected {min_args}, got {len(args)}")
                sys.exit(1)

            sys.exit(dirwalker_main(args))

        elif entry:  # recentchangessearch, ffsearch
            if script == "recentchangessearch.py":
                recent_args = build_subparser(script)
                result = entry(*recent_args)
                sys.exit(result)

            elif script == "ffsearch.py":
                sys.exit(entry(args))

    # direct to recentchangessearch.py

    method = argv[1].lower()  # for `recentchanges` with no args so it doesnt open main window
    if method == "inv":

        # recent_args = build_subparser(method)
        # result = recentchanges_main(*recent_args) # command line use from .bat
        result = rntchanges_main(argv[1:])
        sys.exit(result)

    # pass all arguments to rntchanges.py
    sys.exit(rntchanges_main(argv))  # any arguments provided to rntchanges.py
