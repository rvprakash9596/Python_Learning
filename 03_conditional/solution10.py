#  Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = input("Enter Species : ")
age = int(input("Enter Age :"))
# Convert species to lowercase for consistency
species = species.lower()
if species == "dog":
    if age < 2:
        food = "Puppy Food"
    elif 2 <= age <= 5:
        food = "Adult Dog Food"
    else:
        food = "Senior Dog Food"
elif species == "cat":
    if age < 2:
        food = "Kitten Food"
    elif 2 <= age <= 5:
        food = "Adult Cat Food"
    else:
        food = "Senior Cat Food"
else:
    food = "Species not recognized. Please enter 'Dog' or 'Cat'."
print("Recommended Food:", food)