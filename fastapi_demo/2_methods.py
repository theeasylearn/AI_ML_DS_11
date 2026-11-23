from fastapi import FastAPI

#create app object
app = FastAPI(title='2nd example',version='1.0.0')
list = [ 
            {'id':1,'name':'IPhone','price':180000},
            {'id':2,'name':'macbook air','price':125000},
            {'id':3,'name':'IPod','price':80000},
            {'id':4,'name':'IPad','price':99000}
        ]
next_id = 5
#create route/pat
#  http://127.0.0.1:8000
@app.get("/product")
def home():
    return list

@app.post("/product/add")
def add(name :str, price :str):
    new_product = {'id':next_id,'name':name,'price':price}
    list.append(new_product)


# to run then command
#fastapi dev 2_methods.py
# or 
#fastapi run 2_methods.py

