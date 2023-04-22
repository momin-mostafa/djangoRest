<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://github.com/momin-mostafa/djangoRest/blob/django-rest-postgre-_r%26d_/image_readme/postgresql.jpg" alt="Project logo {Image_credit:https://www.pexels.com/@realtoughcandy/}"></a>
</p>

<h3 align="center">Django Rest Postgres R&D</h3>

<div align="center">
</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
<!-- - [Usage](#usage) -->
- [Built Using](#built_using)
<!-- - [Contributing](../CONTRIBUTING.md) -->
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This is an R&D Project for connecting [Django](https://www.djangoproject.com) & [Django Rest](https://www.django-rest-framework.org) framework to a [postgresql](https://www.postgresql.org/docs/15/index.html) database.

## 🏁 Getting Started <a name = "getting_started"></a>

will create a requirements.txt later

### Prerequisites

What things you need to install the software and how to install them.

Basic Python Virtual Environment, Django, Django Rest Framework

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
pip install django
```

for django rest frame work

```
pip install djangorestframework
```

<!-- End with an example of getting some data out of the system or using it for a little demo.

## 🔧 Running the tests <a name = "tests"></a>

Explain how to run the automated tests for this system.

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
``` -->

<!-- ## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system. -->

## 🚀 Deployment <a name = "deployment"></a>

```Bash
pip install django
pip install psycopg2
django-admin startproject myproject
cd myproject
```
Please change settings.py file change the database ENGINE string from sqlite3 to postgresql and add NAME, USER, PASSWORD, HOST and POST as keys to the default dictionary.

```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        #This Fields Needs To Be Customised.
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org) - Python
-  [Django](https://www.djangoproject.com) - Server
- [Django Rest](https://www.django-rest-framework.org) - Server Framework
- [Postgresql](https://www.postgresql.org/) - Database
<!-- - [VueJs](https://vuejs.org/) - Web Framework -->
<!-- - [NodeJs](https://nodejs.org/en/) - Server Environment -->

## ✍️ Authors <a name = "authors"></a>

- [@momin-mostafa](https://github.com/momin-mostafa) - Idea & Initial work
<!-- 
See also the list of [contributors](https://github.com/momin-mostafa/The-Documentation-Compendium/contributors) who participated in this project. -->

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
    https://www.youtube.com/@DennisIvy
