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
