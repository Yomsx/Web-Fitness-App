class Diet:
    def __init__(self, user):
        self.user = user

    def generate_diet_plan(self):
        diet_plan = {
            'Monday': ['Breakfast: Oatmeal with banana and almond milk', 'Lunch: Grilled chicken with brown rice and vegetables', 'Dinner: Salmon with quinoa and broccoli'],
            'Tuesday': ['Breakfast: Scrambled eggs with whole wheat toast and avocado', 'Lunch: Turkey sandwich with carrot sticks and hummus', 'Dinner: Grilled turkey with sweet potato and green beans'],
            'Wednesday': ['Breakfast: Greek yogurt with berries and granola', 'Lunch: Chicken Caesar salad', 'Dinner: Shrimp with brown rice and mixed vegetables'],
            'Thursday': ['Breakfast: Smoothie bowl with banana and almond milk', 'Lunch: Grilled chicken with quinoa and mixed vegetables', 'Dinner: Pork chop with roasted vegetables and quinoa'],
            'Friday': ['Breakfast: Avocado toast with scrambled eggs', 'Lunch: Chicken wrap with mixed vegetables', 'Dinner: Grilled salmon with brown rice and steamed asparagus'],
            'Saturday': ['Breakfast: Omelette with vegetables and whole wheat toast', 'Lunch: Grilled chicken with mixed vegetables and quinoa', 'Dinner: Beef with roasted vegetables and brown rice'],
            'Sunday': ['Breakfast: Breakfast burrito with scrambled eggs and black beans', 'Lunch: Turkey and cheese sandwich with carrot sticks and hummus', 'Dinner: Chicken with mixed vegetables and quinoa']
        }
        return diet_plan
