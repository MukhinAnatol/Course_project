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
        if response.status_code == 201:
            print(f'Папка {folder_path} успешно создана')
            return response.json()

    # def upload(self, file_path: str, file_name: str):
    #     href = self.get_url(file_path=file_path).get('href')
    #     upload = requests.put(href, data=open(file_name, 'rb'))
    #     upload.raise_for_status()
    #     if upload.status_code == 201:
    #         print("Success")

Ya = YaUploader(Ya_Token)
Ya.create_folder('new_folder')