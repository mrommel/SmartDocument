# project creation

django-admin startproject smartdocument

cd smartdocument
python manage.py startapp data

# change admin password

python manage.py changepassword admin
fordocument


# data migration

python manage.py makemigrations data
python manage.py sqlmigrate data 0002
python manage.py migrate


# template
http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/pages/index.html
https://github.com/flot/flot/blob/master/examples/basic-options/index.html