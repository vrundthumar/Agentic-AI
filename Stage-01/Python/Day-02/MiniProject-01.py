# Students marks average calculator

marks = []

for i in range(5):
     m = int(input("Enter marks: "))
     marks.append(m)

total = 0

for x in marks:
   total = total + x

average = total / 5

print(f"The average of the students is : {average}")

# Output
# Enter marks: 30
# Enter marks: 40
# Enter marks: 50
# Enter marks: 60
# Enter marks: 70
# The average of the students is : 50.0