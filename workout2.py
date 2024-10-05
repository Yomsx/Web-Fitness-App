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
