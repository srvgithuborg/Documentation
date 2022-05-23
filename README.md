# Branch Protection Automation at Scale 

**What it does?

Intent of this web service is to replicate branch protection rules on multiple repositories once created. 

**How it Works:

The service listens for organization events to see when a repository is created. Once a new repository is created the web service triggers protection rules on the branch. It also notifies the owner of the organization with @mention in an issue within the repository that calls out that protection rules have been applied.

**Usage 

Look for comments under myapp.py file
