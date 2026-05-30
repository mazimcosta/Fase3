SELECT customer.customer_id,
customer.first_name,
customer.last_name,
count(payment.amount)
FROM customer
jOIN payment ON customer.customer_id=payment.customer_id
GROUP BY customer.customer_id
LIMIT 1