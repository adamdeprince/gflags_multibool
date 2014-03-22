gflags_multibool
================

Multiple uses of the verbose flag to indicate successively greatere
degrees of verbosity is a common convention in Unix utilities due to
the relative ease of implementing this feature in C's getops library.

Google's [GFlags library](https://code.google.com/p/python-gflags/)
opts for a somewhat more modern approach; instead of -vvv a developer
might use gflag's enum type and write --verbosity=DEBUG.  This
approach, however, makes Gflags incompatible with tools and
conventions that specifically require the use of multiple flags.  Once
such instance is the Nagios alerting enviroment; it specifically
requires that fully compatible modules suport four levels of verbosity
ranging from no verbose flags to -vvv.

gflags_multibool makes it easy to write command line parsers that
support this convention.

Installation
============

````bash
pip install gflags_multibool}}
````

Example
=======

To see gflags_multibool in action we first create a minimal GFLAGS based application
 
````python
#!/usr/bin/env python
# demo_multibool.py

import gflags
import gflags_multibool

FLAGS = gflags.FLAGS

gflags_multibool.DEFINE_multibool('verbose', 0, 'Set verbosity', short_name='v')

def main(argv):
    FLAGS(argv)[1:]
    print("Verbosity level:", FLAGS.verbose)
if __name__ == "__main__" 
````

And we now run this on the command line:

````bash
python demo_multibool.py 
_Verbosity level: 0_
python demo_mutlibool.py -v -v -v 
_Verbosity level: 3_
python demo_multibool.py --verbose --verbose --noverbose
_Verbosity level: 1_
````