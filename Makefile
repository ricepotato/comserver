init:
	poetry build
	docker build --no-cache -t comserver:$(shell poetry version -s) .
