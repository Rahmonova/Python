#BMI (Body Mass Index) Calculator
"""RESOURCE: https://www.medicalnewstoday.com/articles/323622#Understanding-the-results"""
height = int(input("Height : "))
weight = int(input("Weight : "))

BMI = weight / ((height / 100) ** 2)
print(BMI)