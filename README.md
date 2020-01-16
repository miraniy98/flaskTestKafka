# flaskTestKafka
Testing Flask Consumer and Producer API with flask for realtime consumption of messages

This code requires Apache Kafka installed and running on your local machine. A Kafka topic has to be created to proceed. 
Follow [this](https://kafka.apache.org/documentation/) link to do so

Once installed follow the below steps:

1. Open the terminal and enter the directory flaskTestKafka
2. Execute `source venv/bin/activate`
3. Execute `pip install -r requirements.txt`
4. Execute `python app.py`
5. Open chrome and open the url [127.0.0.1:5004](127.0.0.1:5004)
6. Open a new terminal and execute `python testproducer.py`


testproducer.py produces 1000 messages and the flask consumer consumes it in realtime.
