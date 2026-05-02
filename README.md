# ProvExec – Conteneur exécutable avec provenance intégrée
Un conteneur Docker qui exécute une expérience scientifique et capture **automatiquement** la provenance des fichiers créés.


 État de l'art

| Outil / Recherche | Fonction | Limite |
|-------------------|----------|--------|
| **Belloum et al. (2014)** – Génération de documentation à partir de la provenance | Capture la provenance pour des workflows scientifiques | Pas de conteneur exécutable |
| **REPRO-Agent (Hu et al., 2025)** – Évaluation automatisée de la reproductibilité | Exécute le code pour tester | Lent, pas de provenance intégrée |
| **RSEMM (Wageningen, 2025)** – Dashboard de maturité logicielle | Évalue la qualité du code | Pas de capture de provenance |
| **FAIR-IMPACT (Europe, 2025)** – Métriques FAIR pour logiciels | Évalue la découvrabilité | Pas d'exécution ni de provenance |

---

 Référence principale

Belloum, A., et al. (2014)** – *Generating Scientific Documentation for Computational Experiments Using Provenance.*  
→ Ce projet prolonge ce travail en ajoutant :
- Un **conteneur Docker exécutable** (reproductible)
- Une **provenance au format JSON** (interopérable)
- Un **export simple** pour la science ouverte



 Architecture technique
┌─────────────────────────────────────────────────────────────────────────────┐
│                              PROVEXEC - ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐                                                            │
│  │ UTILISATEUR │                                                            │
│  └──────┬──────┘                                                            │
│         │ python orchestrator.py                                           │
│         ▼                                                                    │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         COUCHE ORCHESTRATION                          │   │
│  │  ┌────────────────────────────────────────────────────────────────┐  │   │
│  │  │                      orchestrator.py                            │  │   │
│  │  │  - Création des données (data/sample.csv)                      │  │   │
│  │  │  - Lancement de la capture                                     │  │   │
│  │  │  - Exécution du pipeline                                       │  │   │
│  │  │  - Sauvegarde des résultats                                    │  │   │
│  │  └────────────────────────────────────────────────────────────────┘  │   │
│  └────────────────────────────────────┬─────────────────────────────────┘   │
│                                       │                                      │
│                                       ▼                                      │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         COUCHE PROVENANCE                             │   │
│  │  ┌────────────────────────────────────────────────────────────────┐  │   │
│  │  │                      provenance.py                              │  │   │
│  │  │  ┌──────────────────────────────────────────────────────────┐  │  │   │
│  │  │  │              ProvenanceTracker                            │  │  │   │
│  │  │  │  - __init__() : events = []                              │  │  │   │
│  │  │  │  - record()   : ajoute un événement                      │  │  │   │
│  │  │  │  - save()     : exporte provenance.json                  │  │  │   │
│  │  │  └──────────────────────────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────────────────────────┘  │   │
│  └────────────────────────────────────┬─────────────────────────────────┘   │
│                                       │                                      │
│                                       ▼                                      │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                         COUCHE STOCKAGE                               │   │
│  │                                                                       │   │
│  │   ┌─────────────────┐      ┌─────────────────────────────────────┐   │   │
│  │   │   DONNÉES       │      │            SORTIES                   │   │   │
│  │   ├─────────────────┤      ├─────────────────────────────────────┤   │   │
│  │   │ data/           │      │ outputs/                            │   │   │
│  │   │ └── sample.csv  │      │ ├── resultat.txt (résultat)         │   │   │
│  │   └─────────────────┘      │ └── provenance.json (traçabilité)   │   │   │
│  │                            └─────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

Valeur ajoutée (par rapport à l'existant)

| Problème actuel | Solution de ProvExec |
|----------------|----------------------|
| Les outils de provenance (Belloum 2014) ne sont pas embarqués dans un conteneur exécutable | ✅ Conteneur Docker prêt à l'emploi |
| REPRO-Agent (2025) est lent car exécute le code | ✅ ProvExec capture **sans exécuter** le code |
| RSEMM et FAIR-IMPACT ne capturent pas la provenance | ✅ Fichier `provenance.json` généré automatiquement |
| Aucun outil ne combine reproductibilité ET traçabilité | ✅ **Premier** à fusionner les deux |

**En une phrase :**  
*ProvExec est le premier outil qui rend une expérience scientifique à la fois **reproductible** (conteneur) et **traçable** (provenance).*


 Auteur 
 chawki FARES 
 IMT Sud – Master IA
 Lien
https://github.com/expertIA35/ProvExec
