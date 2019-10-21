#!/bin/bash


dist_id="$(lsb_release -is | tr '[:upper:]' '[:lower:]')"

echo $dist_id
