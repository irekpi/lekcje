import requests
import os
import shutil


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


url = 'http://www.mobilo24.eu/spis/'
dir_path = 'pomoce/'
tmpfile = 'download.tmp'
file = 'spis.html'

tmpfile_path = os.path.join(dir_path, tmpfile)
file_path = os.path.join(dir_path, file)

try:
    if os.path.exists(tmpfile_path):
        os.remove(tmpfile_path)
    save_url_to_file(url, tmpfile_path)

    print('Copying file {} {}'.format(tmpfile_path, file_path))
    shutil.copy(tmpfile_path, file_path)

except requests.exceptions.ConnectionError as e:
    print('Provided url is faulty')

except PermissionError as e:
    print('File {} is Read-only'.format(file))

except FileNotFoundError as e:
    print('File not found')

except Exception as e:
    print('Error downloading the URL {}'.format(url))
    print('Error details: {}'.format(e))

else:
    print('URL downloaded successfully {}'.format(file))

finally:
    if os.path.exists(tmpfile_path):
        print('Final removal of the file {}'.format(tmpfile_path))
        os.remove(tmpfile_path)
    print('DONE!')


