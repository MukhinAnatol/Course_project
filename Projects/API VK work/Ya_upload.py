import requests

with open ('token_ya_disc.txt', 'rt') as f:
    Ya_Token = f.read().strip()

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return{
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder (self, folder_path: str):
        params = {"path": folder_path}
        headers = self.get_headers()
        create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(create_folder_url, headers=headers, params=params)
        print(response.json())
        if response.status_code == 201:
            print(f'Папка {folder_path} успешно создана')

    def upload(self, file_path, url: str):
        params = {
            'path': file_path,
            'url' : url
        }
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.post(url=upload_url, headers= self.get_headers(), params=params)

Ya = YaUploader(Ya_Token)
Ya.upload('test_path', 'https://sun9-48.userapi.com/impf/hZBImqkCXbzy3VGIhn30Jj4P3RWurerkaZZSnw/oDCgWwpSe34.jpg?size=580x807&quality=96&sign=e2d576d1b2cf05e8e8b9d9be2b4b2fb8&c_uniq_tag=UzBC-6GSTe_a1WxqGKsHwPyCUsS0NgHsvI_yuaG5BkQ&type=album')