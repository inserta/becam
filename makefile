#all about development
shell:
	docker-compose -f dev.yml exec becam_dev bash


#all about production
# gen_static:
#	sudo docker-compose -f prod.yml run becam_prod python manage.py collectstatic --no-input
#	exit 0

# makemigration:
#	sudo docker-compose -f prod.yml run becam_prod python manage.py makemigrations
#	exit 0

# migrate:
#	sudo docker-compose -f prod.yml run becam_prod python manage.py migrate
#	exit 0
