# Repo_migration

This python code is used to migrate your GitHub repository to bitbucket with all branches, tags and open PR's.

## GitHub Requirements:
  1. Token :- First you have to generate the token from your github account that you need to pass in the code.
   ## Here are the steps to generate the code
    ### 1). In the upper-right corner of any page, click your profile photo, then click Settings.
    ### 2). In the left sidebar, click  Developer settings.
    ### 3). In the left sidebar, under  Personal access tokens, click token (classic).
    ### 4). Then select all the checks.
    ### 5). Click Generate token.
   
## Bitbucket Requirements:
  ### 1. Token :- First you have to generate the repo token from your Bitbucket account that you need to pass in the code.
   ## Here are the steps to generate the token
    ### 1). Click on the repo in which you want to add code with all branches, tags and open PR's.
    ### 2). In the left sidebar, click Repository settings.
    ### 3). In the left sidebar, click Access tokens
    ### 4). Then click on Create Repository Access Token
    ### 5). Then select all the checks.
    ### 6). Click Create.
   
## Code procedure:
After all inputs were given in code first it will get all the branches from Github account. Then Create all branch in bitbucket that it finds in github repo. Then get file and files data in that perticuler branch and create simplery fiels in newlly created branch.
Then we will featch all Open PR in that perticular repositry and create similer in new PR for Newly created branch in bitbucket.

## GitHub Code procedure:

After all the inputs were given code will first fetch all of your branches of the provided repository.
Then it will pull code from each of your branches and download it in zip format.
After getting all code it will download all open PR from your git repository in json format.

## Bitbucket Code procedure:

After all the input was given code will first fetch the token that will expire after some time.
Then it is fetching user details from that particular bitbucket account.
Then it is fetching all repo details from that particular bitbucket account.


## Steps to Execute the Code
 ### 1). First install python in your system
 ### 2). Then clone the code from the github repe then open the terminal in the code folder.
 ### 3). Then run a command pip install -r requirements.txt
 ### 4). After that run the code with command python code.py
 ### 5). Then It will ask for the token of github and bitbucket. You have to add the tokens that we have generated in the above steps.
 ### 7). Then it will take time to migrate the repo with all branches, tags and open PR's

# Thank you for visiting the page

