# SLA & Anomaly Intelligence

Synthetic operations-ticket analytics project using SQL and Python to evaluate SLA performance, queue health and abnormal resolution times.

## Analysis included

- Resolution-time calculation
- SLA breach rate
- Reopen rate
- Team × priority performance
- IQR-based resolution-time anomaly detection

## Run locally

```bash
pip install -r requirements.txt
python src/generate_data.py
python src/analyze.py
```

The SQL example in `sql/analysis.sql` is written in PostgreSQL-compatible syntax and derives resolution time directly from the generated timestamps.

## Data policy

Synthetic dataset only. No employer, client or production ticket data is used.
