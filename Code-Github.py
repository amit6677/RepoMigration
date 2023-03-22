import requests
import json
import base64

################### Requried variables #######################
owner = input('Enter your owner Name: ')
repo = input('Enter your repo Name: ')
token = input('Enter your Github Token: ')

url = "https://api.github.com/{}"
path = f'repos/{owner}/{repo}/branches'

headers = {"Accept": "application/vnd.github.v3+json",
           'Authorization': 'token ' + token}

######################## To Featch all branches ################################################

response = requests.get(url.format(path), headers=headers, allow_redirects=True)
data = response.json()


######################## To Fetach all data from different branches ############################

for branch in data:
    print(branch['name'])
    branchs = branch['name']
    path = f'repos/{owner}/{repo}/zipball/{branchs}'
    print(url.format(path))
    response = requests.get(url.format(path), headers=headers, allow_redirects=True)

    if response.status_code == 200:
        filename = f'code-{branch}.zip'
        with open(filename, "wb") as f:
            f.write(response.content)
    else:
        print(f"Error: {response.status_code} {response.reason}")
        

######################## To featch all Open PR if there are any. ############################

path=f'repos/{owner}/{repo}/pulls'

response = requests.get(url.format(path),headers=headers,allow_redirects=True)
respoonse = response.json()

if len(respoonse)>0:
    print("Total PR: " ,len(respoonse))

    for i in respoonse:

        if i['state'] =='open':
            pr = dict()
            body = i['body']
            branch = i['default_branch']
            title = i['title']
            pr['description'] = body
            pr['title'] = title
            pr['branch'] = branch
            PRNUM= i['number']
            print(pr) 
            filename = f"PR-{branch}-{PRNUM}.json"

            with open(filename, "wb") as f:
                f.write(pr)

        else:
            pass

else:
    print('No OPEN PR found.')