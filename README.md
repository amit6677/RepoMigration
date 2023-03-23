# Repo_migration

This python code is used to migrate your GitHub repository to bitbucket with all branches, tags and open PR's.

## GitHub Requirements:
  1. Token :- First you have to generate the token from your github account that you need to pass in the code.
   ## Here are the steps to generate the code
    1. In the upper-right corner of any page, click your profile photo, then click Settings.
    ![image](https://user-images.githubusercontent.com/128475997/227165846-515f8b10-5b70-4b7e-b54d-2625201f68ed.png)



## Code procedure:

After all the inputs were given code will first fetch all of your branches of the provided repository.
Then it will pull code from each of your branches and download it in zip format.
After getting all code it will download all open PR from your git repository in json format.


## Bitbucket Requirements:
These parameters are mandatory to use bitbucket APIs.
You have to follow this document to get these details.
https://support.atlassian.com/bitbucket-cloud/docs/use-oauth-on-bitbucket-cloud/

  1. Refresh Token :- Input the refresh token to regenerate the token.
  2. Access_Id :- Input the Access_Id.
  3. Secret_Key :- Enter the Access_Id.
 
 
## Code procedure:

After all the input was given code will first fetch the token that will expire after some time.
Then it is fetching user details from that particular bitbucket account.
Then it is fetching all repo details from that particular bitbucket account.
After that there is a code to delete a particular repo from an account.


Note:-- Currently the code is not creating the repo in the bitbucket to migrate the code. The above token doesn't have permissions to create the repo or push the code for that we do have to purchase a premium plan as in the screenshots.
https://prnt.sc/Dz6AevFWeht5
