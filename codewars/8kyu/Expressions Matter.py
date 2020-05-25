# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
#In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

def expression_matter(a, b, c):
    results = []
    results.append(a+b+c)
    results.append(a*b*c)
    results.append(a * b + c)
    results.append(a + b * c)
    results.append(a * (b + c))
    results.append((a + b )* c)
    return max(results)