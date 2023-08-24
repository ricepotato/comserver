init:
	poetry build
	docker build -t comserver:latest .
