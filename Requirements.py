To use the code, follow these steps:

pip3 install haversine # to compute distances between two points on a sphere
wget https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat
wget https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat -O flights.dat
python3 dijkstra.py

