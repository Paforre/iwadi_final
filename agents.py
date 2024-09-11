from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool, SerperDevTool
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
import os
import json
from typing import List
from schemas import Parcours
from ast import literal_eval
#from get_api_keys import get_api_keys

import PyPDF2  
import pandas as pd

os.environ["SERPER_API_KEY"]= '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'

llm_groq = ChatGroq(temperature=0,groq_api_key=os.environ["SERPER_API_KEY"],model="llama-3.1-70b-versatile")

# llm_ollama = ChatOllama(
#     temperature=0,
#     model = "llama3.1",
#)

file_path_pdf= "Guide D'orientation 2024-2025.pdf"
file_path_excel = "Extraction.xlsx"
 

exemple_parcours ="""
{type: 'Excellence',
  'formations': [
    {
      'filière': "Licence statistique",
      'ecoles': ["African School of Economics", "Ecole Nationale d'Economie "],
      'domaine': 'statistique & Economie',
      'niveau': "Bac"
    }
  ]
}
"""
class ReadPDFTool(BaseTool):
    name:str = "ReadPDFTool"
    description : str = "outil pour extraire du texte d'un fichier pdf"

    def _run(self,filepath:str) -> str:
        pdf_text = ""

        try:
            with open(filepath,"rb") as f:
                reader = PyPDF2.PdfFileReader(f)
                for page in range(len(reader.pages)):
                    pdf_text = reader.pages[page].extract_text()
                return pdf_text
        except FileNotFoundError :
            return f"Erreur! Le fichier {filepath} spécifié n'est pas trouvé."
        except Exception as e:
            return f"Une erreur est survenue lors de la lecture du fichier pdf {filepath}."


class ReadExcelTool(BaseTool):
    name:str = "ReadExcelTool"
    description : str = "outil pour extraire du texte d'un fichier excel"

    def _run(self,filepath:str) -> dict:

        try:
            df = pd.read_excel(filepath)
            data = df.to_dict(orient='list')
            return data
        
        except FileNotFoundError :
            return f"Erreur le fichier {filepath} spécifié n'est pas trouvé"
        except Exception as e:
            return f"Une erreur lors de la lecture du fichier excel {filepath}."




#La définition de l'agent : son role, goal, backstory (contexte),llm, tool, verbose ( pour afficher tous les messages d'interaction)
agent = Agent(
    role="Conseiller en orientation et insertion professionelle au Bénin",
    goal = "Proposer des parcours académiques en vue de la construction d'une carrière professionnelle en fonction de la filière ou spécialité actuelle, le métier souhaité ou la passion, les matières préférées ou compétences, le niveau d'étude actuelle.",
    backstory = "Tu es un agent spécialisé dans le conseil en orientation et insertion professionnelle au Bénin."
    f"Ta mission est te servir du fichier {file_path_excel} pour proposer des parcours académiques adaptés à un utilisateur au Bénin.",
    allow_delegation=False,
    verbose= True,
    tool = [SerperDevTool(), ReadExcelTool()],
    llm= llm_groq
)

exemple = "{'type': 'Parcours classique','formations': [{'intitule_filiere': 'Licence en Informatique','ecoles': ['Université de Paris', 'Université dAbomey Calavi'],'niveau_detude': 'Bac','domaine_detude': 'Informatique'}],....}"
task= Task(
    description =(
        f"1-Se servir du fichier {file_path_excel} d'orientation des élèves et étudiants du Bénin et proposer des parcours 4 types de parcours: parcours excellence, parcours public, parcours normal, parcours privé."
        "Le parcours excellence est le parcours dans les écoles réputées et bien côtées indépendamment du coût de la formation au Bénin."
        "Le parcours public est le parcours dans les établissements dont le statut est public au Bénin"
        "Le parcours privé est le parcours dans les écoles et universités de statut privé au Bénin"
        "Le parcours normal est le parcours dans les écoles et universités accessibles au Bénin"
        "2- Fournir le parcours sous forme d'un json en te basant sur les informations suivantes qui te sont fournies:{niveau_etude}, {specialite}, {matieres}, {passions} et {metier}"
        ),
        expected_output="Une liste de json de parcours contenant des dicts de clés type,formations. La clé formation contient une liste de dictionnaires ayant pour clé filière,ecoles,domaine,niveau(a choisir parmi la liste suivante :Bac, Licence, Master, Doctorat). Donne le parcours dans un ordre hierarchique. Ne renvois pas de commentaire.",
        output_file = 'parcours_academiques.json',
        agent=agent


)

crew = Crew(
    agents= [agent],
    tasks = [task],
    verbose=True
)

def generateParcours(
        niveau_etude: str,
        specialite: str | None = None,
        matieres: str | None = None,
        metier: str | None = None,
        passions: str | None = None,
) -> List[Parcours | None]:
    template_inputs = {
        "niveau_etude":niveau_etude,
        "specialite":specialite,
        "matieres" :matieres,
        "passions":passions,
        "metier":metier    
    }
   
    
    result = crew.kickoff(inputs=template_inputs)
    result=literal_eval(result.raw)
    return result