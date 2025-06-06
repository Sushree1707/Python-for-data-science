marks={
    "Suraj":100,
    "Sushree":80,
    "Anuj":50
}

print(marks.items())

print(marks.keys())

print(marks.values())

print(marks.update({"Suraj":99 , "Sunil":88}))

print(marks)

print(marks.get("Suraj1")) #prints none
print(marks["Suraj1"]) #returns an error