'''
1st, define a new python class called "food_item", including calories, protein, carbohydrate, and fat 
2nd, define  a new function to calculate the total calories, protein, carbohydrate, and fat of a list of food items
3rd, check if the total calories > 2500 kcal, and if fat > 90g, print a warning message
'''

# 1st, define a new python class called "food_item", including calories, protein, carbohydrate, and fat 
class food_item:
    def __init__(self, name, calories, protein, carbohydrate, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat

    def __str__(self):
        return f"{self.name}: {self.calories} kcal, {self.protein} g protein, {self.carbohydrate} g carbohydrate, {self.fat} g fat"

# 2nd, define  a new function to calculate the total calories, protein, carbohydrate, and fat of a list of food items
def calculate_nutrition(food_list):
    # Initialize the total nutrition values
    total_calories = 0.0
    total_protein = 0.0
    total_carbohydrate = 0.0
    total_fat = 0.0

    # Calculate the total nutrition values by iterating through the food list
    for item in food_list:
        total_calories += item.calories
        total_protein += item.protein
        total_carbohydrate += item.carbohydrate
        total_fat += item.fat
    
    return total_calories, total_protein, total_carbohydrate, total_fat

# create some food items
# name, calories, protein, carbohydrate, fat
# breakfast: apple, noodle, milk, 
# lunch: chicken breast, rice, banana
# dinner: rice, potato, shrimp, nut, cola
apple = food_item("Apple", 95, 0.5, 25, 0.3)
noodle = food_item("Noodle", 200, 7, 40, 1)
milk = food_item("Milk", 122, 8, 12, 5)

rice = food_item("Rice", 206, 4.3, 45, 0.4)
chicken_breast = food_item("Chicken Breast", 165, 31, 0, 3.6)
banana = food_item("Banana", 105, 1.3, 27, 0.4)

potato = food_item("Potato", 163, 4.3, 37, 0.2)
shrimp = food_item("Shrimp", 99, 24, 0.2, 0.3)
nut = food_item("Nut", 607, 20, 20, 50)
cola = food_item("Cola", 150, 0, 39, 0)

# create a list to store the food items
food_list = [apple, banana, chicken_breast, rice, milk, potato, shrimp, nut, cola]
# calculate the total nutrition values of the food list
total_calories, total_protein, total_carbohydrate, total_fat = calculate_nutrition(food_list)
# print the total nutrition values
print(f"Total Calories: {total_calories:.2f} kcal")
print(f"Total Protein: {total_protein:.2f} g")
print(f"Total Carbohydrate: {total_carbohydrate:.2f} g")
print(f"Total Fat: {total_fat:.2f} g")  

# 3rd, check if the total calories > 2500 kcal, and if fat > 90g
if total_calories > 2500:
    print("Warning: Total calories exceed 2500 kcal! Please consider reducing your intake.")

elif total_fat > 90:
    print("Warning: Total fat exceed 90 g! Please consider reducing your intake.")

else :
    print("Your total nutrition intake is within the recommended limits. Keep it up!")