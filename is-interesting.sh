#!/bin/bash
FIRST=0
SECOND=0
THIRD=0
FOURTH=0
for i in $* ; do
  if [ $i -eq 1 ]; then FIRST=1 ; fi
  if [ $i -eq 2 ]; then SECOND=1 ; fi
  if [ $i -eq 3 ]; then THIRD=1 ; fi
  if [ $i -eq 4 ]; then FOURTH=1 ; fi
done
if [ $FIRST -eq 1 ] ; then
  if [ $SECOND -eq 1 ] ; then
    if [ $THIRD -eq 1 ] ; then
      if [ $FOURTH -eq 1 ] ; then
        exit 1 # interesting
      fi
    fi
  fi
fi
exit 0