#!/usr/bin/env python
# demo_multibool.py

import gflags
import gflags_multibool

FLAGS = gflags.FLAGS

gflags_multibool.DEFINE_multibool('verbose', 0, 'Set verbosity', short_name='v')

def main(argv):
    FLAGS(argv)[1:]
    print("Verbosity level: %s" % FLAGS.verbose)

if __name__ == "__main__":
    import sys
    main(sys.argv)
