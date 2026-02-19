import requests
import json

BASE_URL = "http://localhost:8000"

def test_welcome():
    print("Testing /welcome endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/welcome")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}\n")
    except Exception as e:
        print(f"Welcome test failed: {e}\n")

def test_chat(message):
    print(f"Testing /chat with message: '{message}'")
    payload = {
        "message": message,
        "history": []
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Intent: {data['intent']}")
    print(f"Response: {data['response']}\n")

if __name__ == "__main__":
    test_welcome()
    test_chat("Hello")
    test_chat("Tell me about internship domains")
    test_chat("How to use LMS?")
    test_chat("Can you help with my resume?")
    test_chat("Where is the contact information?")
    test_chat("What is the internship process?")
    test_chat("lsjdfkljsd") # Test fallback
