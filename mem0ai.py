from mem0 import MemoryClient
client = MemoryClient(api_key="m0-rjFKgivAZxiq5tZK49SyZIKV8jhGJQ15HJml5jpQ")
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]
client.add(messages, user_id="alex")
messages = [
    {"role": "user", "content": "I'm planning a trip to Japan next month."},
    {"role": "assistant", "content": "That's exciting, Alex! A trip to Japan next month sounds wonderful. Would you like some recommendations for vegetarian-friendly restaurants in Japan?"},
    {"role": "user", "content": "Yes, please! Especially in Tokyo."},
    {"role": "assistant", "content": "Great! I'll remember that you're interested in vegetarian restaurants in Tokyo for your upcoming trip. I'll prepare a list for you in our next interaction."}
]
client.add(messages, user_id="alex123", session_id="trip-planning-2024")
messages = [
    {"role": "system", "content": "You are a personalized travel assistant. Remember user preferences and provide tailored recommendations."},
    {"role": "assistant", "content": "Understood. I'll maintain personalized travel preferences for each user and provide customized recommendations based on their dietary restrictions, interests, and past interactions."}
]
client.add(messages, agent_id="travel-assistant")
query = "What do you know about me?"
client.search(query, user_id="alex")
