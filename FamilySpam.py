import requests
import random
import threading

def start():
    while True:
        with open('bot.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        random_line = random.choice([line.strip() for line in lines if ':' in line])
        uid, accessToken = random_line.split(':')

        generate_region = ["zh_CN", "en_US", "de_DE", "es_ES", "fr_FR", "hi_IN", "in_ID", "it_IT", "ja_JP", "ko_KR", "pl_PL", "pt_PT", "ru_RU", "th_TH", "tr_TR", "uk_UA", "vi_VN"]

        region = random.choice(generate_region)

        memberType = random.choice([1, 2, 3, 4])
        ownerType = random.choice([1, 2, 3, 4])
        age = random.randint(9, 200)

        API_1 = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

        headers_1 = {'userId': uid, 'Access-Token': accessToken, 'User-Agent': 'okhttp/3.12.1'}

        response = requests.delete(API_1, headers=headers_1)

        API_2 = "http://modsgs.sandboxol.com/friend/api/v1/family/recruit"

        data_1 = {'age': age, 'memberType': memberType, 'ownerType': ownerType}

        headers_2 = {'userId': uid, 'Access-Token': accessToken, 'userLanguage': region, 'appVersion': '4962', 'User-Agent': 'okhttp/3.12.1'}

        response = requests.post(API_2, headers=headers_2, json=data_1)

        print(response.text)

threads = []
for i in range(20):
    t = threading.Thread(target=start)
    t.start()
    threads.append(t)
