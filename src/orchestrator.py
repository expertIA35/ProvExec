import time
from pathlib import Path
from provenance import start_trace

def run_experiment():
    print("🚀 ProvExec - Démarrage de l'expérience")
    
    Path("data").mkdir(exist_ok=True)
    with open("data/sample.csv", "w") as f:
        f.write("valeur1,valeur2\n1,2\n3,4")
    
    tracker = start_trace()
    
    print("📝 Traitement des données...")
    time.sleep(1)
    tracker.record("created", "data/sample.csv")
    
    with open("outputs/resultat.txt", "w") as f:
        f.write("Résultat de l'expérience")
    tracker.record("created", "outputs/resultat.txt")
    
    tracker.save()
    print("✅ Expérience terminée")

if __name__ == "__main__":
    run_experiment()
