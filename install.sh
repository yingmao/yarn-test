#!/bin/sh
python3 setup.py
cat /mapreduce-test/workers | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        ssh root@$line -n "rm -rf /yarn-test/ && mkdir /yarn-test/"
        echo "Copy data to $line"
        scp  /yarn-test/setup.py root@$line:/yarn-test/
        echo "Setup $line"
        ssh root@$line -n "cd /yarn-test/ && python3 setup.py"
        echo "Finished config node $line"
    fi
done

rm -rf HiBench
git clone https://github.com/intel-hadoop/HiBench
master=$(cat /mapreduce-test/manager)
cp hibench.conf HiBench/conf/
cp hadoop.conf HiBench/conf/
sed -i "s/node-0/$master/g" HiBench/conf/hadoop.conf
