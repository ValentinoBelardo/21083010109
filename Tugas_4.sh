#!/bin/bash

printf "input: "
read input

a=0
until [ ! $input -gt $a ]
do
	echo $input
	input=$((input-2))
done 
