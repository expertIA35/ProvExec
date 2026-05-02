import json
import time
from datetime import datetime
from pathlib import Path

class ProvenanceTracker:
    def __init__(self):
        self.events = []
    
    def record(self, event_type, file_path):
        self.events.append({
            "event": event_type,
            "file": file_path,
            "timestamp": datetime.now().isoformat()
        })
    
    def save(self, output_file="outputs/provenance.json"):
        Path("outputs").mkdir(exist_ok=True)
        with open(output_file, "w") as f:
            json.dump({
                "events": self.events,
                "total_events": len(self.events)
            }, f, indent=2)
        print(f"✅ Provenance sauvegardée: {len(self.events)} événements")

def start_trace():
    print("🔍 Capture de provenance active")
    return ProvenanceTracker()
