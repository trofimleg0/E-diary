# Scripts for working with the E-diary database #

The website of the electronic diary is an interface for school students. Here you can see the grades, schedule and other open information. Teachers fill in the database through another website. They put grades there, etc.

### How to install ### 

Python should be already installed.  

Copy the repository of E-diary and go to the created directory
```commandline
git clone https://github.com/devmanorg/e-diary/tree/master
```

Use `pip`(or `pip3` for Python3) to install dependencies:
```commandline
pip3 install -r requirements.txt
```
Recommended using [virtualenv/venv](https://docs.python.org/3/library/venv.html)

## Launch ##

1. Run the server
```
python3 manage.py runserver
```

2. Open Django shell
```
python3 manage.py shell
```

3. Copy the contents of the file scripts.py and paste it into the console

## Description of scripts ##

**fix_marks**

The script corrects all the student's bad grades. Example:
```
fix_marks('Фролов Иван Григорьевич')
```

**remove_chastisements**

The script deletes all the student's comments.Example:
```
remove_chastisements('Фролов Иван Григорьевич')
```

The script praises the student, randomly choosing praise from the prepared list.  
Input data: Student's full name and subject. Example:
```
create_commendation('Фролов Иван Григорьевич', 'Математика')
```
