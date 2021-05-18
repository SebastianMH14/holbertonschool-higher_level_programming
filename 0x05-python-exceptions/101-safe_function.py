#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        div = fct(*args)
        return div
    except Exception as er:
        print("Exception: {}".format(er), file=sys.stderr)
        return None
