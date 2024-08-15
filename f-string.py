letter = "My name is {1}.I am from{0}"
country= "Bangladesh"
name= "Shuvo"
print(letter.format(country,name))
print(f"My name is {name}.I am from{country}")

txt ="For only {price:.2f} dollar!"
print(txt.format(price = 40.125232))

price = 40.125232
print(f"for only {price:.3f} dollars!")


print(f"we use f-strings like this: My name is {{name}}.I am from{{country}}")
