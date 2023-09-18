people=[
    {"name":"harry","house":"flat"},
    {"name":"cho","house":"raven"},
    {"name":"draco","house":"sly"}
]
#in other to sort the dict. you write this function
def f(person):
    return person["name"]

people.sort(key=f)

#instead of writing the above function you can use lambda
people.sort(key=lambda person:person["name"])

print(people)