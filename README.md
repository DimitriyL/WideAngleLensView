# WideAngleLensView
## Project Overview
#### Our project is intended to do three things:
* Compile articles by use of The Guardian's API
* Analyze the TONE and MOOD of these articles using IBM Watson's Tone Analyzer
* Display a list of these articles, and links to these articles, using a table

## How to run and utilize our project:
1. Clone our repository
2. (And this is a matter of particular importance) Create a file, entitled "cred.csv", in both the repo's main branch AND in the "utils" directory
   * This file will be used to store your API keys for the two APIs.
3. Create an account with the Watson API
   * Use [this page](https://console.bluemix.net/registration/?target=%2Fcatalog%2Fservices%2Ftone-analyzer%3FtaxonomyNavigation%3Dapps) to register your account
   * From there, you will be sent an email asking you to confirm your account
4. In the CSV file, on the first line, type in your login info as such:
   * watson,api_key,password
## REMEMBER: do NOT push the csv file with API keys and login credentials to the repo; leave it on your OWN computer
5. Procure an API key for the Guardian API
   * This is done by going to [this website](https://bonobo.capi.gutools.co.uk/register/developer)
   * Here, just register an account with an email that you have NOT done so before with, and an API key will be sent to your email.
6. On the second line of the CSV file, write your login credentials for the Guardian API as so: 
   * guardian,api_key,NULL
   * there is no need to enter a password here
7. Create a virtual environment, pip-install flask and requests, and then run app.py as so:
  ```shell 
  $ python app.py
  ```
8. The app will take a long time to run (maybe ~30 seconds). This is due to the nature of the large number of api calls being made. Please be patient!
## In the case of Mr. DW and ONLY Mr. DW using our project:
  * A csv file of keys and passwords has already been sent to you.
  * Simply copy this file into the "utils" directory, and that should render the project usable.
