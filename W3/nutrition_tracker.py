"""Nutrition Tracker Module

This module provides classes for tracking daily food intake,
including calories and protein consumption.
"""
from datetime import datetime
from typing import List


class Food:
    """Represents a food item with nutritional information."""
   
    def __init__(self, name: str, calories: int, protein: float):
        """Initialize a Food object.
        
        Args:
            name: The name of the food item
            calories: The calorie content (kcal)
            protein: The protein content (grams)
        """
        self.name = name
        self.calories = calories
        self.protein = protein
        self.date_added = datetime.now()


class DailyLog:
    """Represents a daily log of food consumption."""
    
    def __init__(self, date: str):
        """Initialize a DailyLog for a specific date.
        
        Args:
            date: The date string (e.g., "2026-05-12")
        """
        self.date = date
        self.foods: List[Food] = []
    
    def add_food(self, food: Food) -> None:
        """Add a food item to the daily log.
        
        Args:
            food: The Food object to add
        """
        self.foods.append(food)
    
    def total_calories(self) -> int:
        """Calculate the total calories from all food items.
        
        Returns:
            Sum of calories for all foods in the log
        """
        return sum(f.calories for f in self.foods)
    
    def total_protein(self) -> float:
        """Calculate the total protein from all food items.
        
        Returns:
            Sum of protein (grams) for all foods in the log
        """
        return sum(f.protein for f in self.foods)
    
    def get_summary(self) -> str:
        """Generate a formatted summary of the daily log.
        
        Returns:
            A multi-line string containing date, total calories,
            total protein, and food count
        """
        return f"""
        Date: {self.date}
        Total Calories: {self.total_calories()} kcal
        Total Protein: {self.total_protein():.1f}g
        Foods: {len(self.foods)}
        """
    
    def get_food_names(self) -> List[str]:
        """Get a list of all food names in the daily log.
        
        Returns:
            A list containing the name of each food item
        """
        return [food.name for food in self.foods]

    def clear_log(self) -> None:
        """Remove all food entries from the daily log."""
        self.foods.clear()
    
    def remove_food(self, food_name: str) -> bool:
        """Remove a food item by its name.
        
        Args:
            food_name: The name of the food to remove
            
        Returns:
            True if the food was found and removed, False otherwise
        """
        for i, food in enumerate(self.foods):
            if food.name == food_name:
                self.foods.pop(i)
                return True
        return False
    
    def has_food(self, food_name: str) -> bool:
        """Check if a food item exists in the daily log.
        
        Args:
            food_name: The name of the food to check
            
        Returns:
            True if the food exists in the log, False otherwise
        """
        return any(food.name == food_name for food in self.foods)
    
    def average_calories(self) -> float:
        """Calculate the average calories per food item.
        
        Returns:
            The average calories per food item, or 0.0 if no foods exist
        """
        if not self.foods:
            return 0.0
        return self.total_calories() / len(self.foods)


# Test
today = DailyLog("2026-05-13")
today.add_food(Food("Chicken", 165, 31))
today.add_food(Food("Rice", 206, 4.3))
today.remove_food("Rice")
# today.remove_food("Chicken")
today.add_food(Food("Salmon", 208, 20))
print(today.get_summary())