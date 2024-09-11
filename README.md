## API de Recommandation de Parcours Étudiants

### Présentation

Cette API RESTful a pour objectif de fournir des recommandations de parcours d'études personnalisées aux étudiants, en fonction de leurs critères de recherche (niveau d'étude, spécialité, matières préférées, métier, passion). Les résultats sont catégorisés (Excellent, Ecole publique, Ecole privée, Classique) et sont alimentés par une IA avancée.

### Fonctionnalités

* **Recommandations personnalisées:** L'API retourne des parcours d'études adaptés au profil de chaque étudiant.
* **Catégorisation des résultats:** Les parcours sont classés en différentes catégories pour faciliter la prise de décision.
* **Intégration avec un agent IA:** L'API s'appuie sur une IA sophistiquée pour effectuer des recherches approfondies et fournir des résultats pertinents.

### Points d'entrée (Endpoints)

#### **GET /parcours**
* **Paramètres:**
  * `niveau`: Niveau d'étude (bac, licence, master, etc.)
  * `specialite`: Spécialité souhaitée
  * `matieres`: Liste de matières préférées (séparées par des virgules)
  * `metier`: Métier visé
  * `passion`: Passion ou intérêt particulier
* **Réponse:** Un tableau de parcours, chaque parcours étant un objet JSON avec les propriétés suivantes :
  * `category`: Catégorie du parcours (Excellent, Ecole publique, etc.)
  * `formations`: Tableau de formations, chaque formation étant un objet JSON avec les propriétés suivantes :
    * `niveau`: Niveau d'étude
    * `filiere`: Filière
    * `ecoles`: Liste d'écoles
    * `domaine`: Domaine d'étude
    * `description`: Description détaillée du parcours

**Exemple de réponse:**

```json
[
  {
    "category": "Excellence",
    "formations": [
      {
        "niveau": "Licence",
        "filiere": "Licence statistique",
        "ecoles": [
          "African School of Economics",
          "Ecole Nationale d'Economie "
        ],
        "domaine": "Statistiques & Economie",
        "description": null
      }
    ]
  },
  {
    "category": "Ecole privée",
    "formations": [
      {
        "niveau": "Licence",
        "filiere": "Licence statistique",
        "ecoles": [
          "African School of Economics",
          "Ecole Nationale d'Economie "
        ],
        "domaine": "Statistiques & Economie",
        "description": null
      }
    ]
  }
]
