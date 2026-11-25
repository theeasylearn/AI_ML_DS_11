from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#create app object
app = FastAPI(title='2nd example',version='1.0.0')

# Schema for request body
class Product(BaseModel):
    name: str
    price: str | int

class ProductUpdate(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[str | int] = None

list = [ 
            {'id':1,'name':'IPhone','price':180000},
            {'id':2,'name':'macbook air','price':125000},
            {'id':3,'name':'IPod','price':80000},
            {'id':4,'name':'IPad','price':99000}
        ]
next_id = 5
#create route/pat
#  http://127.0.0.1:8000

@app.get("/")
def home():
    return {"home": 'api has been started successfully'}

#  http://127.0.0.1:8000/product
@app.get("/product")
def product():
    return list

#  http://127.0.0.1:8000/product
@app.post("/product")
def add(product: Optional[Product] = None, name: Optional[str] = None, price: Optional[str | int] = None):
    global next_id
    # Support both JSON Body and Query parameters
    prod_name = product.name if product else name 
    prod_price = product.price if product else price

    if not prod_name or prod_price is None:
        return {"error": "Missing required fields: 'name' and 'price' must be provided in JSON body or as query parameters"}

    new_product = {'id': next_id, 'name': prod_name, 'price': prod_price}
    list.append(new_product)
    next_id += 1
    return {"message": "Product added successfully", "product": new_product}

@app.put("/product")
def update(
    product: Optional[ProductUpdate] = None,
    name: Optional[str] = None,
    price: Optional[str | int] = None,
    id: Optional[int] = None
):
    # Support both JSON Body and Query parameters
    prod_id = product.id if (product and product.id is not None) else id
    prod_name = product.name if (product and product.name is not None) else name 
    prod_price = product.price if (product and product.price is not None) else price

    if prod_name is None or prod_price is None or prod_id is None:
        return {"error": "Missing required fields: 'name' and 'price' and 'id' must be provided in JSON body or as query parameters"}
    
    for i in range(len(list)):
        if list[i]['id'] == prod_id:
            new_product = {'id': prod_id, 'name': prod_name, 'price': prod_price}
            list[i] = new_product      
            return {"message": "Product updated successfully"}
    return {"message": "Product not found"}

# to run then command
#fastapi dev 2_methods.py
# or 
#fastapi run 2_methods.py

