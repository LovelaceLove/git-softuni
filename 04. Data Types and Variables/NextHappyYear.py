year = int(input())

year += 1
year_as_string = str(year)

while len(year_as_string) != len(set(year_as_string)):   #set ,može da ima samo skup jedinstvenih vrednosti 
    year += 1
    year_as_string = str(year)

print(year)

