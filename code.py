import requests
import json
import base64
import env

################### Requried variables #######################

owner = env.owner
repo = env.repo
token = env.token
workspace = env.workspace
repo_slug = env.repo_slug
bittoken  =env.bittoken

git_url = "https://api.github.com/{}"
path = f'repos/{owner}/{repo}/branches'

headers = {"Accept": "application/vnd.github.v3+json",
           'Authorization': 'token ' + token}


######################## To Featch all branches ################################################


response = requests.get(git_url.format(path), headers=headers, allow_redirects=True)
data = response.json()
print(response.text , "For all Branches")

for branch in data:
    print('Branch Name = ',branch['name'])
    branchs = branch['name']
    
    headers = { "Authorization": f"Bearer {bittoken}",
           "Content-Type":"application/x-www-form-urlencoded"}
    

######################## To create new branch branches in bitbucket ############################


    url = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/refs/branches"

    headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {bittoken}"
    }

    data = {
        "name" : branch['name'],
        "target" : {"hash":"master"}
    }
    response = requests.request("POST", url, headers=headers,json = data )
    print(response.status_code, " For creating a new Branch")

    print(branch['name'], 'Branch Created in Bitbucket Repo')


######################## To Fetach files branches ############################

    content_url = f"https://api.github.com/repos/{owner}/{repo}/contents?ref={branchs}"
    response = requests.get(content_url)
    print(response.status_code, "Files in branch Github")

    for i in response.json():


######################## To Fetach files data ############################


        data_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branchs}/{i['name']}"
        response = requests.get(data_url)
        print(response.status_code, "Files Data")

        filename = i['name']
        data = response.text
        print(data)

        headers = { 
            "Authorization": f"Bearer {bittoken}",
            "Content-Type":"application/x-www-form-urlencoded"
        }

######################## To create new file with data form github branches ############################

        biturl = f"https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/src/"
        response = requests.post(biturl, headers=headers, data={filename:data , "branch": branchs},)
        print(response.status_code, " create new file")


print('-------------------------------Branch All Created------------------------------------')

######################## To featch all Open PR if there are any. ############################


headers = {"Accept": "application/vnd.github.v3+json",
           'Authorization': 'token ' + token}
path=f'repos/{owner}/{repo}/pulls'

response = requests.get(git_url.format(path),headers=headers,allow_redirects=True)

respoonse = response.json()
if len(respoonse)>0:
    print("Total PR: " ,len(respoonse))

    for i in respoonse:

        if i['state'] =='open':
            pr = dict()
            pr_title = i['title']
            source_branch = i['head']['ref']
            des_branch = i['base']['ref']
            title = i['title']

            url = f'https://api.bitbucket.org/2.0/repositories/{workspace}/{repo_slug}/pullrequests'

            payload ={
                "title": pr_title,
                "source": {
                    "branch": {
                        "name": source_branch
                    }
                },
                "destination": {
                    "branch": {
                        "name": des_branch
                    }
                }
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {bittoken}"
            }

            response = requests.post(
                url,
                json=payload,
                headers=headers
                )
            print('PR created ')
        else:
            pass
        print('-----------------------------------------All Open PR created-------------------------------')
        
else:
    print('No OPEN PR found.')