CREATE TABLE users (
user_id SERIAL PRIMARY KEY,
user_name VARCHAR(25),
is_available BOOLEAN DEFAULT true 
);
CREATE TABLE saved_equations (
equation_id SERIAL PRIMARY KEY,
equation_name VARCHAR(75),
modification_date TIMESTAMP VARCHAR(100),
has_graph REFERENCES saved_graphs(graph_id) BOOLEAN DEFAULT false
);
-- CREATE TABLE saved_graphs (
-- graph_id SERIAL PRIMARY KEY,
-- is_a_graph BOOLEAN NOT NULL,
-- modification_date TIMESTAMP VARCHAR(100)
-- );
