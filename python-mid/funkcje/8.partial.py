import os
from functools import partial

import requests


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


msg = "Please wait - the file {} will be downloaded"
dir = r'pomoce/'

# first vars for download
url = 'http://mobilo24.eu/spis'
file = 'spis.html'

# sec vars for download
url2 = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file2 = 'logo.png'

save_url_to_file_partial = partial(save_url_file, msg=msg, dir=dir)
save_url_to_file_partial(url=url, file=file)
save_url_to_file_partial(url=url2, file=file2)
