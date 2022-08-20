import requests
import time


# Get your token by chatting with BotFather:
# Create your own bot by calling /newbot and giving it a Name + Username.
# After that you will get your http api token.. Paste it below!
botToken = "5629707692:AAFoB31K7003skX9Iqsdf72Y9zaX1HoBqLQ"

# You need to get a chatID of your chat:
# To get this, first dm the bot and then paste this in your browser url bar:
# https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
# Replace <YOUR_BOT_TOKEN> with the token you got earlier.
# Dont worry, the response looks quite ugly and unreadable but thats no problem.
# You just need to press CTRL+F (Mac: COMMAND+F) and search for id.
# Paste the first result in the variable below.
chatID = "0000000000"

# Input the ID of your cryptoCurrency below (lowercase name of the crypto currency in most cases)
cryptoCurrency = "eos"

# Define your threshold. If the price is higher than this value the server will notify you. (!Price is in dollars!)
priceThreshold = 1.30


def get_price(coinID: str) -> int:
    response = requests.get("https://api.coinstats.app/public/v1/coins") # GET all api data (json format)
    json_data = response.json()
    for cryptoCurrency in json_data['coins']:
        if cryptoCurrency['id'] == coinID:
            if cryptoCurrency['price'] > priceThreshold:
                send_telegram_message(f"{coinID} went over {priceThreshold}!")

def send_telegram_message(msgText: str) -> str:
    requests.get("https://api.telegram.org/bot"+ botToken +"/sendMessage?chat_id="+ chatID +"&text= "+ msgText)


while True:
    get_price(cryptoCurrency)
    time.sleep(60)