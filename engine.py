
BANKS = ["KBank", "SCB", "Krungsri", "KTC"]
CARD_TYPES = ["Platinum", "Gold", "Classic"]
LIFESTYLES = ["สายกิน", "สายเที่ยว", "สายช้อป"]

class UserManager:
    def __init__(self):
        self.users = {}

    def authenticate_user(self, username, password):
        return username in self.users and self.users[username]["password"] == password

    def register_user(self, username, password, bank, card_type, lifestyle):
        if username in self.users:
            return False, "มีผู้ใช้นี้อยู่แล้ว"
        self.users[username] = {
            "password": password,
            "bank": bank,
            "card_type": card_type,
            "lifestyle": lifestyle
        }
        return True, "ลงทะเบียนสำเร็จ"

    def get_user_data(self, username):
        return self.users.get(username, {})

class RestaurantSelector:
    def __init__(self):
        self.all_restaurants = ["Thong Grill", "Burger King", "Starbucks", "MOS BURGER"]

    def get_sample_data(self):
        return [
            {
                "name": "Thong Grill Hide & Yakiniku",
                "category": "ชาบู/สุกี้",
                "rating": 4.8,
                "reviews": 5,
                "image_url": "https://img.wongnai.com/p/624x0/2025/03/28/7b4e368494c94cee80dfc99f0a7704dc.jpg"
            },
            {
                "name": "Burger King",
                "category": "เบอร์เกอร์",
                "rating": 4.4,
                "reviews": 10,
                "image_url": "https://img.wongnai.com/p/624x0/2025/04/11/e6b18c24a9914034b14666aba59ecdfd.jpg"
            },
            {
                "name": "Starbucks River City",
                "category": "ร้านกาแฟ/ชา",
                "rating": 4.6,
                "reviews": 14,
                "image_url": "https://img.wongnai.com/p/624x0/2024/04/17/1e4ec5eae8ad4e2cbcb79fd2753e16f9.jpg"
            },
            {
                "name": "MOS BURGER",
                "category": "เบอร์เกอร์",
                "rating": 4.5,
                "reviews": 13,
                "image_url": "https://img.wongnai.com/p/624x0/2024/09/10/44f2586e3bd84950b34fd074b82e7a85.jpg"
            }
        ]

class CardRecommender:
    def recommend_cards(self, restaurant):
        class Card:
            def __init__(self):
                self.card_name = "KTC Platinum"
                self.bank = "KTC"
                self.cashback = 5
                self.rewards = 10
                self.dining_discount = 15
                self.travel_benefit = "Lounge Access"
        return Card()
