import requests

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
        #print(response.json())
        if response.status_code == 201:
            print(f'Папка {folder_path} успешно создана')

    def upload(self, file_path, url: str):
        params = {
            'path': file_path,
            'url' : url
        }
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        response = requests.post(url=upload_url, headers= self.get_headers(), params=params)
        print(response.json())
