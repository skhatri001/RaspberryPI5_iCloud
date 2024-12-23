INSTALLED_APPS = [
...
'storage',
...
]

STORAGES = {
"default":{
"BACKEND": "storages.backends.dropbox.DropboxStorage",
"OPTIONS": {
"oauth2_access_token":"sl.CDLYr2WpAZIB36uA-GBqBsuU_X0lmWY8kk5Ky4SntU3wdXGYGMsnMp_1JDshPlEeREJJELYn_QYXoQ7ZiFGMa4OrRhOowpseH2ecskY3DaEuP6TfxGDzzKsg0BdqkVPn028Av1G4p9FX"
"app_key":"6wr6mzj1yuhtgjr",
"app_secret": "3uxa6aynlxuuwql",
},
},
}

