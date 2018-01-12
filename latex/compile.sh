#!/bin/bash

for texfile in `/bin/ls -1 *.tex | /usr/bin/grep -v template`; do
    # Procedure:
    # - turn plain latex into templated latex
    # - pdflatex: latex to pdf
    # - convert: pdf to image
    
    tmpfile="`echo $texfile | sed 's/.tex/_tmp.tex/g'`"
    jpgfile="`echo $texfile | sed 's/.tex/.jpg/g'`"
    pdffile="`echo $texfile | sed 's/.tex/_tmp.pdf/g'`"

	echo "Processing $texfile"

    cp template.tex $tmpfile
    sed -i "s/FILENAME/$texfile/g" $tmpfile 

    # latex to pdf
    pdflatex \
        -interaction nonstopmode \
        $tmpfile $pdffile \
        && rm -f *.aux *.log

    # pdf to image
    convert            \
        -verbose       \
        -density 500   \
        -trim          \
             $pdffile  \
        -quality 100   \
        -flatten       \
        -sharpen 0x1.0 \
             $jpgfile

    rm -f $tmpfile 
    rm -f $pdffile

done
