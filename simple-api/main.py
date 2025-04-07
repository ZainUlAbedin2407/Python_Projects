from fastapi import FastAPI
import random

app = FastAPI()

# Creating simple two get endpoints
# 1_side_hustles
# 2_money_quotes

side_hustles = [
    "Freelance Writing",
    "Graphic Design",
    "Web Development",
    "Online Tutoring",
    "Dropshipping",
    "Affiliate Marketing",
    "Virtual Assistant",
    "Social Media Management",
    "Content Creation (YouTube, TikTok)",
    "Photography",
    "Selling Handmade Crafts",
    "Print on Demand",
    "Blogging",
    "App Development",
    "Online Surveys",
    "Transcription Services",
    "Selling Digital Products",
    "Flipping Items Online",
    "Pet Sitting/Dog Walking",
    "Ride Sharing (Uber, Lyft)",
    "Delivery Services (Food, Parcels)",
    "Language Translation",
    "Resume Writing Services",
    "Online Course Creation",
    "Stock Trading/Crypto Investing",
]


money_quotes = [
    "Don't work for money; make it work for you. – Robert Kiyosaki",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "The goal isn't more money. The goal is living life on your terms. – Chris Brogan",
    "It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "The more you learn, the more you earn. – Warren Buffett",
    "Make money while you sleep or you will work until you die. – Warren Buffett",
    "If you don't find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Money is a tool. Used properly it makes something beautiful; used wrong, it makes a mess. – Bradley Vinson",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Too many people spend money they haven't earned to buy things they don't want to impress people they don't like. – Will Rogers",
    "A penny saved is a penny earned. – Benjamin Franklin",
    "Wealth is the ability to fully experience life. – Henry David Thoreau",
    "It’s not about having lots of money. It’s knowing how to manage it.",
]


@app.get("/side_hustles")
def get_side_hustles(apiKey: str):
    """Returns a random side hustle idea."""
    if apiKey != "1234567890":
        return {"error": "Invalid API Key"}
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes(apiKey: str):
    if apiKey != "1234567890":
        return {"error": "Invalid API Key"}
    """Returns a random money quote."""
    return {"money_quote": random.choice(money_quotes)}
