# WideAngleLensView
## Project Overview
#### Our project is intended to do three things:
* Compile articles by use of The Guardian's API
* Analyze the TONE and MOOD of these articles using IBM Watson's Tone Analyzer
* Display a list of these articles, and links to these articles, using a table

## How to run and utilize our project:
1. Clone our repository
2. (And this is a matter of particular importance) Create a file, entitled "cred.csv", in both the repo's main branch AND in the "utils" directory
  * This file will be used to store your usernames and passwords, as well as API keys, for the two APIs.
3. Procure an API key for the Guardian API
   * This is done by going to [this website](https://bonobo.capi.gutools.co.uk/register/developer)
   * Here, just register an account with an email that you have NOT done so before with, and an API key will be sent to your email.
4. In the first line of the CSV file, write your login credentials for the Guardian API as so: 
   * email_address,API_key
5. Create an account with the Watson API
   * Use [this page](https://console.bluemix.net/registration/?target=%2Fcatalog%2Fservices%2Ftone-analyzer%3FtaxonomyNavigation%3Dapps) to register your account
   * From there, you will be sent an email asking you to confirm your account
6. In the CSV file, on the next line, type in your login info as such:
   * email_address,password
## REMEMBER: do NOT push the csv file with API keys and login credentials to the repo; leave it on your OWN computer
7. Create a virtual environment, pip-install flask and requests, and then run app.py as so:
  * python app.py