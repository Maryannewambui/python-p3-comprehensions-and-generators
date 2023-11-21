#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]
#example
numbers_0_to_20 = list(range(21))

even = return_evens(numbers_0_to_20)

print(even)


def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list]
    return exclamation_list

#example
example_sentence = ["Hello, world"]
result = make_exclamation(example_sentence)

print(result)