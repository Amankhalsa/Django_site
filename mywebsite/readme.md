# This is a Django website  project 
# Added manually
  * 'DIRS': [os.path.join(BASE_DIR,'templates')],
  
  * STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static") ]
  
  * python manage.py collectstatic
  * in head tag add below 
    * {% load static %}
========================================
	for style sheet in link tag add this 
========================================
* <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
* 1st open setting add app name 
========================================
* INSTALLED_APPS['myapp']


