# BCF Manager
##Powered by Django, DRF, and VueJS

### Purpose

Django BCF Manager purpose is to give web tools for managing BCF files. 
BCF is a format for managing issues on a BIM project. 

For more information about this format see https://github.com/buildingSMART/BCF-XML. 
API is documented here: https://github.com/buildingSMART/BCF-API

### Features roadmap 

- Load bcfzip file into dedicated django model
- Provide managing tools to visualize/manipulate issues
- Re-export model data to bcfzip (with custom filters)
- Implement BCF-API to remotely manipulate data according to BCF-API specification

- Might try to link this to a bimserver someday (see https://github.com/opensourceBIM/BIMserver)

### quickstart for developpers

```
$ git clone path_to_repostery/django-bcf-manager 
$ cd  django-bcf-manager
$ pip install -r requirements.txt 
$ python manage.py collectstatic --noinput
$ python manage.py migrate  
$ cd frontend 
$ npm install
$ npm run dev 
$ cd .. 
$ python manage.py runserver
```

You should then have 

vuecli app running  at http://localhost:8080/
django app running at http://localhost:8000/ 


