import requests, json

url ='https://api.twitter.com/2/search/adaptive.json?'
search = 'python programming'

headers = json.loads(open('headers.json','r').read())
params = json.loads(open('params.json','r').read())
params['q'] = search

cursors = json.loads(open('cursors.json','r').read())

hitung = 0
video_url_list = []
for cursor in cursors:
    params['cursor'] = cursor
    r = requests.get(url,params=params, headers=headers).json()
    print(r)
    ids = r['globalObjects']['tweets'].values()
    for id in ids :
        # print(id)
        hitung+=1
        print(hitung)
        try:
            varian = id['extended_entities']['media'][0]['video_info']['variants']
        except:
            continue
        video_list = []
        for v in varian:
            if 'bitrate' in v:
                video_list.append(v)
        video_url = video_list[0]['url']
        hitung +=1
        print(hitung)
        print(video_url)
        video_url_list.append(video_url)

json.dump(video_url_list, open('video_urls.json','w'))