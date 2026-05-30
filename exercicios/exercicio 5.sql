SELECT
customer_id,
amount,
payment_date
FROM
payment
ORDER BY amount desc
LIMIT 15