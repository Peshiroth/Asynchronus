import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]):
        self.customer_id = customer_id
        self.products = products

# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_take = {"id": cashier_number, "time": 0,"customer": 0}
    while not queue.empty():
        customer: Customer = await queue.get()
        cashier_take['customer'] += 1
        print(f"The cashier_{cashier_number}"
            f"Will checkout Customer_{customer.customer_id}")
        for product in customer.products:
            if cashier_number == 2:
                product.checkout_time = 0.1
            else:
                product.checkout_time = round(product.checkout_time + (0.1*cashier_number),ndigits=2)
        
            product_take_time = round(product.checkout_time, ndigits=2)
            cashier_take["time"] += product_take_time
            print(f"The cashier_{cashier_number}"
                  f"will checkout Customer_{customer.customer_id}'s"
                  f"Product_{product.product_name}"
                  f"in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        print(f"The cashier_{cashier_number}"
              f"finished checkout Customer_{customer.customer_id}"
              f"in {round(cashier_take['time'],ndigits=2)} secs")

        queue.task_done()
    return cashier_take
























# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', .4),
                    Product('sausage', .4),
                    Product('diapers', .2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id)
                     for the_id in range(customer_count, customer_count+customers)]
        for customer in customers:
            print(f"Waiting to put Customer_{customer.customer_id} in line.... ")
            await queue.put(customer)
            print(f"Customer_{customer.customer_id} put in line...")
        customer_count = customer_count + len(customers)
        await asyncio.sleep(.001)
        return customer_count

# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    CUSTOMER = 10
    QUEUE = 10
    CASHIER = 5
    customer_queue = Queue(QUEUE)
    customers_start_time = time.perf_counter()
    

    
    async with asyncio.TaskGroup() as group:
        customer_group = group.create_task(customer_generation(customer_queue,CUSTOMER))
        cashier_group = [group.create_task(checkout_customer(customer_queue, i )) for i in range(CASHIER)]
    print(20*'-')
    for cg in cashier_group:
        if cg.result():
            cashier = cg.result()
            print(f'The Cashier_{cashier['id']}'
                  f'take{cashier['customer']} - customers'
                  f'total {round(cashier['time'], ndigits=2)} secs')
    if customer_group.result():
        print(f"The supermarket process finished "
                f'{customer_group.result()} customers'
                f" in {round(time.perf_counter() - customers_start_time, 2)} secs")

        
    
if __name__ == "__main__":
    asyncio.run(main())
