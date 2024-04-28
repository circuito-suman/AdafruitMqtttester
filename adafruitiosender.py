import paho.mqtt.client as mqtt

SERVER_ADDRESS = "io.adafruit.com"
PORT = 1883
CLIENT_ID = "IwillPublish"
TOPIC = "circuito_suman/feeds/Name"
QOS = 1

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
def on_publish(client, userdata, mid):
    print("Message published")

def main():
    list=[0,5,6,7]
    list
    list.sort
    list.append(70)
    while(1):
        playerName = input("Enter your name: ")
        payload = f"{playerName}"
        client = mqtt.Client(CLIENT_ID)
        client.on_connect = on_connect
        client.on_publish = on_publish
        client.username_pw_set("your_username", "your_password") 
        client.connect(SERVER_ADDRESS, PORT, 60)
        client.loop_start()
        print("Publishing message:", payload)
        client.publish(TOPIC, payload, QOS)
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
