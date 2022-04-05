import requests
import time
from pprint import pprint

with open('VK_Token.txt', 'rt') as f:
     VK_Token = f.read().strip()

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version='5.131'):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photos_vk (self, id):
        get_photo_url = self.url + 'photos.get'
        get_photo_params = {
           'owner_id': id,
            'album_id': 'profile',
            'extended': '1',
            'rev': '0',
            'count': 5,
            'photo_sizes': '1'
        }
        req = requests.get(get_photo_url, params={**self.params, **get_photo_params})
        result = req.json()['response']['items']
        return result


#target_group_ids = ','.join([str(group['id']) for group in target_groups])



Client = VkUser(VK_Token)
pprint(Client.get_photos_vk(552934290))

#while True:
    #user_id = input('Введите id пользователя: ')
    #ya_disc_token = input('Введите токен для работы с яндекс диском: ')