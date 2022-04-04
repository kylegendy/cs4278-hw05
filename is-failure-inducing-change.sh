#!/bin/bash
cp ./wireworld-unzip/wireworld-original.c ./wireworld-unzip/wireworld-original_copy.c
for i in $* ; do
    cat ./wireworld-unzip/patch.$i | patch -p0 -s ./wireworld-unzip/wireworld-original_copy.c
done
gcc -c ./wireworld-unzip/wireworld-original_copy.c
res=$?
rm -f ./wireworld-unzip/wireworld-original_copy.c
if [ $res -eq 1 ]; then
    exit 1
fi
exit 0