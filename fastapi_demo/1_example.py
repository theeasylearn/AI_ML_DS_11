from fastapi import FastAPI

#create app object
app = FastAPI(title='1st example',version='1.0.0')

#create route/pat
#  http://127.0.0.1:8000
@app.get("/")
def home():
    return {"home":'api has been started successfully'}

# http://127.0.0.1:8000/product
@app.get("/product")
def product():
    return [{'name':'IPhone','price':180000},
            {'name':'macbook air','price':125000},
            {'name':'IPod','price':80000},
            {'name':'IPad','price':99000}
            ]

@app.get("/service")
# http://127.0.0.1:8000/service
def service():
    return [
            {'name':'Web site development','price':55000},
            {'name':'mobile app development','price':75000},
            {'name':'Machine learning model development','price':155000},
        ]

# to run then command
#fastapi dev 1_example.py
# or 
#fastapi run 1_example.py