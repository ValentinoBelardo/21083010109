echo "a = 1200"
echo "b = 30"
echo "c = a dibagi b"
echo -e "\npernyataan yang benar mengenai c adalah"
echo "a. c lebih besar daripada b"
echo "b. c lebih besar daripada a"
echo -e "c. c sama dengan a \n"
echo "jawabannya adalah..."

a=1200
b=30

c=`expr $a / $b`


if [ $c -ge $b ]
then
echo "a benar"
elif [ $c -ge $a ]
then
echo "b benar"
elif [ $c -eq $a ]
then
echo "c benar"
else
echo "error"
fi

