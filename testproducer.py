from pykafka import KafkaClient

def get_kafka_client():
    return KafkaClient(hosts="localhost:9092")


def get_client_topic(client):
    return client.topics['testTopic']

client = get_kafka_client()
topicname = get_client_topic(client)

producer = topicname.get_sync_producer()

count = 1

while count<1000:
    message = ("Hello from" + str(count)).encode('ascii')
    producer.produce(message)
    count = count + 1
