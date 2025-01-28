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

model2 = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="I want you to act as an AI-powered customer sentiment analysis tool. Given a bunch of customer reviews, analyze it and provide the following insights:\n1. Time Series Analysis: Perform a time series analysis of the sentiment over time. Identify trends such as:\nHow sentiment fluctuates by day/week/month.\nPeaks of negative sentiment or improvement in customer feedback.\nAny correlation between sentiment changes and external events, promotions, or changes in product/service.\n2. Overall Sentiment Analysis: Determine the overall sentiment of the reviews (positive, neutral, or negative) and provide a confidence score on a scale of 0 to 1 for each review.\n3. Key Emotions and their net value from 0 to 1.\n\nGive output in this sample format:\n{\"Fluctuation\":[0.5,0.6,0.4,0.2,0.5],\n\"Overall Analysis\":\"The review was generally positive\",\n\"Key Emotions\":{\"anger\":0.5, \"happy\":0.7},\nrecommendations: [\"Gather more data: Collect more reviews over a longer period to perform a meaningful time series analysis and identify trends.\",\"Monitor reviews regularly: Track sentiment changes over time to identify and address issues promptly.\"]\n}\n",
)

chat_session2 = model2.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Review: \"The product quality is amazing, and I love how it works seamlessly with my existing setup.\"\nTimestamp: 2025-01-10 08:45:00\n\nReview: \"The delivery was delayed, and the customer service didn’t offer any help.\"\nTimestamp: 2025-01-11 15:30:00\n\nReview: \"I’m happy with the service, though the price could be a little lower.\"\nTimestamp: 2025-01-12 10:20:00\n\nReview: \"The app crashed on me multiple times, and I couldn’t even use the features I paid for.\"\nTimestamp: 2025-01-13 14:00:00\n\nReview: \"Excellent experience, the product arrived on time and met all my expectations!\"\nTimestamp: 2025-01-14 09:00:00\n\nReview: \"The food quality was great, but the wait time was a little too long for my taste.\"\nTimestamp: 2025-01-15 18:15:00\n\nReview: \"I had an issue with my order, and the support team didn’t resolve it quickly enough.\"\nTimestamp: 2025-01-16 11:30:00\n\nReview: \"I’m really pleased with the customer service. They helped me right away when I had a question.\"\nTimestamp: 2025-01-17 13:45:00\n\nReview: \"The product is okay, but I had expected more based on the description.\"\nTimestamp: 2025-01-18 07:30:00\n\nReview: \"I’m extremely disappointed. My order was wrong, and the replacement didn’t come until much later.\"\nTimestamp: 2025-01-19 16:00:00\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "{\n  \"Fluctuation\": [\n    0.8,\n    0.2,\n    0.6,\n    0.1, \n    0.9,\n    0.5, \n    0.3, \n    0.7,\n    0.4,\n    0.0 \n  ],\n  \"Overall Analysis\": \"The overall sentiment is somewhat mixed, with a noticeable number of negative reviews related to customer service and order issues.\",\n  \"Key Emotions\": {\n    \"joy\": 0.45,\n    \"satisfaction\": 0.3,\n    \"frustration\": 0.4,\n    \"disappointment\": 0.35,\n    \"anger\": 0.2\n  },\n  \"recommendations\": [\n    \"Investigate and address the recurring issues with customer service and order fulfillment.  Negative reviews related to these areas are impacting overall sentiment.\",\n    \"Monitor customer service response times and efficiency.  Ensure timely resolution of customer issues.\",\n    \"Review product descriptions and ensure they accurately reflect the product features and functionalities to manage customer expectations.\",\n    \"Consider offering compensation to customers who experienced significant delays or incorrect orders. This could help mitigate negative sentiment and improve customer loyalty.\" ,\n    \"Gather more data: Collect more reviews over a longer period to perform a meaningful time series analysis and identify trends.\",\n    \"Monitor reviews regularly: Track sentiment changes over time to identify and address issues promptly.\"\n  ]\n}\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Review: \"I love the design and functionality of this product. It works perfectly for my needs.\"\nTimestamp: 2025-01-20 08:00:00\n\nReview: \"The customer service was unhelpful, and I had to wait a long time for a response.\"\nTimestamp: 2025-01-21 14:20:00\n\nReview: \"The food was cold when it arrived, and the portion size was smaller than expected.\"\nTimestamp: 2025-01-22 12:10:00\n\nReview: \"I’ve been using this app for a while, and I am very satisfied with the performance.\"\nTimestamp: 2025-01-23 09:45:00\n\nReview: \"The checkout process was slow, but the product quality made up for it.\"\nTimestamp: 2025-01-24 17:30:00\n\nReview: \"I’m highly dissatisfied with the packaging. It was damaged, and my items were missing.\"\nTimestamp: 2025-01-25 10:05:00\n\nReview: \"The product is good, but I would like to see more color options.\"\nTimestamp: 2025-01-26 16:00:00\n\nReview: \"Fantastic experience! Fast delivery and the product exceeded my expectations.\"\nTimestamp: 2025-01-27 11:15:00\n\nReview: \"Not what I expected. The product didn’t work as described and was difficult to set up.\"\nTimestamp: 2025-01-28 08:30:00\n\nReview: \"Great value for money. I’ve recommended this to all my friends!\"\nTimestamp: 2025-01-29 19:00:00\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\n  \"Fluctuation\": [\n    0.9, \n    0.2, \n    0.3, \n    0.8, \n    0.6, \n    0.1, \n    0.5, \n    1.0, \n    0.0, \n    0.7\n  ],\n  \"Overall Analysis\": \"Sentiment is mixed. While there are positive comments about product functionality and value, negative feedback regarding customer service, delivery, and packaging issues persists.\",\n  \"Key Emotions\": {\n    \"joy\": 0.4,\n    \"satisfaction\": 0.35,\n    \"frustration\": 0.3,\n    \"disappointment\": 0.4,\n    \"anger\": 0.25\n  },\n  \"recommendations\": [\n    \"Prioritize addressing the recurring negative feedback themes: customer service responsiveness, delivery (including temperature and portion size for food), and packaging quality/damage. These are consistently impacting customer satisfaction.\",\n    \"Proactively communicate with customers regarding potential delays or issues. Transparency can mitigate frustration.\",\n    \"Investigate the reasons behind damaged packaging and missing items. Implement quality control measures to minimize such incidents.\",\n    \"Consider offering various compensation options to affected customers (e.g., refunds, replacements, discounts) to improve their experience and rebuild trust.\",\n    \"While positive feedback on product functionality and value is encouraging, don't let the recurring negative issues overshadow these strengths. Address them promptly to improve overall customer sentiment.\"\n  ]\n}\n```\n",
      ],
    },
  ]
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

@router.get("/predictOverall")
async def predictOverall(input: str):
    response = chat_session2.send_message(input)
    response_json = json.loads(response.text.replace("```", "").replace("json", "").replace("\n", ""))
    return response_json