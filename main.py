
config = configparser.ConfigParser()

config.read("config.ini")

#temps
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

#Creating object of client TG API
client = TelegramClient(username, api_id, api_hash)

client.start()

# channel_username = 'itemalert_bot'# your channel
channel_username = 'uselessfAk3'# your channel

test_of_name = ''
test_of_phone_number = ''

while True:
    for message in client.get_messages(channel_username, limit=1):
        msg_str = message.message

    print(msg_str)
    msg_date = message.date
    now_date = datetime.now()

    str_msg_date = msg_date.strftime('%m%d%Y%H%M%S')
    str_now_date = now_date.strftime('%m%d%Y%H%M%S')

    for_msg_date_checker = msg_date.strftime('%m%d%Y')
    for_now_date_checker = now_date.strftime('%m%d%Y')
    date_checker = for_msg_date_checker == for_now_date_checker

    msg_date_hours = int(str_msg_date[8:10])
    msg_date_minutes = int(str_msg_date[10:12])
    msg_date_seconds = int(str_msg_date[12:14])

    now_date_hours = int(str_now_date[8:10])
    now_date_minutes = int(str_now_date[10:12])
    now_date_seconds = int(str_now_date[12:14])

    sum_of_msg_time = msg_date_hours*3600 + msg_date_minutes*60 + msg_date_seconds + 3*3600
    sum_of_now_time = now_date_hours*3600 + now_date_minutes*60 + now_date_seconds
    sum_diff = sum_of_now_time - sum_of_msg_time

    phone_number = ''
    name_of_client = ''
    views = ''

    msg_list = msg_str.split()

    if sum_diff < 60 and date_checker is True:
        try:
            phone_number = msg_list[10]
            name_of_client = msg_list[11]
            views = msg_list[9]
        except IndexError:
            print('Неправильные данные')
            client.send_message('Zikki4444', 'Неверные данные бот выслал')
            pag.sleep(60)

    phone_number = phone_number.replace('📞+7', '')
    views = views.replace('👀', '')

    if sum_diff < 60 and date_checker is True:
        try:
            if int(views) < 100 and name_of_client != test_of_name and phone_number != test_of_phone_number:
                test_of_name = name_of_client
                test_of_phone_number = phone_number
                clicker(phone_number, name_of_client)
                client.send_message('Zikki4444', 'Занесено')
            else:
                print('Объявление не актуально на', now_date)
        except ValueError:
            print('Неправильные данные')
            client.send_message('Zikki4444', 'Неверные данные бот выслал')
            pag.sleep(60)
    else:
        print('Объявление не актуально на', now_date)