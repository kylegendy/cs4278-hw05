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
for i in $* ; do
  libpng/deriv/pngtest libpng/large-png-suite/$i.png
done

# check results
gcov libpng/deriv/*.c 
# HOW TO CHECK IF FILE RAN FINE??? WHERES THE LINES RAN OUTPUT??

# clean up -- remove all .gcov files
rm -r *.gcov

exit 0