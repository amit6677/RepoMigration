import requests
from base64 import b64encode

################### Requried variable #######################

refresh_token=input("Please enter refresh token")
Access_Id=input("Please enter Access Id")
Secret_Key=input("Please enter Secret Key")



######################## To Featch token ################################################
url = "https://bitbucket.org/site/oauth2/access_token"
payload=f'grant_type=refresh_token&refresh_token={refresh_token}'
headers = {
    "Authorization": "Basic {}".format(
        b64encode(bytes(f"{username}:{password}", "utf-8")).decode("ascii")
    ),
    "Content-Type": "application/x-www-form-urlencoded"
}

tokenResponse = requests.request("POST", url, headers=headers, data=payload)
print(tokenResponse.json())
token=tokenResponse.json()
token=token['access_token']
print(token)


######################## To fecth user details from a account ################################################

url = "https://api.bitbucket.org/2.0/user"

payload={}
headers = {
  'Authorization': f'Bearer  {token}'
}

userResponse = requests.request("GET", url, headers=headers, data=payload)
print(userResponse.json())
userdata=userResponse.json()
print(userdata)


######################## To fecth all repo from a account ################################################

url = f"https://api.bitbucket.org/2.0/repositories?access_token={token}&role=admin"
payload={}
headers = {}
reposResponse = requests.request("GET", url, headers=headers, data=payload)
print(reposResponse.text)


######################## To delete repo from a account ################################################
url = "https://api.bitbucket.org/2.0/repositories/workdatas/bitbucket"
headers = {
  "Authorization": f"Bearer {token}"
}
response = requests.request(
   "DELETE",
   url,
   headers=headers
)
print(response.text)




