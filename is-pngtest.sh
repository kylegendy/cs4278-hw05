#!/bin/bash
rm -r libpng/deriv/
cp -r libpng/libpng-1.6.34/ libpng/deriv/

libpng/deriv/pngtest libpng/large-png-suite/1.png

gcov libpng/deriv/*.c

exit 0