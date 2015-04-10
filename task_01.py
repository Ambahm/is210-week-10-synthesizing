#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Misc. dictionary"""


import data

def sum_orders(customers, orders):
    """
    A module to show the correlation between two dictionaries.
    Crossmatch between key and values.

    Args:
        cusotmer(dict): Customer dictionary, primary key customer_id
        orders(dict): Orders dictionary , primary key order id

    Return:
        dict: A combined dictionary, retreived through customer id

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
        3: {'customer_id': 2, 'total': 10},
        4: {'customer_id': 3, 'total': 15}}

        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
        3: {'name': 'Person Two', 'email': 'email@two.com'}}

        >>> sum_order_orders(customers, orders)
        {2: {'name': 'Person One',
        'email': 'email@one.com',
        'orders': 2,
        'total': 20}
        3: {'name': 'Person Two',
        'email': 'email@two.com',
        'orders': 1,
        'total': 15}}

    """
    customer_ids = customers.keys()               # getting list of customer_ids
    order_ids = [o for o in orders]                 # list of ids in ORDERS

    sum_order = []                      # sum_order of orders for each customer
    for i in customer_ids:
        sum_total = 0
        total_orders = 0
        for order_ind in order_ids:         # count total orders for a customer
            if orders[order_ind]['customer_id'] == i:
                total_orders = total_orders + 1         # Increment the count of
                                                        # total orders
                sum_total = sum_total + orders[order_ind]['total']

        # Each element in the list 'sum_order' contains a list -
        #[customer id, number of orders, sum_order of orders]

        sum_order.append([i, total_orders, sum_total])

    # sum_order has the total orders and sum_order of orders
    # pick them one by one and add them to customers
    #with matching customer ids
    for i in customer_ids:

        # For a particular customer_id, select the corresponding element
        # from the 'sum_order' list

        elem = [e for e in sum_order if e[0] == i]

        # For ith customer get orders, total
        customers[i]['orders'] = elem[0][1] # Set the orders to the right value
        customers[i]['total'] = elem[0][2]  # Set the total to the right value

    return customers



if __name__ == "__main__":
    print sum_orders(customers=data.CUSTOMERS, orders=data.ORDERS)
    #print customers






