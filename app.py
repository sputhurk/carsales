from flask import Flask, jsonify, render_template, request,url_for,redirect
from database import load_inventory,add_cars,delete_car,load_customers,updateCustomer
print ("hello")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    #return 'index.html'
######################################
# Route for customer link from the main the page.
@app.route('/customer')
def customer():
    #return 'index.html'
    items = load_customers(-1)
    print(type(items),"YYYYY")
    print (items)
    return render_template('customer.html',items=items)

###################################
@app.route('/customerinfo/<id>')
def customer_info(id):
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]

    items= load_customers(id)
    return render_template('cust_info.html',item=items[0]) ## to get the dictiory
    #return 'index.html'

###################################
## For Customer ADD/Update
@app.route('/cust_maint',methods=['GET', 'POST'])
def add_customer() :

    if request.method == 'POST':
      # Handle POST request
      # Get the values from the submitted forms
      # make, model,year, price
      customer = request.form.to_dict();
      #print (new_car)
      updateCustomer(customer)
      return render_template('cust_maint.html')
    else:
      # Handle GET request
      return render_template('cust_maint.html')
################################

@app.route('/cust_maint/<id>',methods=['GET', 'POST'])
def edit_customer(id):

      if request.method == 'POST':
        # Handle POST request
        # Get the values from the submitted forms
        # make, model,year, price
        customer = request.form.to_dict();
        #print (new_car)
        updateCustomer(customer)
        return render_template('add_car.html')
      else:
        # Handle GET request
        items= load_customers(id)
        print ("XXXXXX")
        #print (car)
        
        return render_template('cust_maint.html',thisCar=items[0])

@app.route('/purchase',methods=['GET', 'POST'])
def add_car() :

    if request.method == 'POST':
      # Handle POST request
      # Get the values from the submitted forms
      # make, model,year, price
      new_car = request.form.to_dict();
      #print (new_car)
      add_cars(new_car)
      return render_template('add_car.html')
    else:
      # Handle GET request
      return render_template('add_car.html')
@app.route('/purchase/<id>',methods=['GET', 'POST'])
def edit_car(id) :

      if request.method == 'POST':
        # Handle POST request
        # Get the values from the submitted forms
        # make, model,year, price
        new_car = request.form.to_dict();
        #print (new_car)
        add_cars(new_car)
        return render_template('add_car.html')
      else:
        # Handle GET request
        car= load_inventory(id)
        print ("XXXXXX")
        print (car)
        
        return render_template('add_car.html',thisCar=car[0])

@app.route('/inventory')
def inventory():
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]
    ## -1 means no parameter to load inventory table.
    items = load_inventory(-1)
    print(type(items),"YYYYY")
    print (items)
    return render_template('inventory.html',items=items)
    #return 'index.html'
@app.route('/api/inventory')
def api_inventory():
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]
    ## -1 means no parameter to load inventory table.
    items= load_inventory(-1)
    print (type(items))
    return jsonify(items)
    
    #return 'index.html'
@app.route('/delete/<id>')
def deletecar(id):
    delete_car(id)
    items= load_inventory(-1)
    return redirect(url_for('inventory'))

@app.route('/inventory/<id>')
def show_car(id):
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]

    items= load_inventory(id)
    return render_template('inventory.html',items=items)
    #return 'index.html'

@app.route('/carinfo/<id>')
def car_info(id):
    #items =[

    #  {'id':1, 'name':'ford',   'year':2024, 'price':1000},
    #  {'id':2, 'name':'tesla',  'year':2022, 'price':1000},
    #  {'id':3, 'name':'toyota', 'year':2025, 'price':1020}
    #]

    items= load_inventory(id)
    return render_template('carinfo.html',item=items[0]) ## to get the dictiory
    #return 'index.html'


if (__name__ == '__main__'):
  app.run(host="0.0.0.0", port=5000,debug=True)