import requests
from pprint import pprint
from API_VK import VkUser
from Ya_upload import YaUploader

with open('VK_Token.txt', 'rt') as f:
    VK_Token = f.read().strip()

# with open ('token_ya_disc.txt', 'rt') as f:
#     Ya_Token = f.read().strip()
id = 552934290
Ya_Token = 'AQAAAABRsTZTAADLW67xtAuJnUtIsPOYsqtQA50'

def main_function(user_id, vk_token, ya_token, folder_path):
    Client = VkUser(vk_token)
    Ya = YaUploader(ya_token)
    Ya.create_folder(f'disk:/test_path/{folder_path}')
    result = Client.get_photos_vk(user_id)
    photos_list = []
    for item in result:
        photos_dict = {
            'file name': f'{item["likes"]["count"]}.jpg',
            'size': item['sizes'][-1]['type'],
            'url': item['sizes'][-1]['url']
        }
        url = photos_dict['url']
        Ya.upload(f'disk:/test_path/{folder_path}/{str(photos_dict["file name"])}.jpg', url)
        photos_list.append(photos_dict)
    pprint(photos_list)
    return photos_list


if __name__ == '__main__':
    main_function(input('Введите id пользователя: '), VK_Token, input('Введите токен Яндекс Диска: '), folder_path=input('Введите название папки: '))