SELECT rating,
count(rating) as total
From film
Group by rating