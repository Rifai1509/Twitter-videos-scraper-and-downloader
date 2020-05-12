import requests,json

urls = json.loads(open('video_urls.json','r').read())

hit = 0
for url in urls:
    hit +=1
    if hit == 3:
        break
    r = requests.get(url)

    with open(f'{hit}.mp4', 'wb') as file:
        file.write(r.content)
        print(f'download video ke {hit} berhasil')