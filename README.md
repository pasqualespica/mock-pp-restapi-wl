# mock-pp-restapi-wl

- [mock-pp-restapi-wl](#mock-pp-restapi-wl)
  - [Prerequisites](#prerequisites)
  - [How2run mock PM_4_WL](#how2run-mock-pm_4_wl)

## Prerequisites

Install on your machine :

- [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)
- _OPTIONAL_ : [VScode]() with extensions [vscode-openapi](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi) and  [swagger-viewer](https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer
)


## How2run mock PM_4_WL

To start you should `clone` the current repo locally typing :

```
git clone https://github.com/pasqualespica/mock-pp-restapi-wl mock-pp-restapi-wl && cd $_
```

then create your [Virtual Environments](https://docs.python.org/3/tutorial/venv.html) typing :

```
python -m venv <MY_VENV_NAME>
```

after that, active it with :

```
. MY_VENV_NAME/bin/activate
```

> NOTE : to exit from _Virtual Environments_ use `deactivate`

then install all packages using `pip` passing `requirements.txt` dependencies files :

```
pip install -r requirements.txt
```

and finally to get started the mock server :

```
python svr_pp-restapi-wl.py 
```

it's all rights you should see something like that :

```
 * Serving Flask app "svr_pp-restapi-wl" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
```

indicates that the server is listening on `localhost:5000` on the end points specified into `swagger_wl.yml`.


> NOTE : the `postman_ex` folder contains example calls using with [postman](https://www.postman.com/)


