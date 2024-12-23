
import webbrowser
import dropbox
import dropbox.files
import os
from PIL import Image

os.chdir('/home/skhatri007')
token = 'sl.CDLYr2WpAZIB36uA-GBqBsuU_X0lmWY8kk5Ky4SntU3wdXGYGMsnMp_1JDshPlEeREJJELYn_QYXoQ7ZiFGMa4OrRhOowpseH2ecskY3DaEuP6TfxGDzzKsg0BdqkVPn028Av1G4p9FX'

APP_Key = '<6wr6mzj1yuhtgjr>'
#url = f'https://www.dropbox.com/oauth2/authorize?client_id={APP_Key}&' \
# f'response_type=code&token_access_type=offline'
#webbrowser.open(url)
dbx = dropbox.Dropbox(token)

def download_file():
	for entry in dbx.files_list_folder("").entries:
		dbx.files_download_to_file(os.path.join("/home/skhatri007/Documents/picture-frame",entry.name),f"/{entry.name}")
	return entry.name

image = download_file()
dir = os.chdir('/home/skhatri007/Documents/picture-frame')
#print(image)
img = Image.open(image)
img.show()

