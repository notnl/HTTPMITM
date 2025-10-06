#!/usr/bin/env bash


if [ "$1" -eq 1 ]; then
	docker-compose up --no-deps --build sslcapture


fi


if [ "$1" -eq 2 ]; then
	docker compose build
	docker compose up


fi


if [ "$1" -eq 3 ]; then

	SAVE_HASH=$(docker build -q .)

	echo $SAVE_HASH

	docker run --rm -p 443:443 -it $SAVE_HASH

	docker rmi $SAVE_HASH
fi
