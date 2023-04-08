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
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This is an R&D Project for connecting [Django](https://www.djangoproject.com) & [Django Rest](https://www.django-rest-framework.org) framework to a [postgresql](https://www.postgresql.org/docs/15/index.html) database.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them.

Basic Python Virtual Environments with mentioned in about frameworks

### Installing

A step by step series of examples that tell you how to get a development env running.

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

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
```

## 🎈 Usage <a name="usage"></a>

Add notes about how to use the system.

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

- [MongoDB](https://www.mongodb.com/) - Database
- [Express](https://expressjs.com/) - Server Framework
- [VueJs](https://vuejs.org/) - Web Framework
- [NodeJs](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

- [@momin-mostafa](https://github.com/momin-mostafa) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
