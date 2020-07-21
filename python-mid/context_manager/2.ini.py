import os, requests, zipfile


class FileDownloader:

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def __enter__(self):
        get_file = requests.get(self.url)
        with open(self.path, 'wb') as file:
            file.write(get_file.content)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


url_adress = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip'
file_path = 'pomoce/euroxref.zip'

with FileDownloader(url_adress, file_path) as f:
    with zipfile.ZipFile(f.path, 'r') as z:
        a_file = z.namelist()[0]
        os.chdir('pomoce/')
        z.extract(a_file, '.', pwd=None)