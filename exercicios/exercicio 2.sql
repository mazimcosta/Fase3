SELECT first_name,
last_name,
email
FROM
customer
WHERE last_name LIKE 'S%' and active=1