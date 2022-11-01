-- script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
SELECT city, AVG(temperature) AS avg_temp FROM temperatures ORDER BY avg_temp DESC GROUP BY city;
