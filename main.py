from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Move this up
from fastapi.responses import FileResponse   # Move this up
from pydantic import BaseModel

import re
import math

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Password(BaseModel):
    password: str

def calculate_password_strength(password: str) -> dict:
    strength = 0
    feedback = []
    time_to_crack = "instant"
    
    # Length check
    if len(password) >= 8:
        strength += 20
        feedback.append("Good length")
    else:
        feedback.append("Password should be at least 8 characters")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        strength += 20
        feedback.append("Contains uppercase letters")
    else:
        feedback.append("Add uppercase letters")

    # Lowercase check
    if re.search(r'[a-z]', password):
        strength += 20
        feedback.append("Contains lowercase letters")
    else:
        feedback.append("Add lowercase letters")

    # Numbers check
    if re.search(r'\d', password):
        strength += 20
        feedback.append("Contains numbers")
    else:
        feedback.append("Add numbers")

    # Special characters check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 20
        feedback.append("Contains special characters")
    else:
        feedback.append("Add special characters")

    # Calculate approximate time to crack
    entropy = len(password) * math.log2(95)  # 95 printable ASCII characters
    combinations = 2 ** entropy
    seconds_to_crack = combinations / (10 ** 9)  # Assuming 1 billion guesses per second

    if seconds_to_crack < 1:
        time_to_crack = "instant"
    elif seconds_to_crack < 60:
        time_to_crack = f"{seconds_to_crack:.0f} seconds"
    elif seconds_to_crack < 3600:
        time_to_crack = f"{seconds_to_crack/60:.0f} minutes"
    elif seconds_to_crack < 86400:
        time_to_crack = f"{seconds_to_crack/3600:.0f} hours"
    elif seconds_to_crack < 31536000:
        time_to_crack = f"{seconds_to_crack/86400:.0f} days"
    else:
        time_to_crack = f"{seconds_to_crack/31536000:.0f} years"

    return {
        "strength": strength,
        "feedback": feedback,
        "timeToHack": time_to_crack
    }

@app.get("/")
async def root():
    return FileResponse('static/index.html')

@app.post("/analyze-password")
async def analyze_password(password: Password):
    return calculate_password_strength(password.password)




