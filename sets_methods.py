# union() and update()
# union
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.union(cities2)
print(cities3)

# udate
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities.update(cities2)
print(cities)

# intersection
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.intersection(cities2)
print(cities3)

# intersection_update
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities.intersection_update(cities2)
print(cities)

# symmetric_difference
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.symmetric_difference(cities2)
print(cities3) 

# symmetric_diffrence_update
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

# difference
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Seoul","Kabul","Delhi"}
cities3=cities.difference(cities2)
print(cities3)

# difference_update
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Seoul","Kabul","Delhi"}
cities.difference_update(cities2)
print(cities)

# isdisjoint
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
print(cities.isdisjoint(cities2))

# issuperset
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Seoul","Kabul",}
print(cities.issuperset(cities2))

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Madrid","Berlin"}
print(cities.issuperset(cities2))

# issubset
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Berlin","Madrid"}
print(cities2.issubset(cities))

# add
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.add("Helsinki")
print(cities)

# update
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Helsinki","Warsaw","Seoul"}
cities.update(cities2)
print(cities)

# remove()/discard()
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)

# pop
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities)

# clear
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

info = {"Carla", 19, False, 5.9}
if ("Carla" in info):
    print("Carla is present")
else:
    print("Carla is absent")