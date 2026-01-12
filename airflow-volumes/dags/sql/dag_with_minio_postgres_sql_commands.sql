--- create public.orders table then exports the CSV file in the table
CREATE TABLE IF NOT EXISTS public.orders (
  order_id VARCHAR,
  date DATE,
  product_name VARCHAR,
  quantity INTEGER,
  primary key (order_id)
);

--- show the first 5 lines
SELECT * FROM public.orders LIMIT 5;

--- show the number of inserted rows in the table 
SELECT COUNT(*) FROM public.orders;