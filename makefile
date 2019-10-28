#all about development
shell:
	docker-compose -f dev.yml exec spacesrental bash


# all about testing
test_dev:
	docker-compose -f test.yml rm -f
	echo $(app)
	docker-compose -f test.yml build
	docker-compose -f test.yml  run spacesrentaltest python manage.py test $(app)
	exit 0



#all about production
gen_static:
	sudo docker-compose -f prod.yml run spacerental_prod python manage.py collectstatic --no-input
	exit 0

makemigration:
	sudo docker-compose -f prod.yml run spacerental_prod python manage.py makemigrations
	exit 0

migrate:
	sudo docker-compose -f prod.yml run spacerental_prod python manage.py migrate
	exit 0
