SELECT
  team,
  priority,
  COUNT(*) AS ticket_count,
  AVG(resolution_hours) AS avg_resolution_hours,
  AVG(CASE WHEN resolution_hours > sla_hours THEN 1.0 ELSE 0 END) AS sla_breach_rate,
  AVG(reopened) AS reopen_rate
FROM tickets
GROUP BY team, priority
ORDER BY team, priority;
