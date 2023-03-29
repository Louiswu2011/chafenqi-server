import json


class ServerConfig:
    jwt_secret = ''

    def __init__(self):
        f = open('config.json', 'r', encoding='utf-8')
        data = json.load(f)
        self.jwt_secret = data['jwt_secret']
        f.close()
