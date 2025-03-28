from biological import Biological
from input import Input
from body import Body
from functools import reduce


def get_possible_biologicals(body: Body, biological_list: list[Biological]) -> list[Biological]:
    possible_biologicals = []

    for biological in biological_list:
        if biological.presence_possible(body):
            possible_biologicals.append(biological)
    return possible_biologicals


def get_most_likely_biologicals(body: Body, biological_list: list[Biological]) -> list[Biological]:

    possible_biologicals = get_possible_biologicals(body, biological_list)

    #sort on likelyhood, and reverse for high value first
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.likelyhood)
    sorted_possible_biologicals.reverse()
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])


def get_most_valuable_biologicals(body: Body, biological_list: list[Biological]) -> list[Biological]:
    
    possible_biologicals = get_possible_biologicals(body, biological_list)

    #sort on value, and reverse for high value first
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.value)
    sorted_possible_biologicals.reverse()
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])
    

def get_least_valuable_biologicals(body: Body, biological_list: list[Biological]) -> list[Biological]:
    
    possible_biologicals = get_possible_biologicals(body, biological_list)

    #sort on value
    sorted_possible_biologicals = sorted(possible_biologicals, key= lambda x: x.value)
    # Remove duplicate maintypes, keep the first occurance
    return reduce(lambda acc, obj: acc if obj.mainType in {o.mainType for o in acc} else acc + [obj], 
                  sorted_possible_biologicals, [])

