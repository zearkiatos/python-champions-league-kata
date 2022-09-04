docker-up:
	docker compose up --build -d
	docker exec -it python-champions-league-kata python interface_champions.py

docker-down:
	docker compose down