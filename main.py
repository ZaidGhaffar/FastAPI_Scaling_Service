from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

user = ["Zaid","Zubair","Zoha","Zohad"]


class data(BaseModel):
    name: str
    upuntil: int


app = FastAPI(version='1.0')


# decorator
@app.get('/user') # Whenever this decorator is called inside of the browser the func below it is auto called
def main():
    return "Hello World!!!"


@app.get('/user/{user_id}') # path parms
def get_main(user_id: int): # this will be treating Everything as str so with type hinting Fastapi auto converts it From str to int withput you manually doing the work
    return user[user_id]    

@app.get('/person') # Query Parms 
def func1(age: int):
    return user[age]



    
@app.post('/getting_data')# So it you don't pass the Pydantic model and give it a try the Fastapi auto Converts it into the Query Parms not the Request Body 
def func2(name: data): # without defining the pydantic model the fastapi is Never able to read the Request body it is still seeing it as Query parms so When you tell the fastapi it's pydantic model Here's what happen
    # 1. user send the data 
    # 2. fastapi looks at you're func and see it is excpecting specific type of data the Fastapi will auto read it from the Request body as Json 
    # 3. it than pass the json to pydantic  to convert from Json to Python 
    # 4. it than stores the result in the func params to use it inside of the func
    return user[name.upuntil]


if __name__ == "__main__":
    uvicorn.run("main:app",host='localhost',port=8080,reload=True)