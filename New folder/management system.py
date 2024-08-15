print(" welcome to <<!!Elmore Middle East!!>>\n ")


class data:
    def data(self):
        print(" <|name|> ", " <|age|> ", " <|class|> ")

student = data()
student.data()


print("The three listed above will be the only data needed from you\n")
print("Pleas answer the question asked below\n")
name = input("Hello, what is your name?\n ")
age = input("Hello " + name + " can you tell us your age\n")
Class = input(name + " which class were you coming from in your previous school?\n ")


print("your data preview")
student_dict = dict(name=name, age=age, Class=Class)
print(student_dict)
print("\n")


print("ok so your class list for class " + Class + " is below")

student_list = ["kofi", "Amy", "Calvin", "Kofi", "Mike", "Kojo", "Gifty", "Stephanie", "Desmond", "OKo", "Agustina",
                "lincon", "Bob", "Chuck", name]

print(student_list)





