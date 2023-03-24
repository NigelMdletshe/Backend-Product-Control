#***(1) Returns all customers from the database.***
customers = Customer.objects.all()

#***(2) Returns first customer in table .***
firstCustomer = Customer.objects.first()

#(3) Returns last customer in table
lastCustomer = Customer.objects.last()

#(4)Returns single customer by name
customerByName = Customer.objects.get(name='John Doe')

#(5)Returns single customer by id
customerById = Customer.objects.get(id=1)

#(6)Returns all orders related to a customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)Returns all orders related to a customer (Querry parent model values)
order = Order.objects.first()
parentName = order.customer.name

#(8)Returns products from products table with value of "Out Door" in category attribute 
products = Product.objects.filter(category='Out Door')

#(9)Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

#(10)Returns all products with tag "Sports":(Querry Many to Many fields)
productsFiltered = Product.objects.filter(tags__name='Sports')

