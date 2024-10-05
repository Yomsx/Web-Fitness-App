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
