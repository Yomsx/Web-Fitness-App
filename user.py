
class User:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


    def calculate_bmi(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return bmi

    def calculate_bmr(self):
        return (10 * self.weight) + (6.25 * self.height) - (5 * self.age)
        
    def calculate_daily_caloric_needs(self):
        daily_caloric_needs = 2500
        
        return daily_caloric_needs

    def calculate_macronutrient_requirements(self):
        macronutrient_requirements = {
            'protein': 100,
            'carbohydrates': 200,
            'fat': 50
        }
        
        return macronutrient_requirements
