build:
	docker compose -f docker-compose.dev.yml build
up:
	docker compose -f docker-compose.dev.yml up -d
down:
	docker compose -f docker-compose.dev.yml down
stop:
	docker compose -f docker-compose.dev.yml stop
migrate:
	docker compose -f docker-compose.dev.yml run python ./manage.py migrate
rm:
	docker rm `docker ps -a -q`
rmi:
	docker rmi `docker images -a -q`
