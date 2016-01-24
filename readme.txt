# project creation

django-admin startproject smartdocument

cd smartdocument
python manage.py startapp data
python manage.py startapp forecast

# change admin password
python manage.py changepassword admin
fordocument

# data migration for data
python manage.py makemigrations data
python manage.py sqlmigrate data 0002
python manage.py migrate

# data migration for forecast
python manage.py makemigrations forecast
python manage.py sqlmigrate forecast 0002
python manage.py migrate

# template
http://ironsummitmedia.github.io/startbootstrap-sb-admin-2/pages/index.html
https://github.com/flot/flot/blob/master/examples/basic-options/index.html

#timeline
http://codepen.io/codyhouse/full/FdkEf/

# Zinsen
2015-07 23,00
2015-08 76,67
2015-09 76,67
2015-10 76,67
2015-11 76,67
2015-12 135,44