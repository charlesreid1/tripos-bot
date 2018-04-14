#!/bin/bash
#
# Run this script two ways:

GREP="`which grep`"
#GREP="/bin/grep"


if [[ "`which pdflatex`" -eq "" ]]; then
    echo "You do not appear to have pdflatex installed."
    echo "Aborting..."
    exit 1;
fi

if [[ "`which convert`" -eq "" ]]; then
    echo "You do not appear to have pdflatex installed."
    echo "Aborting..."
    exit 1;
fi

if [[ -n "$1" ]]; then
    texfiles="`/bin/ls -1 $1.tex | $GREP -v template`"
else
    texfiles="`/bin/ls -1 *.tex | $GREP -v template`"
fi

echo $texfiles

for texfile in $texfiles; do

    # Procedure:
    # - turn plain latex into templated latex
    # - pdflatex: latex to pdf
    # - convert: pdf to image
    
    tmpfile="`echo $texfile | sed 's/.tex/_tmp.tex/g'`"
    jpgfile="`echo $texfile | sed 's/.tex/.jpg/g'`"
    pdffile="`echo $texfile | sed 's/.tex/_tmp.pdf/g'`"
    auxfile="`echo $texfile | sed 's/.tex/_tmp.aux/g'`"
    logfile="`echo $texfile | sed 's/.tex/_tmp.log/g'`"

    echo "Processing $texfile"

    if [ ! -f $jpgfile ]; then

        cp template.tex $tmpfile
        sed -i "s/FILENAME/$texfile/g" $tmpfile 

        # latex to pdf
        pdflatex \
            -interaction nonstopmode \
            -halt-on-error \
            $tmpfile $pdffile \
            && rm -f $auxfile $logfile

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

    fi

done
