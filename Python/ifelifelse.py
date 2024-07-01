"""
Simple problem 

A- 90-100
b =80-90
c=70-79
d= 60-69
f=0-59
"""

grade = int(input("Enter your grade :"))
if grade >= 90:
    print("A")
elif 80 <= grade < 90:
    print("B")
elif 70 <= grade <80:
    print("C")
elif 60 <= grade<70:
    print("D")
else:
    print("F")
