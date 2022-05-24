# Branch Protection Automation

# Goal
Customer's security team requires a scalable solution to ensure proper reviews are done to code that is added into hundreds of repositories in a client org.  
Aim is to create a working solution that will accomplish an automated and scalable approach to apply github branch protection rules to any new repository whereby if any new code is merged goes via a code review process/worflow.

# Pre-requisites
1. A GitHub account & an org setup under the github account.
2. PAT (Personal access tokens) are required to establish authentication. To create please refer Github Docu https://github.com/settings/tokens
3. Python v3 or above 
4. Flask Framework
5. ngrok tunnelling tool to route localhost traffic to the internet. Other tools like seem.io can also be used.
6. Other dependencies as defined under requirements.txt

# Approach
1. Create webhook component that listens for organization events to know when a repository has been created. 
2. Once a new repository is created, apply branc protection rules automatically by leveraging github API.
3. Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

# Build & Usage
- Install listed pre-requisites
- Set GitHub token (GH_TOKEN). Extract your personal token from GitHub and add it as your environment variable. 
  Use the following command to add it as an environment variable : 
     MAC export GH_TOKEN = (your personal token)
     WIN set GH_TOKEN = (your personal token) or 
     Define GH_TOKEN = (your personal token) under Flask configuration file
- Edit your username (not orgname) in myapp.py file
- Start the local flask service using flask run --host=0.0.0.0 or execute the myapp.py file via debugger 
- Start ngrok server using ngrok http https://localhost:5000
- Note the forwarding address from ngrok (in this case https://XXXX.ngrok.io) (replace XXX with actual forwarded address)
- Add webhook to GitHub org and add the payload URL.
  - Set Payload URL = https://XXXX.ngrok.io (replace XXX with actual forwarded address)
  - Set content type as 'application/json'
  - Select Let me choose individual events to trigger and selected 'Repositories' and any other option as required to be listened to.  
- Save the webhook.

# Testing 
- Create a new repo under the org. with a new name. 
- Once the new repo is created, under branches check to see if there is a branch protection rule set up automatically.
- Check under issues to see if you are notified about the issue and appropriate branch protection rule addition.

# References
Follow comments under myapp.py file for additional context and usage

https://ngrok.com/docs 
https://docs.github.com/en/developers/webhooks-and-events/webhooks/about-webhooks 
https://github.com/jimzucker/github-webhooks 
https://docs.github.com/en/rest
