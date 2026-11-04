from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine

from models import Company, Driver, Car 

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/company/{id}")
async def read_company(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        comp = session.get(Company, id)
        return {"message": comp}
    

@app.post("/company")
async def root(company  : Company):
    with Session(engine) as session:
        session.add(company)
        session.commit()
        session.refresh(company)

        return {"message": 'created'}


@app.get("/driver/{id}")
async def read_driver(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        comp = session.get(Driver, id)
        return {"message": driv}
    

@app.post("/driver")
async def root(driver  : Driver):
    with Session(engine) as session:
        session.add(driver)
        session.commit()
        session.refresh(driver)

        return {"message": 'created'}



@app.get("/car/{id}")
async def read_car(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        comp = session.get(Car, id)
        return {"message": car}
    


@app.post("/car")
async def root(car  : Car):
    with Session(engine) as session:
        session.add(car)
        session.commit()
        session.refresh(car)

        return {"message": 'created'}