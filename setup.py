import os
import sys, socket

def writeHadoopConfigFile(name,xml):
    f = open("/usr/local/hadoop/etc/hadoop/" + name,"w")
    f.write(xml)
    f.close()

mf = open("/mapreduce-test/master","r")
mip = mf.read().strip()
mf.close()

print("Config Hadoop 2.9.2 YARN...")

yarnSiteXml = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>%(mip)s</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>%(mip)s:8032</value>
  </property>
  <property>
     <name>yarn.resourcemanager.scheduler.address</name>
     <value>%(mip)s:8030</value>
  </property>
  <property>
     <name>yarn.resourcemanager.resource-tracker.address</name>
     <value>%(mip)s:8031</value>
  </property>
  <property>
     <name>yarn.resourcemanager.admin.address</name>
     <value>0.0.0.0:8033</value>
   </property>
   <property>
      <name>yarn.resourcemanager.webapp.address</name>
      <value>0.0.0.0:8088</value>
   </property>
   <property>  
      <name>mapreduce.jobhistory.address</name>  
      <value>%(mip)s:10020</value>  
   </property>  
   <property>  
      <name>mapreduce.jobhistory.webapp.address</name>  
      <value>0.0.0.0:19888</value>  
   </property>
</configuration>
""" % dict(mip=mip)
writeHadoopConfigFile("yarn-site.xml",yarnSiteXml)
writeHadoopConfigFile("yarn-site-capacity.xml",yarnSiteXml)

yarnSiteXml = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
    <property>
        <name>yarn.resourcemanager.hostname</name>
        <value>%(mip)s</value>
    </property>

    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>

    <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
    </property>
  <property>
    <name>yarn.resourcemanager.address</name>
    <value>%(mip)s:8032</value>
  </property>
  <property>
     <name>yarn.resourcemanager.scheduler.address</name>
     <value>%(mip)s:8030</value>
  </property>
  <property>
     <name>yarn.resourcemanager.resource-tracker.address</name>
     <value>%(mip)s:8031</value>
  </property>
  <property>
     <name>yarn.resourcemanager.admin.address</name>
     <value>0.0.0.0:8033</value>
   </property>
   <property>
      <name>yarn.resourcemanager.webapp.address</name>
      <value>0.0.0.0:8088</value>
   </property>
   <property>  
      <name>mapreduce.jobhistory.address</name>  
      <value>%(mip)s:10020</value>  
   </property>  
   <property>  
      <name>mapreduce.jobhistory.webapp.address</name>  
      <value>0.0.0.0:19888</value>  
   </property>
<property>
<name>yarn.resourcemanager.scheduler.class</name>
<value>org.apache.hadoop.yarn.server.resourcemanager.scheduler.fair.FairScheduler</value>
</property>
<property>
<name>yarn.scheduler.fair.allocation.file</name>
<value>/usr/local/hadoop/etc/hadoop/fair-scheduler.xml</value>
</property>
<property>
<name>yarn.scheduler.fair.preemption</name>
<value>true</value>
</property>
<property>
<name>yarn.scheduler.fair.user-as-default-queue</name>
<value>true</value>
<description>default is True</description>
</property>
<property>
<name>yarn.scheduler.fair.allow-undeclared-pools</name>
<value>false</value>
<description>default is True</description>
</property>
</configuration>
""" % dict(mip=mip)
writeHadoopConfigFile("yarn-site-fair.xml",yarnSiteXml)

fairSchedulerXml = """<?xml version="1.0"?>
<allocations>  
  <queue name="sample_queue">  
    <minResources>10000 mb,0vcores</minResources>  
    <maxResources>90000 mb,0vcores</maxResources>  
    <maxRunningApps>50</maxRunningApps>  
    <weight>2.0</weight>  
    <schedulingPolicy>fair</schedulingPolicy>  
    <queue name="sample_sub_queue">  
      <minResources>5000 mb,0vcores</minResources>  
    </queue>  
  </queue>  
  <user name="sample_user">  
    <maxRunningApps>30</maxRunningApps>  
  </user>  
  <userMaxAppsDefault>5</userMaxAppsDefault>  
</allocations>  
"""
writeHadoopConfigFile("fair-scheduler.xml",fairSchedulerXml)
