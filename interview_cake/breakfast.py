



def unique_identifier(delivery_id_confirmation):

    number_tracker = {}

    for number in delivery_id_confirmation:

        if number in number_tracker:
            number_tracker[number] +=1
        else:
            number_tracker[number] = 1

    for key, value in number_tracker.items():

        if value == 1:
            return key







delivery_id_confirmation = [1,5,2,5,1,6,6]

unique_identifier(delivery_id_confirmation)