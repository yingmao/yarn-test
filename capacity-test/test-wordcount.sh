#!/bin/sh
./capacity.sh
../start.sh
../HiBench/bin/workloads/micro/wordcount/prepare/prepare.sh
starttime=`date +'%Y-%m-%d %H:%M:%S'`
../HiBench/bin/workloads/micro/wordcount/hadoop/run.sh
endtime=`date +'%Y-%m-%d %H:%M:%S'`
start_seconds=$(date --date="$starttime" +%s);
end_seconds=$(date --date="$endtime" +%s);
echo "Test cost time:"$((end_seconds-start_seconds))"s"
../stop.sh
