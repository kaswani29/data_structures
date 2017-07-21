



def max_duffel_bag_value(cake_tuples, weight_capacity):


    max_values_at_capacities = [0] * (weight_capacity + 1)
    remaining_capacity = weight_capacity
    for current_capacity in range(1,capacity+1):

        for cake_weight, cake_value in cake_tuples:

            if cake_weight <= current_capacity:

                max_value_using_cake = cake_value + max_values_at_capacities[current_capacity - cake_weight]
                max_values_at_capacities[current_capacity] = max(max_values_at_capacities[current_capacity], max_value_using_cake)



def max_value_at_current








cake_tuples = [(7, 160), (3, 90), (2, 15)]
weight_capacity    = 20

max_duffel_bag_value(cake_tuples, capacity)