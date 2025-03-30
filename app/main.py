from biological import Biological
from input import Input
from body import Body
from functools import reduce


def get_possible_biologicals(body: Body, biological_list: list[Biological], already_found: list[Biological] = []) -> list[Biological]:
    
    possible_biologicals = []
    found_main_types = [bio.mainType for bio in already_found]
    for biological in biological_list:
        if biological.presence_possible(body) and biological.mainType not in found_main_types:
            possible_biologicals.append(biological)
    return possible_biologicals


def get_most_likely_biologicals(body: Body, biological_list: list[Biological], already_found: list[Biological] = []) -> list[Biological]:

    possible_biologicals = get_possible_biologicals(body, biological_list, already_found)

    #sort on likelyhood, and reverse for high value first
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.likelyhood)
    sorted_possible_biologicals.reverse()
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])


def get_most_valuable_biologicals(body: Body, biological_list: list[Biological], already_found: list[Biological] = []) -> list[Biological]:
    
    possible_biologicals = get_possible_biologicals(body, biological_list, already_found)

    #sort on value, and reverse for high value first
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.value)
    sorted_possible_biologicals.reverse()
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])
    

def get_least_valuable_biologicals(body: Body, biological_list: list[Biological], already_found: list[Biological] = []) -> list[Biological]:
    
    possible_biologicals = get_possible_biologicals(body, biological_list, already_found)

    #sort on value
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.value)
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])

def get_total_value(body: Body, bio_list: list[Biological]):
    running_total = 0
    if  len(bio_list) >= body.biologicalCount:
        i = 0
        for i in range(body.biologicalCount):
            running_total += bio_list[i].value

    return running_total
    