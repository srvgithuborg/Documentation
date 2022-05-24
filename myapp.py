#Aim of this app is to automate branch protection rules on creation of a new repository

import json #Imports json lib
import os  #Imports json lib
import time # Imports time module for waiting between code execution
import requests # Imports requests lib for flask
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["POST"]) #supporting POST route method for flask app

#defining a function as a web-hook listener

def webhook():
# Storing incoming json data from webhook
    payload = request.get_json()
    #print (payload)
# Supplying username and access token for Github. This was set under the flask configuration file and was generated via Git personal account (PAT)
    user = "srvchawla"
    cred = os.environ["GH_TOKEN"]

# Verifying if the repo was created via json payload retrieved 
    try:
        if payload["action"] == "created":
            # Delay needed for server to create the page
            time.sleep(1)
            # Creating branch protection for the master or main branch of the repo. This is where various parameters of branch protection rules can be defined. 
            branch_protection ={
                "required_status_checks": {"strict": True, "contexts": ["default"]},
                "enforce_admins": False,
                "required_pull_request_reviews": 
                    {
                    "require_code_owner_reviews":True,"required_approving_review_count":1
                    },
                "restrictions": None,
                                }
            session = requests.session()
            session.auth = (user, cred)
            response_1 = session.put(
                payload["repository"]["url"] + "/branches/main/protection",
                json.dumps(branch_protection, indent=4)
               # print(json.dumps) 
                )
            if response_1.status_code == 200:
                print(
                    "Hello! Branch protection was created successfully. Status code: ",
                    response_1.status_code,
                )

                # Create issue in repo notifying user of branch protection
                try:
                    if payload["repository"]["has_issues"]:
                        issue = {
                            "title": "Branch Protection Rule Added",
                            "body": "@"
                                    + user
                                    + " A new branch protection was added to the master/main branch.",
                        }
                        session = requests.session()
                        session.auth = (user, cred)
                        response_2 = session.post(
                            payload["repository"]["url"] + "/issues", json.dumps(issue)
                        )
                        if response_2.status_code == 201:
                            print(
                                "Issue created successfully. Status code: ",
                                response_2.status_code,
                            )
                        else:
                            print(
                                "Unable to create an issue. Status code: ",
                                response_2.status_code,
                            )
                    else:
                        print(
                            "This repo has no issues so one cannot be created at this time."
                        )
                except KeyError:
                    # Request did not contain information about if the repository has issues enabled
                    pass
            else:
                print(response_1.content)
                print(
                    "Unable to create branch protection. Status code: ",
                    response_1.status_code,
                )
    except KeyError:
        # Ignore POST payload since it is not a create action
        pass
    return "OK"

if __name__ == "__main__":
    app.run()
