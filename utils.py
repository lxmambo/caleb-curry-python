def stats_range(my_list):
    lowest = my_list[0]
    maximum = my_list[0]
    for nb in my_list:
        if (nb > maximum):
            maximum = nb
        elif (nb < lowest):
            lowest = nb
    return [lowest, maximum]
        
def stats_range_caleb(data):
    data.sort()
    return data[-1]-data[0]

#__pycache__ is a compiled version of the module