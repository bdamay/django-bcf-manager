# BCF Manager
## Powered by Django, DRF 

*This project is just starting. Don't expect its functionnality to be complete*

### Purpose

Django BCF Manager purpose is to give web tools for managing BCF files. 
BCF is a format for managing issues on a BIM project. 

For more information about this format see https://github.com/buildingSMART/BCF-XML. 
API is documented here: https://github.com/buildingSMART/BCF-API

### Targeted features  - roadmap 

- Load bcfzip files into dedicated django model (V2.0 V2.1)
- Provide managing tools to visualize/manipulate/merge issues from different sources
- Export model data to bcfzip (with custom filters) 
- Implement BCF-API with DRF to remotely manipulate data according to BCF-API specification

- Might try to link to an ifc hosted on a bimserver someday (see https://github.com/opensourceBIM/BIMserver)

### quickstart for developpers

```
$ git clone https://github.com/bdamay/django-bcf-manager.git
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

### Notes 

Repository provides the full django project in myproject folder, it might not suit your needs. 
You can of course use your project instead and keep only the django app and frontend. 
Make sure you provide correct information into your setting files mostly regarding webpackloader ans VueJS.

### Deploiement 

TODO
