from pathlib import Path
import random
from datetime import datetime, timedelta
import pandas as pd

random.seed(42)
sla = {"P1":4,"P2":8,"P3":24,"P4":48}
rows = []
start = datetime(2026,1,1)
for i in range(3500):
    priority = random.choice(list(sla))
    created = start + timedelta(hours=random.randint(0, 24*180))
    base = {"P1":3,"P2":6,"P3":18,"P4":32}[priority]
    resolution = max(0.2, random.gammavariate(2, base/2))
    rows.append({
        "ticket_id": f"T{i+1:05d}",
        "team": random.choice(["Ops-A","Ops-B","Ops-C"]),
        "priority": priority,
        "created_at": created,
        "resolved_at": created + timedelta(hours=resolution),
        "reopened": int(random.random() < 0.08),
        "sla_hours": sla[priority]
    })

Path("data").mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv("data/tickets.csv", index=False)
print("Synthetic ticket dataset created.")
