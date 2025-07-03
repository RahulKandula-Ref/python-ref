import requests

res = requests.get('https://xkcd.com/353/')

print(res)
print(res.text)

res = requests.get('https://imgs.xkcd.com/comics/python.png')

print(res.headers)
print('status code ' + str(res.status_code))
if res.status_code == 200:
    with open('comic.png', 'wb') as f:
        f.write(res.content) # there is res.json too

print('done')