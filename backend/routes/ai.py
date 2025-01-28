from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
import os
import json

router = APIRouter(
    prefix="/ai",
    tags=["ai"]
)
load_dotenv()

import google.generativeai as genai

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="I want you to act as an AI-powered customer sentiment analysis tool. Given a customer review, analyze it and provide the following insights:\n\nSentiment Analysis:\n\nClassify the sentiment as Positive, Negative, or Neutral.\nProvide a sentiment score between -1 (very negative) to +1 (very positive).\nEmotion Detection:\n\nIdentify the predominant emotions (e.g., joy, frustration, anger, excitement, disappointment).\nKey Themes/Topics:\n\nExtract the main topics or aspects mentioned in the review (e.g., product quality, customer service, delivery, pricing).\nPain Points & Improvement Areas:\n\nIdentify specific concerns or areas where the business can improve.\nUrgency Level:\n\nCategorize the review's urgency (e.g., High, Medium, Low) based on the customer's tone and sentiment.\nActionable Recommendations:\n\nSuggest practical actions the business can take to address the feedback.\nComparative Sentiment:\n\nCompare sentiment with similar reviews if possible and suggest whether the issue is an isolated incident or part of a trend.\nExample Review:\n'The delivery was late, and the support team was unhelpful. I will never order from here again.'\n\nExpected Output Format: JSON\n\n{\n\"Sentiment\": \"-0.85\",\n\"Emotion\": [\"Frustration\", \"Disappointment\"],\n\"Key Themes:\" [\"Delivery\", \"Customer Support\"],\n\"Pain Points\": [\"Late delivery\", \"Poor support service\"],\n\"Urgency Level\": \"High\",\n\"Recommendations\": [\"Improve logistics\", \"Train support staff\", \"Offer discount for inconvenience\"],\n}",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Khalsa Restaurant offers an amazing dining experience with its delicious food and warm hospitality. The variety of dishes, especially the North Indian cuisine, is impressive, and everything I tried was flavorful and fresh. The portions are generous, and the prices are reasonable. The staff is friendly, and the service is quick. It's definitely one of the best spots for a hearty meal in town. Highly recommended!\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"Sentiment\": \"0.95\",\n  \"Emotion\": [\"Joy\", \"Satisfaction\"],\n  \"Key Themes\": [\"Food Quality\", \"Hospitality\", \"North Indian Cuisine\", \"Portion Size\", \"Pricing\", \"Service\"],\n  \"Pain Points\": [],\n  \"Urgency Level\": \"Low\",\n  \"Recommendations\": [\"Maintain the quality of food and service\", \"Consider adding more variety to the menu (optional)\", \"Promote positive customer reviews on social media\"],\n  \"Comparative Sentiment\": \"This review is likely consistent with other positive reviews, suggesting a trend of customer satisfaction with Khalsa Restaurant.\"\n}\n```\n",
      ],
    },
  ]
)


@router.get("/predict")
async def predict(input: str):
    response = chat_session.send_message(input)
    response_json = json.loads(response.text.replace("```", "").replace("json", "").replace("\n", ""))
    return response_json