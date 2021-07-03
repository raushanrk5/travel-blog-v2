# travel-blog-v2
Check demo at:
```
https://raushanrk.pythonanywhere.com/
```

Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/raushanrk5/travel-blog-v2.git
```
Create a virual envronment and activate it using
```
virtualenv env
source env/bin/activate
```
Install Dependencies 

```
pip install -r requirements.txt
```

Set Database (Make Sure you are in directory same as manage.py)
```
python manage.py makemigrations
python manage.py migrate
```
Create SuperUser 
```
python manage.py createsuperuser
```

After all these steps , you can start testing and developing this project. 
