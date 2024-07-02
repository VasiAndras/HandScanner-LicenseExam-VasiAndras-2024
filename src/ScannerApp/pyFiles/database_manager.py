import json
import os

class Database:
    def __init__(self, filepath='Database/database.json'):
        self.filepath = filepath
        self.data = self.load_database()
        
    def load_database(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, 'r') as file:
                return json.load(file)
        else:
            return {
                "general": {
                    "totalImageCount": 0,
                    "totalUserCount": 0
                },
                "users": []
            }
            
    def save_database(self):
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)
    
    def add_user(self, usercode, legalName, birthDay, directory, gdprFile):
        new_user = {
            "usercode": usercode,
            "legalName": legalName,
            "birthDay": birthDay,
            "pictures": {
                "rightHand": 0,
                "leftHand": 0
            },
            "directory": directory,
            "gdprFile": gdprFile
        }
        
        self.data["users"].append(new_user)
        self.data["general"]["totalUserCount"] += 1
        self.save_database()
    
    def update_picture_count(self, usercode, hand):
        for user in self.data["users"]:
            if user["usercode"] == usercode:
                if hand == "rightHand":
                    user["pictures"]["rightHand"] += 1
                elif hand == "leftHand":
                    user["pictures"]["leftHand"] += 1
                else:
                    raise ValueError("Hand must be either 'rightHand' or 'leftHand'")
                
                self.data["general"]["totalImageCount"] += 1
                self.save_database()
                return
        
        raise ValueError(f"No user found with usercode {usercode}")
    

# Usage example:

# Add a new user
# db.add_user("JD011209", "JOHN DOE", "2001.12.09.", "/database/JD011209_db", "JD011209_gdpr.pdf")
# Update picture count for a user
# db.update_picture_count("VA011208", "rightHand")
# db.update_picture_count("VA011208", "leftHand")
