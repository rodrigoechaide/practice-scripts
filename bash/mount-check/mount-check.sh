#!/bin/bash

## Author: Rodrigo Echaide
## Usage
## ./mount-check.sh <dirs_to_check_if_mounted_separeted_with_a_space>
## ./mount-check.sh /mnt/shared/SAOCOM/ /mnt/it-team/ /mnt/shared/iso-files/ /mnt/ito-documents/

mountcheck()
{

DIR=$1;

for i in ${DIR[*]}
do
	if mount | grep "${i%/}" > /dev/null;
	then
    		echo "Directorio $i está montado"
	else
    		echo "ERROR: Directorio" $i "no está montado"
	fi
done
}


DIRS=()

for x in "$@"
do
	DIRS+=($x)
done

echo "The following directoies will be checked if they are mounted ${DIRS[*]}"
#echo "Number of items in original array: ${#DIRS[*]}"
mountcheck "${DIRS[*]}"
