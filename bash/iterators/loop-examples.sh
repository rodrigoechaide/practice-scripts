#!/bin/bash

cd /home/rodrigo/Projects
OUTPUT="$(ls)"
arr=($OUTPUT)

x=0
y=0

for dir in "${arr[@]}"
do
if [ "$(ls -A /home/rodrigo/Projects/$dir)" == "" ]
then

echo "Empty"
empty[x]=$dir
x=$x+1

else

not_empty[y]=$dir
y=$y+1
echo "Not Empty"

fi

done

echo  ${empty}
echo  ${not_empty[0]} ${not_empty[1]} ${not_empty[2]} ${not_empty[3]} ${not_empty[4]}


if [ ${#empty[@]} -eq 0 ]; then
    echo "No empty directories"
else
    echo "Oops, something went wrong..."
fi
