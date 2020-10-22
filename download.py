from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報

key = "0bac15eb3e872775aa3af2a653de72c7"
secret = "7b988d33210bb782"
wait_time = 0.5

#保存フォルダの指定
animalname = sys.argv[1]#検索キーワードとしてコマンドに引数をとる
savedir = "./" + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    safe_search = 1,
    extras = 'url_q, licence'
)

photos = result['photos']
#返り値を表示する
# pprint(photos)

for i,photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    #検索キーワードのフォルダが存在しなかったらその名でフォルダを作成する
    if not os.path.exists(savedir):
       os.makedirs(savedir)
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
