import json

# Example JSON as a string
json_text = '''
{
  "Sentiment": "0.7",
  "Emotion": ["Satisfaction"],
  "Key Themes": ["Food Quality"],
  "Pain Points": [],
  "Urgency Level": "Low",
  "Recommendations": [
    "Maintain the quality of food",
    "Encourage more detailed reviews to understand specific aspects customers appreciate."
  ],
  "Comparative Sentiment": "Difficult to compare without more context. If most reviews are similarly short and positive, it suggests general satisfaction, but more detailed feedback would be beneficial."
}
'''

json_text.replace("'''", "")

# Parse the JSON
data = json.loads(json_text)

# Accessing elements
print(f"Sentiment: {data['Sentiment']}")
print(f"Emotion: {data['Emotion']}")
print(f"Key Themes: {data['Key Themes']}")
print(f"Pain Points: {data['Pain Points']}")
print(f"Urgency Level: {data['Urgency Level']}")
print(f"Recommendations: {', '.join(data['Recommendations'])}")
print(f"Comparative Sentiment: {data['Comparative Sentiment']}")
