SELECT name, date(from_unixtime(cast(time_nano as double) / 1e9)) as date, SUM(CAST(measurement_pm100atmo as DOUBLE)*CAST(no_of_people_visited as INT)) as pollution_total_visitor
FROM my_db_nt_levi9.pollution
GROUP BY 1, 2
ORDER BY 1