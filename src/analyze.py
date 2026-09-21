import pandas as pd

df = pd.read_csv("data/tickets.csv", parse_dates=["created_at","resolved_at"])
df["resolution_hours"] = (df["resolved_at"] - df["created_at"]).dt.total_seconds() / 3600
df["sla_breach"] = df["resolution_hours"] > df["sla_hours"]

q1 = df["resolution_hours"].quantile(.25)
q3 = df["resolution_hours"].quantile(.75)
upper = q3 + 1.5 * (q3-q1)
df["iqr_anomaly"] = df["resolution_hours"] > upper

summary = (df.groupby(["team","priority"], as_index=False)
             .agg(ticket_count=("ticket_id","count"),
                  avg_resolution_hours=("resolution_hours","mean"),
                  sla_breach_rate=("sla_breach","mean"),
                  reopen_rate=("reopened","mean"),
                  anomaly_count=("iqr_anomaly","sum")))
print(summary.to_string(index=False))
