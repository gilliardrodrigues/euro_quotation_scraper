import os
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
from utils.Mail import Mail
import sys
import dotenv

# Getting the sender e-mail credentials and setting some important variables:
dotenv.load_dotenv()
SENDER_EMAIL = os.getenv('SENDER_EMAIL')
SECURE_PASSWORD = os.getenv('SECURE_PASSWORD')
if float(sys.argv[1]) < 60:
    DESIRED_THRESHOLD = 60
else:
    DESIRED_THRESHOLD = float(sys.argv[1])
COOLDOWN_TIME_IN_SECS = float(sys.argv[2])
EMAIL_ADDRESS = sys.argv[3]

while True:
    # Opening a session:
    session = requests.Session()
    # Sending a GET request to the page we want to scrape:
    cookies = {
        'SOCS': 'CAISOAgSEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjMwMzA1LjA5X3AxGgVwdC1CUiACGgYIgKCfoAY'
    }
    page = session.get('https://www.google.com/finance/quote/EUR-BRL', cookies=cookies)
    # Building a BeautifulSoup object from the page:
    soup = BeautifulSoup(page.text, 'html.parser')
    # Getting the tag that contains the quotation:
    html_tag = soup.find(class_='YMlKec fxKbKc')
    # Getting the value from html tag:
    euro_quotation = html_tag.get_text()
    # Getting the current date and time:
    current_date = datetime.now().strftime('%d/%m/%Y')
    current_time = datetime.now().strftime('%Hh%M')
    # Printing the result and sleeping for at least 60 secs:
    print(f'Valor do euro às {current_time} de {current_date}: R${euro_quotation}')
    # Checking if the quotation is below the desired and sending an e-mail if it's:
    if float(euro_quotation) <= DESIRED_THRESHOLD:
        mail = Mail(SENDER_EMAIL, SECURE_PASSWORD)
        mail.send(
            'Cotação do euro aceitável!',
            f'Valor do euro às {current_time} de {current_date}: R${euro_quotation}',
            EMAIL_ADDRESS)
    time.sleep(COOLDOWN_TIME_IN_SECS)
