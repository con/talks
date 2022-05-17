#!/bin/bash

sed -n -e '/<img/s,.*data-src="\([^"]*\)".*,\1,gp' index.html \
| while read p; do
    if [ ! -e "$p" ]; then
        echo -n "$p missing"
        for d in /home/yoh/proj/repronim/artwork/talks/webinar-2020-reprocomp \
					 /home/yoh/proj/datalad/datalad-course \
					 /home/yoh/proj/experiments/nuisance/presentations/2020-NNL \
					 /home/yoh/proj/dandi/artwork \
					 /home/yoh/proj/pymvpa/papers \
					 /home/yoh/proj/datalad/artwork/talks/2022-abcd \
				 ; do
            c="$d/$p"
            if [ -e "$c" ]; then
                cp --reflink=auto "$c" "$p"
                echo " OK - copied"
                break
            fi
        done
        [ -e "$p" ] || { echo " !!Failed to find $p"; exit 1; }
    fi
done
