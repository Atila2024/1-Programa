d1 = {"adao smith": "a", "Judite Silva": "B+"}
d2 = {"marli Santos": "a", "Paulo Jose": "C"}
d3 ={}

for item in (d1, d2):
    d3.update(item)

print(d3)
