#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Jorge Galvis 


def is_onto (domain, co_domain, mapping):
    """Determines if the function is onto.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in the co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]
    """
    # YOUR CODE HERE

    #This means that every codomain must be present, as a value, in mapping
    for v in co_domain:
        if v not in mapping.values():
            meets_definition = False 
            break 
        meets_definition = True

    return meets_definition

def is_one_to_one (domain, co_domain, mapping):
    """Determines if the function is one-to-one.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    # YOUR CODE HERE

    #This means that every image of f must be unique 
    unique_v = set()
    for k,v in mapping.items():
        if v not in unique_v:
            unique_v.add(v)
            meets_definition = True 
        else:
            meets_definition = False 
            break

    return meets_definition

def is_bijective ( domain , co_domain , mapping ) :
    """Determines if the function is bijective.

    Args:
        domain [list[int]]: a list of values in the domain
        co_domain [list[int]]: a list of values in teh co-domain
        mapping [dict[int,int]]: a dictionary of the function mapping between the domain and co-domain

    Returns:
        meets_definition [bool]

    """
    # WRITE YOUR CODE HERE

    #Both is_onto and one_to_one must be true 
    onto_result = is_onto(domain, co_domain, mapping)
    one_to_one_result = is_one_to_one(domain, co_domain, mapping)
    if onto_result and one_to_one_result:
        meets_definition = True 
    else:
        meets_definition = False 

    return meets_definition

######################################################################
### DO NOT TURN IN AN ASSIGNMENT WITH ANYTHING BELOW HERE MODIFIED ###
######################################################################
if __name__ == '__main__':
    print("#######################################")
    print("Welcome to Coding 3: Functions!")
    print("#######################################")
    print()
    print("---------------------------------------")
    print("PART A: Function Properties")
    print("---------------------------------------")

    example_1 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:3}] #not anything
    example_2 = [[1 ,2 ,3 ,4],[1,2,3,4,5,6,7],{1:2, 2:3, 3:1,4:5}] #one to one (nothing else)
    example_3 = [[1 ,2 ,3 ,4],[1,2,3],{1:2, 2:3, 3:1,4:3}] #onto (nothing else)
    example_4 = [[1 ,2 ,3 ,4],[1,2,3,4],{1:2, 2:3, 3:1,4:4}] #bijective
    
    print("---------------------------------------")
    print("\'is_onto\' Tests")
    print("---------------------------------------")
    is_onto_tests = [example_1, example_2, example_3, example_4]
    is_onto_answers = [False, False, True, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_onto(is_onto_tests[count][0],is_onto_tests[count][1],
                    is_onto_tests[count][2]) == is_onto_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_onto_answers[count]}')
        print(f'Your Answer: {is_onto(is_onto_tests[count][0],is_onto_tests[count][1],is_onto_tests[count][2])}')
        
    print("---------------------------------------")
    print("\'is_one_to_one\' Tests")
    print("---------------------------------------")
    is_one_to_one_tests = [example_1, example_2, example_3, example_4]
    is_one_to_one_answers = [False, True, False, True]
  
    for count, test in enumerate(is_one_to_one_tests):
        if (is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],
                    is_one_to_one_tests[count][2]) == is_one_to_one_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_one_to_one_answers[count]}')
        print(f'Your Answer: {is_one_to_one(is_one_to_one_tests[count][0],is_one_to_one_tests[count][1],is_one_to_one_tests[count][2])}')
    
    print("---------------------------------------")
    print("\'is_bijective\' Tests")
    print("---------------------------------------")
    is_bijective_tests = [example_1, example_2, example_3, example_4]
    is_bijective_answers = [False, False, False, True]
  
    for count, test in enumerate(is_onto_tests):
        if (is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],
                    is_bijective_tests[count][2]) == is_bijective_answers[count]):
            passed = 'PASSED!'
        else:
            passed = "FAILED!"
        
        print("Test #{}: {}".format(count + 1, passed))
        print(f'Correct Answer: {is_bijective_answers[count]}')
        print(f'Your Answer: {is_bijective(is_bijective_tests[count][0],is_bijective_tests[count][1],is_bijective_tests[count][2])}')
