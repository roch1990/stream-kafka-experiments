# Полезные команды для кафки

## get topic info
kafka-topics.sh --describe --zookeeper zookeeper:2181 --topic mytopic

## get cluster nodes
zookeeper-shell.sh zookeeper:2181 ls /brokers/ids

## get cluster node info
zookeeper-shell.sh zookeeper:2181 get /brokers/ids/{id}

## get consumer groups
kafka-consumer-groups.sh --bootstrap-server 10.5.0.8:9094 --list
