class Workout:
    def __init__(self, user):
        self.user = user

    def generate_workout_plan(self):
        workout_plan = {
            'Monday': ['Squats', 'Lunges', 'Push-ups'],
            'Tuesday': ['Deadlifts', 'Bench press', 'Rows'],
            'Wednesday': ['Rest day'],
            'Thursday': ['Leg press', 'Shoulder press', 'Bicep curls'],
            'Friday': ['Chest press', 'Tricep dips', 'Leg extensions'],
            'Saturday': ['Rest day'],
            'Sunday': ['Rest day']
        }
        return workout_plan
