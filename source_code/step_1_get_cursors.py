import requests, json

url ='https://api.twitter.com/2/search/adaptive.json?'
search = 'python programming'

#set parameter dan header
params = json.loads(open('../json_file/params.json', 'r').read())
params['q'] = search

#cursor pertama tidak ada
cursor = ''
params['cursor'] = cursor
headers = json.loads(open('../json_file/headers.json', 'r').read())

# buat ariabel cursors yang nantinya akan berisi cursor-cursor
cursors = ['']
#dapatkan cursor tiap request dan masukkan ke dalam variabel cursors
num = 0
while 1:
    params['cursor'] = cursor
    print(cursor)
    r = requests.get(url, params=params, headers=headers).json()
    if num == 0:
        cursor = r['timeline']['instructions'][0]['addEntries']['entries'][-1]['content']['operation']['cursor']['value']
    else:
        cursor = r['timeline']['instructions'][-1]['replaceEntry']['entry']['content']['operation']['cursor']['value']
    num +=1
    #set jumlahcursor yang akan diambil
    if num ==5:
        break
    cursors.append(cursor)

json.dump(cursors, open('../json_file/cursors.json', 'w'))