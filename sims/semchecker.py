from django.db import models
#from sematch.semantic.graph import DBpediaDataTransform, Taxonomy
#from sematch.semantic.similarity import ConceptSimilarity
#from .forms import sendIncidentForm
from django.db import models
#from sematch.semantic.graph import DBpediaDataTransform, Taxonomy
#from sematch.semantic.similarity import ConceptSimilarity
#from .forms import sendIncidentForm
from django.db import models
#concept = ConceptSimilarity(Taxonomy(DBpediaDataTransform()), 'sims/Incident_Ontology_IRI.txt')
#readForm=sendIncidentForm()
#concept=input("Incident Report")
#conceptTwo=readForm.cleaned_data['report']
#if(concept.similarity('sims/Incident_Ontology_IRI.txt', conceptTwo,'path')==True):
#   concept.category=conceptTwo
from collections import namedtuple
def semChecker():
    sampleIncidentCategory=("device", "request", "infrastructure")
    incidentReport=input("Incident Report\n")
    inputConcepts=incidentReport.split(" ")
    for part in inputConcepts:
        if part.lower() in sampleIncidentCategory:
            print('Incident Category: ', part)
        else:
            print('Incident Category: Infrastructure' )
    return incidentReport
semChecker()