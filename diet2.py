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
