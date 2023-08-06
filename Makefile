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
migrations:
	docker compose -f docker-compose.dev.yml run python ./manage.py makemigrations
rm:
	docker rm `docker ps -a -q`
rmi:
	docker rmi `docker images -a -q`
all_clear:
	docker compose -f docker-compose.dev.yml down
	docker volume rm profilee.db.volume
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc" -delete
