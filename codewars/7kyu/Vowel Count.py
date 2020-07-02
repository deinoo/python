"""Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""

def get_count(input_str):
    return len(list(filter(lambda x: x in ('a', 'e', 'i', 'o', 'u'), input_str)))

#input_str= "pear tree pear tree pear tree" #, 5
#print (get_count(input_str))