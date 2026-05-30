SELECT store_id,
Count(customer_id) as total_clientes
FROM customer
group by store_id