#!/bin/bash
# for i in $* ; do
#     cat ./wireworld-example/patch.$i | patch -p0 -s ./wireworld-example/wireworld-original.c
# done
# if gcc -c ./wireworld-example/wireworld-original.c ; then
#     for i in $* ; do
#         cat ./wireworld-example/patch.$i | patch -p0 -s -R ./wireworld-example/wireworld-original.c
#     done
#     exit 1
# fi
# for i in $* ; do
#     cat ./wireworld-example/patch.$i | patch -p0 -s -R ./wireworld-example/wireworld-original.c
#     echo $i
# done
gcc -c ./wireworld-example/wireworld-original.c
exit 0