numOfMax             = 999 # below 1000. 
countOf_3Multiple    = numOfMax          /  3
lastItemOf_3Multiple = countOf_3Multiple *  3
countOf_5Multiple    = numOfMax          /  5
lastItemOf_5Multiple = countOf_5Multiple *  5
countOf15Multiple    = numOfMax          / 15
lastItemOf15Multiple = countOf15Multiple * 15

result  = 0
result += ( 3 + lastItemOf_3Multiple) * countOf_3Multiple / 2
result += ( 5 + lastItemOf_5Multiple) * countOf_5Multiple / 2
result -= (15 + lastItemOf15Multiple) * countOf15Multiple / 2

print(result)
