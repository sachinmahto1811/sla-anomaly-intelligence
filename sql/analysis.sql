-- PostgreSQL-compatible example.
-- Derive resolution_hours from the generated created_at / resolved_at timestamps.

WITH ticket_metrics AS (
    SELECT
        ticket_id,
        team,
        priority,
        reopened,
        sla_hours,
        EXTRACT(EPOCH FROM (resolved_at - created_at)) / 3600.0 AS resolution_hours
    FROM tickets
)
SELECT
    team,
    priority,
    COUNT(*) AS ticket_count,
    AVG(resolution_hours) AS avg_resolution_hours,
    AVG(CASE WHEN resolution_hours > sla_hours THEN 1.0 ELSE 0.0 END) AS sla_breach_rate,
    AVG(reopened * 1.0) AS reopen_rate
FROM ticket_metrics
GROUP BY team, priority
ORDER BY team, priority;
