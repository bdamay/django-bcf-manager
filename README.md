# BCF Manager
## Powered by Django, DRF 

*This project is just starting. Don't expect its functionnality to be complete*

### Purpose

Django BCF Manager purpose is to give web tools for managing BCF files. 
BCF is a format for managing issues on a BIM project. 

For more information about this format see https://github.com/buildingSMART/BCF-XML. 
API is documented here: https://github.com/buildingSMART/BCF-API

### Targeted features  - roadmap 

- Load bcfzip files into dedicated django model (BCF V2.0 V2.1)
- Provide managing tools to visualize/manipulate/merge/add issues from different sources 
- Export model data to bcfzip (with custom filters) 
- Implement BCF-API with DRF to remotely manipulate data according to BCF-API specification (BCFServer)

- Provide links to an ifc hosted on a bimserver (see https://github.com/opensourceBIM/BIMserver)

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


For now access index of the django app, you need to be connected to a django account 
(you can use your supersuser account and connect via the admin login)

For now (2020 10 20), you can just load a bcf zip at /topic url and look at your issues that's pretty much it.
I'm working on next steps. 





### Notes 

Repository provides the full django project in "myproject" folder, it might not suit your needs. 
You can of course use your own project instead and keep only the django app and frontend or whatever you want to use. 
Make sure you provide correct information regarding webpackloader ans VueJS into your setting files if you want VueJS to work properly.

### Deploiement 

TODO
