from sqlalchemy import create_engine,text
import datetime
import os
db_conn_string = os.environ['DB_CONN_STRING']
#db_conn_string ='mysql+pymysql://admin:tnt-projects#24@cars.cjw4gio06s5f.us-east-1.rds.amazonaws.com:3306/cars'
engine=create_engine(db_conn_string,connect_args={"ssl":  {"ssl_ca": "/etc/ssl/cert.pem"}}, echo=True)



#### This is to show the car inventort information for inventory.html
def load_customers(parid):
  result_dicts = []
  
  QryLine1 = """select m.id,name,c.address1,c.city,c.state,c.zip,c.mobile_phone,c.primary_email,c.active_flag
                FROM   customer_master  m,        
                       customer_contact c         
                where  m.id   = c.customer_id"""

  if int(parid) >0: 
     sqlqry = text(QryLine1 +" and m.id = :parid")
  else:
     sqlqry = text(QryLine1)
  print ("####################### -- customer query ######################")  
  print (sqlqry)    
  with engine.connect() as conn:
      if int(parid) >0:
         result = conn.execute(sqlqry,{"parid": parid})
      else:
         result = conn.execute(sqlqry)
      # Now feth the records from the result object.    
      for row in result.all():
          result_dicts.append(row._asdict())
  return result_dicts ## Always going to return a list of dicts.

#### This is to show the car inventort information for inventory.html
def load_inventory(parid):
  result_dicts = []
  
  if int(parid) >0: 
     sqlqry = text("select * from cars where id = :parid")
  else:
     sqlqry = text("select * from cars")
  print (sqlqry)    
  with engine.connect() as conn:
      if int(parid) >0:
         result = conn.execute(sqlqry,{"parid": parid})
      else:
         result = conn.execute(sqlqry)
      # Now feth the records from the result object.    
      for row in result.all():
          result_dicts.append(row._asdict())
  return result_dicts ## Always going to return a list of dicts.


############

def updateCustomer(parcustomer):
  # get the cars details from the form
  # crete a sql statement to save it to the database.
  # Check the value of the type (it could be Add or Edit)
  action = parcustomer["type"]
  if action == "Add":
    sql_stmt = text("insert into customer_master (name, active) values (:name, :active)")
  else:
    sql_stmt = text("update customer_master set name =:name, active=:active where id=:id" ) 
      
  print (parcustomer["name"])
  with engine.connect() as conn:
        if action == "Add":
            result = conn.execute(sql_stmt, {
                            "name"   : parcustomer["name"], 
                            "active" : parcustomer["active"]
                            })
            print(result.lastrowid)
            
            #for row in result.all():
          #result_dicts.append(row._asdict())
        else:
            result = conn.execute(sql_stmt, {
                            "name"  : parcustomer["make"], 
                            "active" : parcustomer["model"]
                            })
        conn.commit()
#########
## This is to add the cars into the cars table.
def add_cars(parnewcar):
  # get the cars details from the form
  # crete a sql statement to save it to the database.
  # Check the value of the type (it could be Add or Edit)
  action = parnewcar["type"]
  if action == "Add":
    sql_stmt = text("insert into cars (make, model,year, msrp) values (:make, :model, :year, :price)")
  else:
    sql_stmt = text("update cars set make =:make, model=:model, year=:year, msrp=:price where id=:id" ) 
      
  print (parnewcar["year"])
  with engine.connect() as conn:
        if action == "Add":
            result = conn.execute(sql_stmt, {
                            "make"  : parnewcar["make"], 
                            "model" : parnewcar["model"],
                            "year"  : parnewcar["year"], 
                            "price" : parnewcar["price"]})
        else:
            result = conn.execute(sql_stmt, {
                            "make"  : parnewcar["make"], 
                            "model" : parnewcar["model"], 
                            "year"  : parnewcar["year"], 
                            "price" : parnewcar["price"],
                            "id"    : parnewcar["id"]})
        conn.commit()
#########
## Function to remove the cars from the inventory table - cars.
def delete_car(parid):
    sqlqry = text("delete from cars where id = :parid")

    print (sqlqry)    
    with engine.connect() as conn:
        result = conn.execute(sqlqry,{"parid": parid})
        conn.commit()
   ## Always going to return a list of dicts.

## This is to add the cars into the cars table.