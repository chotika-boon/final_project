import random
from difflib import SequenceMatcher

class RestaurantSelector:
    """Handles restaurant selection process, including recommendations."""

    def __init__(self):
        self.all_restaurants = [
            "MK Suki", "Shabu Indy", "Shabushi", "Shabu Kai Yang", "The Pizza Company",
            "After You", "Starbucks", "Suki Teenoi", "Suki Jinda", "Shabu House"
        ]

    def all_recommend_restaurants(self):
        """Returns a list of recommended restaurants."""
        return self.all_restaurants 

    def recommend_restaurants(self):
        """Returns a list of recommended restaurants."""
        return self.all_restaurants[:5]  # ✅ คืนค่า list แทน None

    def get_similarity(self, a, b):
        """Returns similarity percentage between two strings."""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio() * 100

    def suggest_similar_restaurants(self, input_name):
        """Suggests up to 5 most similar restaurant names with match > 60%."""
        matches = [(restaurant, self.get_similarity(input_name, restaurant))
                   for restaurant in self.all_restaurants]

        # Filter matches > 60% and sort by highest match
        matches = sorted([m for m in matches if m[1] >= 60], key=lambda x: x[1], reverse=True)

        # Return only the top 5 matches
        return matches[:5]

class CardRecommender:
    """Handles card recommendations based on user lifestyle and benefits."""

    def __init__(self):
        self.cards = [
            Card("C001", "Platinum Rewards", "SCB", 5, 2, 15, "Free airport lounge access"),
            Card("C002", "Cashback Plus", "Krungsri", 7, 1, 10, "Travel insurance up to 5M THB"),
            Card("C003", "Dining Exclusive", "KBank", 3, 3, 20, "Priority restaurant reservations"),
            Card("C004", "Travel Pro", "Bangkok Bank", 2, 4, 5, "Bonus miles for flights"),
            Card("C005", "Shopping Master", "TMB", 4, 5, 12, "Extra discounts on e-commerce")
        ]

    def recommend_cards(self, restaurant_name):
        """Assigns 1 random credit card per restaurant selection."""
        if not self.cards:
            return None  # ✅ ป้องกันคืนค่า None
        return random.choice(self.cards)  # ✅ คืนค่าบัตรเครดิตแบบสุ่ม

class Card:
    """Represents a credit card and its benefits."""

    def __init__(self, card_id, card_name, bank, cashback, rewards, dining_discount, travel_benefit):
        self.card_id = card_id
        self.card_name = card_name
        self.bank = bank
        self.cashback = cashback
        self.rewards = rewards
        self.dining_discount = dining_discount
        self.travel_benefit = travel_benefit
