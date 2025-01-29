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

model3 = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="I have a collection of LinkedIn posts and tweets related to a particular service. Analyze the content of these posts and tweets to identify the following:\n\nSentiments: Determine whether the overall sentiment is positive, neutral, or negative. Provide an approximate percentage distribution for each category.\nEmotions: Identify the predominant emotions (e.g., happiness, frustration, admiration, anger, or disappointment) expressed in these posts. Provide examples to support your findings.\nKey Themes: Highlight the recurring themes or topics that people are discussing in relation to the service (e.g., ease of use, affordability, customer support, or innovation).\nInsights: Summarize actionable insights from the analysis. For instance, what aspects of the service are appreciated or criticized most? Are there any patterns in user feedback that can guide improvements?\n\nReturn output in this FORMAT ONLY:\n{\"Sentiments\":{\"Positive\":100,\"Neutral\":0,\"Negative\":0},\n\"Emotions\":{\"Pride\":\"The NMIT post expresses pride in its students' achievements as 0x.Day Fellows and their contributions to the platform. (We take immense pride...)\", \"Enthusiasm\":\"The tweets convey enthusiasm for 0x.Day's future and partnerships. \", \"Key Themes\": [\"Industry-Academia Collaboration: The NMIT post highlights the importance of bridging the gap between academia and the tech industry, praising 0x.Day's efforts in this area, especially with the 0xCampus Program.\",\"Student Success and Empowerment: The NMIT post focuses on the success of its students who became 0x.Day Fellows and how the platform has helped them develop their skills and prepare for the tech industry.\"], \"Insights\":[\"0x.Day's focus on industry-academia collaboration is resonating well and being seen as a valuable contribution. The 0xCampus Program appears to be a successful initiative.\",\"The platform's association with blockchain innovation and decentralized technologies is a key strength and driver of positive sentiment.\"]}",
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

chat_session3 = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "[\"NMIT Hacks & 0xDay: Bridging Academia and Industry, Empowering Future Tech Leaders 🌐\n\nWe are delighted to announce the recent visit of Mr. Saran Kumar, founder of 0x.Day, and Mr. Naresh Shetty, Director of Operations of 0x.Day, to Nitte Meenakshi Institute of Technology. During their interaction with our Principal, Dr. HC Nagaraj . and Dr. S. Meenakshi Sundaram, Head of the Department of Computer Science and Engineering, Mr. Kumar commended our exceptional students K Sai Uttej, Karthik Rao, and Sai Shravan Motamarri for their outstanding contributions to the 0x.Day platform and conferred upon them the title of \"0x.Day Fellows.\" ✨️\n\nAs part of his visit, Mr. Saran Kumar introduced the 0xCampus Program, a groundbreaking initiative aimed at fostering deeper industry-academia collaboration. We take immense pride in the accomplishments of our \"0x.Day Fellows\", who, through their dedication and ingenuity, have significantly contributed to advancing 0x.Day - 0xHacking.com, a decentralized hackathon platform, onto the global stage.\n\nThese students showcased exceptional leadership and technical expertise, tackling challenges with innovation and precision while collaborating with industry giants such as TON Foundation and Router Protocol. Their journey exemplifies the transformative power of decentralized technologies, blockchain innovation, and industry-focused hackathons in shaping future-ready tech professionals. 🌟\n\nWe extend our heartfelt gratitude to 0x.Day, Saran Kumar, Prashanth BM, Naresh Shetty, and their dedicated team for their invaluable partnership and commitment to bridging the gap between academia and the tech industry. This collaboration has not only enhanced our students' technical and leadership skills but also prepared them to excel in the ever-evolving technology landscape. \n\nhashtag#NMIT hashtag#NMITHacks hashtag#0xDay hashtag#Hackathon hashtag#BlockchainInnovation hashtag#IndustryAcademia hashtag#FutureTechLeaders hashtag#Partnerships hashtag#TechnologyTransformation\", \"we are 0x.Day are proud to host the TON Hacker House along with Pivot. Looking forward to a great Partnership🥂\nLFG ✌️🚀\", \"Think about it. 0x.Day is nailing the revolution in the ecosystem which has been ignored for ages.\nGreat work Captains. 👏 \nSaran Kumar - BUIDL'ng 0x.Day®, Prashanth BM\nMany more to come 😀 \nhashtag#0xHacking\"]",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```json\n{\"Sentiments\": {\"Positive\": 100, \"Neutral\": 0, \"Negative\": 0},\n\"Emotions\": {\"Pride\": \"The NMIT post expresses pride in its students' achievements as 0x.Day Fellows and their contributions to the platform. (We take immense pride...)\", \"Enthusiasm\": \"The tweets convey enthusiasm for 0x.Day's future and partnerships. (Looking forward to a great Partnership🥂 LFG ✌️🚀)\", \"Admiration\": \"The tweet praising the work of 0x.Day captains shows admiration for their efforts. (Great work Captains. 👏)\", \"Gratitude\": \"The NMIT post expresses gratitude towards 0x.Day for their partnership and commitment. (We extend our heartfelt gratitude...)\"},\n\"Key Themes\": [\"Industry-Academia Collaboration\": \"The NMIT post highlights the importance of bridging the gap between academia and the tech industry, praising 0x.Day's efforts in this area, especially with the 0xCampus Program.\", \"Student Success and Empowerment\": \"The NMIT post focuses on the success of its students who became 0x.Day Fellows and how the platform has helped them develop their skills and prepare for the tech industry.\", \"Innovation and Decentralized Technologies\": \"The posts emphasize 0x.Day's role in promoting blockchain innovation and decentralized technologies.\", \"Partnerships and Growth\": \"The tweets highlight 0x.Day's partnerships and express optimism about its future growth.\"],\n\"Insights\": [\"0x.Day's focus on industry-academia collaboration is resonating well and being seen as a valuable contribution. The 0xCampus Program appears to be a successful initiative.\", \"The platform's association with blockchain innovation and decentralized technologies is a key strength and driver of positive sentiment.\", \"Partnerships with organizations like TON Foundation and Router Protocol are viewed positively and contribute to the perception of 0x.Day as a growing and influential player in the space.\", \"Highlighting student success stories and the impact of 0x.Day on their careers can be a powerful way to further strengthen the platform's reputation and attract more talent.\"]}\n```\n",
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

@router.get("/predictLinkedIn")
async def predictLinkedIn(input: str):
    response = chat_session3.send_message(input)
    response_json = json.loads(response.text.replace("```", "").replace("json", "").replace("\n", ""))
    return response_json
