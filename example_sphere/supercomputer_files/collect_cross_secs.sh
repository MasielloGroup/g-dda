#!/bin/bash
# Collect all the files and write it to a file named Spectrum
for i in *eV ;do
    cd $i
    cp qtable temp
    sed -i -e "1,14d" temp
    cat temp >>../Spectrum
    rm temp
    cd ../
done
