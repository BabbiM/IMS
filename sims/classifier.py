from sematch.semantic.graph import DBpediaDataTransform, Taxonomy
from sematch.semantic.similarity import ConceptSimilarity
from .forms import sendIncidentForm
concept = ConceptSimilarity(Taxonomy(DBpediaDataTransform()), 'sims/Incident_Ontology_IRI.txt')
readForm=sendIncidentForm()
conceptTwo=readForm.cleaned_data['report']
if(concept.similarity('sims/Incident_Ontology_IRI.txt', conceptTwo,'path')==True):
   concept.category=conceptTwo



#     You can't get there from here
#     This application contains sensitive information and can only be
#     access from:
#     WBG domain joined devices. Access from personal devices
#     is not allowed.
#     please contact your administrator
#     more details
#     ok






#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'wup')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'li')
concept=input("Incident Report")














# A concept in the taxonomy with those semantically rich words extracted from the incident report.
    #print(concept.name2concept('actor'))
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'path')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'wup')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'li')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'res')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'lin')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'jcn')
#print concept.similarity('http://dbpedia.org/ontology/Actor', 'http://dbpedia.org/ontology/Film', 'wpath')