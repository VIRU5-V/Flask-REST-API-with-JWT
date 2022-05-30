# Flask REST API with JWT

to run this project open your terminal and write these commands:
```

python -m venv venv
venv\Scripts\activate.bat

```

Linux
```

source venv/bin/activate

```

```

pip install -r requirements.txt

```

Windows
```


set FLASK_APP=auth_app.py
set FLASK_DEBUG=1 #optional
set SECRET_KEY=SECRET_KEY
set MONGO_DB=MONGO_DB
set MONGO_USERNAME=MONGO_USERNAME
set MONGO_PASSWORD=MONGO_PASSWORD
set MONGO_CLUSTER = your mongo cluster name
set MONGO_CLUSTER_ID = your cluster id

```

Linux
```

export FLASK_APP=auth_app.py
export FLASK_DEBUG=1 #optional
export SECRET_KEY=SECRET_KEY
export MONGO_DB=MONGO_DB
export MONGO_USERNAME=MONGO_USERNAME
export MONGO_PASSOWORD=MONGO_PASSOWORD
export MONGO_CLUSTER = your mongo cluster name
export MONGO_CLUSTER_ID = your cluster id

```

flask run
```
Done

```

API Routes
```

1.Register
    
    URL : /register
    Method : POST
    Headers : {
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                first_name : 'lead_test@subi.com',
                last_name : '123456'.
                email : 'lead_test@subi.com',
                password : '123456'
              }


2 Login

    URL : /login
    Method : POST
    Headers : {
                 'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                email : 'lead_test@subi.com',
                password : '123456'
              }  

    
    2 Template CRUD
    
    1.Insert new Template

    URL : /template

    Method : POST
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
                     }  

    2.Get All Template

    URL : /template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}      


    3.GET Single Template

    URL : /template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  

    2.Update Single Template

    URL : /template/<template_id>
    
    Method : PUT
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
    }   

    3.DELETE Single Template

    URL : /template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}                  




```
