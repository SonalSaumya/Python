import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine =create_engine('sqlite:///employees4.db', echo = True)
Base = sqlalchemy.orm.declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    salary= Column(Float, nullable=False)

def create_table():
    Base.metdata.create_all(engine)
    print("Table 'employees' created successfully.")

def insert_sample_data():
    Session = sessionmaker(bind=engine)
    session = Session()

    employees = [
       Employee(name='Mayura', position='Engineer', salary=70000),
       Employee(name='Mayuresh', position='Manager', salary=85000),
       Employee(name='Sugandha', position='Technician', salary=50000),
       Employee(name='Srujan', position='Analyst', salary=65000)
            ]

    session.add.all(employees)
    session.commit()
    session.close()
    print("Sample data inserted successfully.")

def read_data():
    df = pd.read_sql('employees', con=engine)
    return df

def update_salary(df,employee_id, new_salary):
    df.loc[df['employee_id'] == employee_id, 'salary'] = new_salary
    return df


def write_data(df):
    df.to_sql('employees', con=engine)
    print("Updated data written back to he database.")


def main():
    create_table()
    insert_sample_data()

    df = read_data()
    print("Original DataFrame:")
    print(df)

    df= update_salary(df,employee_id=2, new_salary=50000)
    print("\n Updated Dataframe:")
    print(df)

    write_data(df)
    print("\nData updated in the database.")

    df=read_data()
    print("Updates DataFrame:")
    print(df)

if __name__ == "--main__":
    main()

    