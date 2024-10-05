I can help you add those features. Here's an updated version of the code:

**user.py**

```python
class User:
    def __init__(self, name, age, weight, height, gender, goals, activity_level):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.goals = goals
        self.activity_level = activity_level

    def calculate_bmr(self):
        if self.gender == 'male':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
        elif self.gender == 'female':
            bmr = (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
        return bmr

    def calculate_daily_caloric_needs(self):
        bmr = self.calculate_bmr()

        # Map activity level to the corresponding factor
        activity_factors = {
            'sedentary': 1.2,
            'lightly_active': 1.375,
            'moderately_active': 1.55,
            'very_active': 1.725,
            'extra_active': 1.9
        }

        # Calculate daily caloric needs based on activity level
        daily_caloric_needs = bmr * activity_factors.get(self.activity_level, 1)

        # Adjust based on goals
        if self.goals == 'lose_fat':
            daily_caloric_needs *= 0.8
        elif self.goals == 'build_muscle':
            daily_caloric_needs *= 1.2
        elif self.goals == 'maintain_weight':
            daily_caloric_needs *= 1

        return daily_caloric_needs

    def calculate_macronutrient_requirements(self):
        daily_caloric_needs = self.calculate_daily_caloric_needs()

        # Calculate macronutrient breakdown
        protein = 1.6 * self.weight  # 1.6g protein per kg of body weight
        carbohydrates = (daily_caloric_needs * 0.55) / 4  # 55% of calories from carbs, 1g carbs = 4 kcal
        fat = (daily_caloric_needs * 0.25) / 9  # 25% of calories from fat, 1g fat = 9 kcal

        return {
            'protein': protein,
            'carbohydrates': carbohydrates,
            'fat': fat
        }

```

**workout.py**

```python
class Workout:
    def __init__(self, user):
        self.user = user

    def generate_workout_plan(self):
        if self.user.goals == 'lose_fat':
            workout_plan = {
                'Monday': ['Warm-up: 5-10 minutes cardio', 'Squats: 3 sets of 15 reps', 'Lunges: 3 sets of 15 reps', 'Push-ups: 3 sets of 15 reps', 'Cool-down: 5-10 minutes stretching'],
                'Tuesday': ['Warm-up: 5-10 minutes cardio', 'Deadlifts: 3 sets of 15 reps', 'Bench press: 3 sets of 15 reps', 'Rows: 3 sets of 15 reps', 'Cool-down: 5-10 minutes stretching'],
                'Wednesday': ['Rest day'],
                'Thursday': ['Warm-up: 5-10 minutes cardio', 'Leg press: 3 sets of 15 reps', 'Shoulder press: 3 sets of 15 reps', 'Bicep curls: 3 sets of 15 reps', 'Cool-down: 5-10 minutes stretching'],
                'Friday': ['Warm-up: 5-10 minutes cardio', 'Chest press: 3 sets of 15 reps', 'Tricep dips: 3 sets of 15 reps', 'Leg extensions: 3 sets of 15 reps', 'Cool-down: 5-10 minutes stretching'],
                'Saturday': ['Rest day'],
                'Sunday': ['Rest day']
            }
            cardio_plan = {
                'Monday': '30 minutes steady-state cardio',
                'Tuesday': '30 minutes HIIT cardio',
                'Wednesday': 'Rest day',
                'Thursday': '30 minutes steady-state cardio',
                'Friday': '30 minutes HIIT cardio',
                'Saturday': 'Rest day',
                'Sunday': 'Rest day'
            }
        elif self.user.goals == 'build_muscle':
            workout_plan = {
                'Monday': ['Warm-up: 5-10 minutes cardio', 'Squats: 4 sets of 6-8 reps', 'Lunges: 4 sets of 6-8 reps', 'Push-ups: 4 sets of 6-8 reps', 'Cool-down: 5-10 minutes stretching'],
                'Tuesday': ['Warm-up: 5-10 minutes cardio', 'Deadlifts: 4 sets of 6-8 reps', 'Bench press: 4 sets of 6-8 reps', 'Rows: 4 sets of 6-8 reps', 'Cool-down: 5-10 minutes stretching'],
                'Wednesday': ['Rest day'],
                'Thursday': ['Warm-up: 5-10 minutes cardio', 'Leg press: 4 sets of 6-8 reps', 'Shoulder press: 4 sets of 6-8 reps', 'Bicep curls: 4 sets of 6-8 reps', 'Cool-down: 5-10 minutes stretching'],
                'Friday': ['Warm-up: 5-10 minutes cardio', 'Chest press: 4 sets of 6-8 reps', 'Tricep dips: 4 sets of 6-8 reps', 'Leg extensions: 4 sets of 6-8 reps', 'Cool-down: 5-10 minutes stretching'],
                'Saturday': ['Rest day'],
                'Sunday': ['Rest day']
            }
            cardio_plan = {
                'Monday': '10 minutes steady-state cardio',
                'Tuesday': '10 minutes HIIT cardio',
                'Wednesday': 'Rest day',
                'Thursday': '10 minutes steady-state cardio',
                'Friday': '10 minutes HIIT cardio',
                'Saturday': 'Rest day',
                'Sunday': 'Rest day'
            }
        elif self.user.goals == 'maintain_weight':
            workout_plan = {
                'Monday': ['Warm-up: 5-10 minutes cardio', 'Squats: 3 sets of 10 reps', 'Lunges: 3 sets of 10 reps', 'Push-ups: 3 sets of 10 reps', 'Cool-down: 5-10 minutes stretching'],
                'Tuesday': ['Warm-up: 5-10 minutes cardio', 'Deadlifts: 3 sets of 10 reps', 'Bench press: 3 sets of 10 reps', 'Rows: 3 sets of 10 reps', 'Cool-down: 5-10 minutes stretching'],
                'Wednesday': ['Rest day'],
                'Thursday': ['Warm-up: 5-10 minutes cardio', 'Leg press: 3 sets of 10 reps', 'Shoulder press: 3 sets of 10 reps', 'Bicep curls: 3 sets of 10 reps', 'Cool-down: 5-10 minutes stretching'],
                'Friday': ['Warm-up: 5-10 minutes cardio', 'Chest press: 3 sets of 10 reps', 'Tricep dips: 3 sets of 10 reps', 'Leg extensions: 3 sets of 10 reps', 'Cool-down: 5-10 minutes stretching'],
                'Saturday': ['Rest day'],
                'Sunday': ['Rest day']
            }
            cardio_plan = {
                'Monday': '15 minutes steady-state cardio',
                'Tuesday': '15 minutes HIIT cardio',
                'Wednesday': 'Rest day',
                'Thursday': '15 minutes steady-state cardio',
                'Friday': '15 minutes HIIT cardio',
                'Saturday': 'Rest day',
                'Sunday': 'Rest day'
            }

        return {
            'workout_plan': workout_plan,
            'cardio_plan': cardio_plan
        }

```

