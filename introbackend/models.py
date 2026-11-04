from sqlmodel import Field , SQLModel

class Company(SQLModel, table=True):
        compid: int | None = Field(default=None, primary_key=True)
        name: str
        dept: str
        age: int | None = None
        branch: str


class Driver(SQLModel, table=True):
    drivid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None
    salary: int | None = None


class Car(SQLModel, table=True):
    carid: int | None = Field(default=None, primary_key=True)
    name: str
    dept: str
    age: int | None = None
    car_model: str
