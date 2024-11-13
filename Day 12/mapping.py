import sqlalchemy
from sqlalchemy import create_engine, MetaData, Column,Integer,String,Float,Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from  sqlalchemy import inspect

engine = create_engine('sqlite:///company_orm1.db')
Base = sqlalchemy.orm.declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer,Sequence('employee_id_seq'),primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    department = Column(String(50))
    salary = Column(Float)


metadata = MetaData()
metadata.reflect(bind=engine)

employees = metadata.tables['employees']
Base.metadata.create_all(engine)

inspector = inspect(engine)
columns = inspector.get_columns('employees')

print("Table Details : ")
for column in columns:
    print(f"Column : {column['name']} - Type:{column['type']}")

Session = sessionmaker(bind=engine)
session = Session()

employees= [
    Employee(name = 'A', age=30, department= 'HR', salary=7000),
    Employee(name = 'B', age=24, department= 'IT', salary=8000),
    Employee(name = 'C', age=40, department= 'Finance', salary=9000)
]

session.add_all(employees)
session.commit()


all_employees =  session.query(Employee).all()
for emp in all_employees:
    print(f'{emp.id}:{emp.name}-{emp.department}-${emp.salary}')

employee_to_update = session.query(Employee).filter_by(name='A').first()
employee_to_update.salary = 7000
session.commit()