**diet.py**

```python
class Diet:
    def __init__(self, user):
        self.user = user

    def generate_diet_plan(self):
        daily_caloric_needs = self.user.calculate_daily_caloric_needs()
        macronutrient_requirements = self.user.calculate_macronutrient_requirements()

        if self.user.goals == 'lose_fat':
            diet_plan = {
                'Monday': ['Breakfast: Oatmeal with almond butter and chia seeds', 'Lunch: Grilled chicken salad with olive oil', 'Dinner: Baked fish with steamed vegetables'],
                'Tuesday': ['Breakfast: Egg whites and avocado', 'Lunch: Turkey wrap with spinach and hummus', 'Dinner: Grilled chicken with mixed greens and avocado'],
                'Wednesday': ['Breakfast: Smoothie with spinach, protein powder, and almond milk', 'Lunch: Salmon salad with mixed greens', 'Dinner: Grilled shrimp with steamed broccoli and quinoa'],
                'Thursday': ['Breakfast: Greek yogurt with berries and flax seeds', 'Lunch: Chicken breast with roasted vegetables', 'Dinner: Lean turkey with mixed greens and olive oil'],
                'Friday': ['Breakfast: Avocado toast with egg whites', 'Lunch: Grilled tuna with steamed vegetables', 'Dinner: Baked fish with roasted sweet potatoes'],
                'Saturday': ['Breakfast: Omelette with vegetables and spinach', 'Lunch: Grilled chicken breast with quinoa and steamed vegetables', 'Dinner: Grilled turkey with mixed greens and olive oil'],
                'Sunday': ['Breakfast: Scrambled eggs with avocado', 'Lunch: Turkey wrap with spinach and hummus', 'Dinner: Grilled salmon with roasted vegetables and quinoa']
            }
        elif self.user.goals == 'build_muscle':
            diet_plan = {
                'Monday': ['Breakfast: Oatmeal with protein powder and almond butter', 'Lunch: Grilled chicken with brown rice and vegetables', 'Dinner: Steak with sweet potato and broccoli'],
                'Tuesday': ['Breakfast: Whole eggs and avocado toast', 'Lunch: Salmon with quinoa and steamed vegetables', 'Dinner: Grilled chicken with mixed greens and sweet potatoes'],
                'Wednesday': ['Breakfast: Smoothie with spinach, protein powder, banana, and almond milk', 'Lunch: Turkey burger with avocado and sweet potato fries', 'Dinner: Grilled beef with roasted vegetables and quinoa'],
                'Thursday': ['Breakfast: Greek yogurt with berries and granola', 'Lunch: Grilled shrimp with brown rice and vegetables', 'Dinner: Chicken breast with roasted vegetables and brown rice'],
                'Friday': ['Breakfast: Scrambled eggs with avocado and whole wheat toast', 'Lunch: Grilled tuna with quinoa and mixed greens', 'Dinner: Grilled salmon with sweet potato and steamed broccoli'],
                'Saturday': ['Breakfast: Omelette with spinach, mushrooms, and whole wheat toast', 'Lunch: Chicken stir-fry with vegetables and brown rice', 'Dinner: Grilled beef with roasted vegetables and sweet potatoes'],
                'Sunday': ['Breakfast: Protein pancakes with banana', 'Lunch: Turkey wrap with avocado and spinach', 'Dinner: Grilled chicken with brown rice and steamed vegetables']
            }
        elif self.user.goals == 'maintain_weight':
            diet_plan = {
                'Monday': ['Breakfast: Greek yogurt with granola and berries', 'Lunch: Grilled chicken wrap with avocado', 'Dinner: Salmon with quinoa and asparagus'],
                'Tuesday': ['Breakfast: Smoothie with protein powder, banana, and almond milk', 'Lunch: Turkey and cheese sandwich with spinach and hummus', 'Dinner: Grilled shrimp with brown rice and steamed vegetables'],
                'Wednesday': ['Breakfast: Oatmeal with almond butter and chia seeds', 'Lunch: Chicken salad with mixed greens and olive oil', 'Dinner: Grilled beef with roasted vegetables and quinoa'],
                'Thursday': ['Breakfast: Scrambled eggs with avocado and whole wheat toast', 'Lunch: Grilled tuna with brown rice and mixed greens', 'Dinner: Grilled chicken with roasted sweet potatoes and vegetables'],
                'Friday': ['Breakfast: Greek yogurt with berries and flax seeds', 'Lunch: Grilled salmon with quinoa and steamed vegetables', 'Dinner: Lean beef with mixed greens and olive oil'],
                'Saturday': ['Breakfast: Omelette with spinach, mushrooms, and whole wheat toast', 'Lunch: Turkey wrap with avocado and spinach', 'Dinner: Grilled turkey with roasted vegetables and quinoa'],
                'Sunday': ['Breakfast: Smoothie with spinach, protein powder, and almond milk', 'Lunch: Grilled chicken with brown rice and mixed vegetables', 'Dinner: Baked fish with roasted sweet potatoes and steamed broccoli']
            }

        return {
            'daily_caloric_needs': daily_caloric_needs,
            'macronutrient_requirements': macronutrient_requirements,
            'diet_plan': diet_plan
        }

```

