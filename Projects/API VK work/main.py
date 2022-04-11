from pprint import pprint
from API_VK import VkUser
from Ya_upload import YaUploader
import time
from progress.bar import ChargingBar
import json

with open('VK_Token.txt', 'rt') as f:
    VK_Token = f.read().strip()


def main_function(user_id, vk_token, ya_token, qty, folder_path):
    client = VkUser(vk_token)
    ya = YaUploader(ya_token)
    ya.create_folder(folder_path)
    result = client.get_photos_vk(user_id, qty)
    photos_list = []
    with ChargingBar('Processing', max=len(result)) as bar:
        for item in result:
            photos_dict = {
                'file name': f'{item["likes"]["count"]}_{item["date"]}.jpg',
                'size': item['sizes'][-1]['type'],
                'url': item['sizes'][-1]['url']
            }
            url = photos_dict['url']
            ya.upload(f'disk:/{folder_path}/{str(photos_dict["file name"])}.jpg', url)
            photos_list.append(photos_dict)
            bar.next()
            time.sleep(1)
    bar.finish()
    pprint(photos_list)
    with open('upload_result.json', mode='wt', encoding='utf-8') as file:
        json.dump(photos_list, file)


if __name__ == '__main__':
    main_function(
        input('Введите id пользователя: '),
        VK_Token,
        input('Введите токен Яндекс Диска: '),
        input('Введите кол-во загружаемых фото: '),
        input('Введите название папки: '))
