#Define a class for food item
class food_item(object):
    def __init__(self,name,calories,protein,carbohydrate,fat):
        self.name= name #name is needed to distinguish items!
        self.calories=calories
        self.protein=protein
        self.carbohydrate=carbohydrate
        self.fat=fat
#Functions to calculate the consumption
    #def consumption(food_list):is the wrong indent, as it was regarded as the method in class
def consumption(food_list):
        """
        input: a list, contains items individual has consumed over a 24hr period
        Returns the total calories,protein,carbohydrate and fat comsumption over the period
        """
        total_calories=0
        total_protein=0
        total_carbohydrate=0
        total_fat=0
        for item in food_list:
            total_calories+=item.calories
            total_protein+=item.protein
            total_carbohydrate+=item.carbohydrate
            total_fat+=item.fat
        print("Daily nutrition consumption")
        print(f"calories consumption:{total_calories:.1f}cal")
        print(f"protein consumption:{total_protein:.1f}g")
        print(f"carbohydrate consumption:{total_carbohydrate:.1f}g")
        print(f"fat consumption:{total_fat:.1f}g")
        if total_calories>2500:
            print("Warning: excessive calorific consumption")
        if total_fat>90:
            print("Warning:excessive fat consumption")
        #return there is no need to return

        
#create an instance
apple=food_item("Apple",60,0.3,15,0.5)
rice=food_item("Rice", 200, 4, 45, 0.5)
food_list=[apple,rice]
print("\nExample consumption calculation:")
consumption(food_list)

# User input for arbitrary foods
print("\nEnter food items consumed today. Enter 'done' to finish.")
user_food_list = []
while True:
    name = input("Food name (or 'done'): ")
    if name.lower() == "done":
        break
    try:
        calories = float(input("Calories: "))
        protein = float(input("Protein (g): "))
        carb = float(input("Carbohydrate (g): "))
        fat = float(input("Fat (g): "))
        user_food_list.append(food_item(name, calories, protein, carb, fat))
    except:
        print("Invalid input, please try again.")

if user_food_list:
    consumption(user_food_list)
else:
    print("No food items entered.")