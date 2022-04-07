import requests

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
        response = req.json()['response']['items']
        return response

