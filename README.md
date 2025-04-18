# CT-API
A simple API to view and summarize data from [ClinicalTrials.gov](https://clinicaltrials.gov/).

# Installation 
[Docker](https://www.docker.com/) is required to successfully install and run this application. Run the following code in the terminal:

```
git clone https://github.com/chechung/CT-API.git
cd CT-API
docker compose up --build
```

Then access the application via the following address in your browser: http://localhost:8000/  
![alt text](https://github.com/chechung/CT-API/blob/main/images/home.png)

# Usage
This application can be used to view and summarize a clinical trial study based on its NCT ID or number. 
Two features are currently supported:

1. View data on a clinical trial study: supply an NCT ID to the `view` port. E.g.:
   `http://localhost:8000/view/NCT00841061`  
   ![alt text](https://github.com/chechung/CT-API/blob/main/images/view.png)
   
2. Summarize data on a clinical trial study: supply an NCT ID to the `summarize` port. E.g.:
   `http://localhost:8000/summarize/NCT00841061`  
   ![alt text](https://github.com/chechung/CT-API/blob/main/images/summarize.png)

# Documentation
The API documentation can be found here: http://localhost:8000/docs

# Repository structure: 
```
CT-API
└───images             [example images]
|   Dockerfile         [Docker build file]
|   compose.yml        [Docker compose configuration]
|   main.py            [Python script for application]
|   requirements.txt   [Python package dependencies]
```
