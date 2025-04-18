from fastapi import FastAPI
from pydantic import BaseModel
import requests

class Study(BaseModel):
    nctID: str
    PMID: str
    condition: str
    intervention: str
    phase: str | None = None
    summary: str | None = None

app = FastAPI()

@app.get('/')
def root():
    return {'status': 'live'}

@app.get('/view/{study_id}')
def view_study(study_id: str):
    url = 'https://clinicaltrials.gov/api/v2/studies/' + study_id
    r = requests.get(url)
    return r.json()

@app.get('/summarize/{study_id}')
def summarize_study(study_id: str):
    url = 'https://clinicaltrials.gov/api/v2/studies/' + study_id
    r = requests.get(url)
    data = r.json()
    try: 
        pmid = data['protocolSection']['referencesModule']['references'][0]['pmid']
    except:
        pmid = None
    try: 
        condition = ', '.join(data['protocolSection']['conditionsModule']['conditions'])
    except: 
        condition = ''
    try:
        interventions = []
        for intervention in interventions: 
            interventions.append(intervention['name'])
        intervention = ', '.join(interventions)
    except: 
        intervention = ''
    try: 
        phase = ', '.join(data['protocolSection']['designModule']['phases'])
    except: 
        phase = None
    try: 
        summary = data['protocolSection']['descriptionModule']['briefSummary']
    except: 
        summary = None
    study = Study(
        nctID=study_id, 
        PMID=pmid, 
        condition=condition, 
        intervention=intervention, 
        phase=phase,
        summary=summary, 
    )
    return study
