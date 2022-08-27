import requests


class YaUploader:

    def __init__(self, token):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json','Authorization': f'OAuth {self.token}'}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        return response



if __name__ == '__main__':
    path_to_file = "test/myfile.txt"
    name_of_file = 'test.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, name_of_file)