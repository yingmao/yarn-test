#!/bin/sh
cp /usr/local/hadoop/etc/hadoop/yarn-site-capacity.xml /usr/local/hadoop/etc/hadoop/yarn-site.xml
cat /mapreduce-test/slaves | while read line
do
    if [ "$line" = "-" ]; then
        echo "Skip $line"
    else
        echo "Copy config file to $line"
        scp  /usr/local/hadoop/etc/hadoop/yarn-site-capacity.xml root@$line:/usr/local/hadoop/etc/hadoop/yarn-site.xml 
        echo "Finished config node $line"
    fi
done
