from schemas import Parcours
from typing import List


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
    """ # Placer les docstrings
    Function for generating a list of paths based on user request

    Args (Form): the entry request with user data

    Returns (JSON): a list of JSON objects withe the proposed paths
    """
    return [
  {
    "type": "Parcours Excellence",
    "formations": [
      {
        "filière": "Mathématiques et Informatique",
        "écoles": "Université d'Abomey-Calavi - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Licence"
      },
      {
        "filière": "Statistique et Mathématique",
        "écoles": "Université d'Abomey-Calavi - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Master"
      },
      {
        "filière": "Ingénierie Statistique",
        "écoles": "Université d'Abomey-Calavi - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Doctorat"
      }
    ]
  },
  {
    "type": "Parcours Public",
    "formations": [
      {
        "filière": "Mathématiques et Informatique",
        "écoles": "Université Nationale du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Licence"
      },
      {
        "filière": "Statistique et Mathématique",
        "écoles": "Université Nationale du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Master"
      },
      {
        "filière": "Ingénierie Statistique",
        "écoles": "Université Nationale du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Doctorat"
      }
    ]
  },
  {
    "type": "Parcours Normal",
    "formations": [
      {
        "filière": "Mathématiques et Informatique",
        "écoles": "Université de Parakou - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Licence"
      },
      {
        "filière": "Statistique et Mathématique",
        "écoles": "Université de Parakou - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Master"
      },
      {
        "filière": "Ingénierie Statistique",
        "écoles": "Université de Parakou - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Doctorat"
      }
    ]
  },
  {
    "type": "Parcours Privé",
    "formations": [
      {
        "filière": "Mathématiques et Informatique",
        "écoles": "Université Privée du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Licence"
      },
      {
        "filière": "Statistique et Mathématique",
        "écoles": "Université Privée du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Master"
      },
      {
        "filière": "Ingénierie Statistique",
        "écoles": "Université Privée du Bénin - Faculté des Sciences et Techniques",
        "domaine": "Statistique et Mathématique",
        "niveau": "Doctorat"
      }
    ]
  }
]

