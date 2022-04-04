#!/bin/bash
# create new testing dir
rm -r libpng/deriv/
cp -r libpng/libpng-1.6.34/ libpng/deriv/

# get percent threshold
# thresh_input="./perc.txt"
# while IFS= read -r line
# do
#   thresh=$line
# done < "$thresh_input"

# # pngtest all input
# for i in $* ; do
#   libpng/deriv/pngtest libpng/large-png-suite/1.png
# done

# check if gcov gets bad result
./libpng/deriv/pngtest ./libpng/large-png-suite/1.png ./libpng/deriv/
gcov libpng/deriv/*.c 

# remove all .gcov files
rm -r *.gcov

exit 0