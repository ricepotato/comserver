init:
	poetry build
	docker build --no-cache -t comserver:$(shell poetry version -s) .
	docker tag comserver:$(shell poetry version -s) ricepotato/comserver:$(shell poetry version -s)

push:
	docker push ricepotat/comserver:$(shell poetry version -s)