**app.py**

```python
from flask import Flask, request, jsonify
from models.user import User
from models.workout import Workout
from models.diet import Diet

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        user_data = request.form
        
        # Create a User instance
        user = User(
            user_data['name'], 
            int(user_data['age']),  
            float(user_data['weight']), 
            float(user_data['height']), 
            user_data['gender'], 
            user_data['goals'], 
            user_data['activity_level']
        )

        # Generate workout and diet plans
        workout = Workout(user)
        diet = Diet(user)

        workout_plan = workout.generate_workout_plan()
        diet_plan = diet.generate_diet_plan()

        # Return the response as JSON
        return jsonify({
            'workout_plan': workout_plan['workout_plan'],
            'cardio_plan': workout_plan['cardio_plan'],
            'diet_plan': diet_plan['diet_plan'],
            'daily_caloric_needs': diet_plan['daily_caloric_needs'],
            'macronutrient_requirements': diet_plan['macronutrient_requirements']
        })

if __name__ == '__main__':
    app.run(debug=True)

```

**gui.py**

```python
import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Workout and Diet Planner")
        self.window.geometry("600x600")  # Set window size

        # Create the input fields and labels for user data
        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.age_label = tk.Label(self.window, text="Age:")
        self.age_label.pack(pady=5)
        self.age_entry = tk.Entry(self.window)
        self.age_entry.pack()

        self.weight_label = tk.Label(self.window, text="Weight (kg):")
        self.weight_label.pack(pady=5)
        self.weight_entry = tk.Entry(self.window)
        self.weight_entry.pack()

        self.height_label = tk.Label(self.window, text="Height (cm):")
        self.height_label.pack(pady=5)
        self.height_entry = tk.Entry(self.window)
        self.height_entry.pack()

        self.gender_label = tk.Label(self.window, text="Gender:")
        self.gender_label.pack(pady=5)
        self.gender_var = tk.StringVar()
        self.gender_var.set("male")
        self.gender_option = tk.OptionMenu(self.window, self.gender_var, "male", "female")
        self.gender_option.pack()

        self.goals_label = tk.Label(self.window, text="Goals:")
        self.goals_label.pack(pady=5)
        self.goals_var = tk.StringVar()
        self.goals_var.set("lose_fat")
        self.goals_option = tk.OptionMenu(self.window, self.goals_var, "lose_fat", "build_muscle", "maintain_weight")
        self.goals_option.pack()

        self.activity_level_label = tk.Label(self.window, text="Activity level:")
        self.activity_level_label.pack(pady=5)
        self.activity_level_var = tk.StringVar()
        self.activity_level_var.set("sedentary")
        self.activity_level_option = tk.OptionMenu(self.window, self.activity_level_var, "sedentary", "lightly_active", "moderately_active", "very_active", "extra_active")
        self.activity_level_option.pack()

        # Submit button
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit)
        self.submit_button.pack(pady=10)

        # Text areas to display results
        self.result_text = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, height=20, width=70)
        self.result_text.pack(pady=10)

        # Close the application with proper cleanup
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            self.window.destroy()

    def submit(self):
        # Collect user data from input fields
        user_data = {
            'name': self.name_entry.get(),
            'age': self.age_entry.get(),
            'weight': self.weight_entry.get(),
            'height': self.height_entry.get(),
            'gender': self.gender_var.get(),
            'goals': self.goals_var.get(),
            'activity_level': self.activity_level_var.get()
        }

        # Input validation
        if not all(user_data.values()):
            messagebox.showerror("Error", "All fields must be filled!")
            return

        try:
            user_data['age'] = int(user_data['age'])
            user_data['weight'] = float(user_data['weight'])
            user_data['height'] = float(user_data['height'])
        except ValueError:
            messagebox.showerror("Error", "Age must be an integer, and Weight/Height must be numbers.")
            return

        # Make POST request to the backend to get workout and diet plans
        try:
            response = requests.post('http://localhost:5000/', data=user_data)

            if response.status_code == 200:
                result = response.json()
                workout_plan = result.get('workout_plan')
                cardio_plan = result.get('cardio_plan')
                diet_plan = result.get('diet_plan')
                daily_caloric_needs = result.get('daily_caloric_needs')
                macronutrient_requirements = result.get('macronutrient_requirements')

                self.result_text.delete(1.0, tk.END)  # Clear the previous result

                # Display workout plan
                workout_text = "Workout Plan:\n\n"
                for day, exercises in workout_plan.items():
                    workout_text += f"{day}:\n" + "\n".join([f"  - {exercise}" for exercise in exercises]) + "\n\n"

                # Display cardio plan
                cardio_text = "Cardio Plan:\n\n"
                for day, exercises in cardio_plan.items():
                    cardio_text += f"{day}:\n" + "\n".join([f"  - {exercise}" for exercise in [exercises]]) + "\n\n"

                # Display diet plan
                diet_text = "Diet Plan:\n\n"
                for day, meals in diet_plan.items():
                    diet_text += f"{day}:\n" + "\n".join([f"  - {meal}" for meal in meals]) + "\n\n"

                # Display caloric needs and macronutrients
                caloric_needs_text = f"Daily Caloric Needs: {daily_caloric_needs}"
                macronutrient_text = f"Macronutrient Requirements: Protein - {macronutrient_requirements['protein']}g, Carbohydrates - {macronutrient_requirements['carbohydrates']}g, Fats - {macronutrient_requirements['fats']}g"

                # Output the result in the text area
                self.result_text.insert(tk.END, workout_text)
                self.result_text.insert(tk.END, cardio_text)
                self.result_text.insert(tk.END, diet_text)
                self.result_text.insert(tk.END, caloric_needs_text + "\n\n")
                self.result_text.insert(tk.END, macronutrient_text)
            else:
                messagebox.showerror("Error", "Failed to retrieve workout and diet plans.")

        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to connect to the server: {e}")

    def run(self):
        self.window.mainloop()

# Create and run the GUI
if __name__ == "__main__":
    app = GUI()
    app.run()

```

**main.py** remains the same.

Note that I've made significant changes to your original code, so make sure to review each file carefully to understand what's changed. Also, this is a basic example and real-world applications would require a more sophisticated approach to handle errors, exceptions and edge cases.
