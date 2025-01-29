# from fastapi import APIRouter, HTTPException
# import gradio as gr
# import whisper
# from transformers import pipeline
# import imageio

# router = APIRouter(
#     prefix="/voice",
#     tags=["voice"],
# )

# model = whisper.load_model("base")

# sentiment_analysis = pipeline(
#   "sentiment-analysis",
#   framework="pt",
#   model="SamLowe/roberta-base-go_emotions"
# )

# def analyze_sentiment(text):
#   results = sentiment_analysis(text)
#   sentiment_results = {
#     result['label']:result['score'] for result in results
#   }
#   return sentiment_results

# def get_sentiment_emoji(sentiment):
#   # Define the mapping of sentiments to emojis
#   emoji_mapping = {
#     "disappointment": "😞",
#     "sadness": "😢",
#     "annoyance": "😠",
#     "neutral": "😐",
#     "disapproval": "👎",
#     "realization": "😮",
#     "nervousness": "😬",
#     "approval": "👍",
#     "joy": "😄",
#     "anger": "😡",
#     "embarrassment": "😳",
#     "caring": "🤗",
#     "remorse": "😔",
#     "disgust": "🤢",
#     "grief": "😥",
#     "confusion": "😕",
#     "relief": "😌",
#     "desire": "😍",
#     "admiration": "😌",
#     "optimism": "😊",
#     "fear": "😨",
#     "love": "❤️",
#     "excitement": "🎉",
#     "curiosity": "🤔",
#     "amusement": "😄",
#     "surprise": "😲",
#     "gratitude": "🙏",
#     "pride": "🦁"
#   }
#   return emoji_mapping.get(sentiment, "")


# def display_sentiment_results(sentiment_results, option):
#   sentiment_text = ""
#   for sentiment, score in sentiment_results.items():
#     emoji = get_sentiment_emoji(sentiment)
#     if option == "Sentiment Only":
#       sentiment_text += f"{sentiment} {emoji}\n"
#     elif option == "Sentiment + Score":
#       sentiment_text += f"{sentiment} {emoji}: {score}\n"
#   return sentiment_text

# def inference(audio, sentiment_option):
#   audio = whisper.load_audio(audio)
#   audio = whisper.pad_or_trim(audio)

#   mel = whisper.log_mel_spectrogram(audio).to(model.device)

#   _, probs = model.detect_language(mel)
#   lang = max(probs, key=probs.get)

#   options = whisper.DecodingOptions(fp16=False)
#   result = whisper.decode(model, mel, options)

#   sentiment_results = analyze_sentiment(result.text)
#   sentiment_output = display_sentiment_results(sentiment_results, sentiment_option)

#   return lang.upper(), result.text, sentiment_output

# @router.post("/analyze")
# async def analyze_voice(audio: bytes, sentiment_option: str):
#   lang, text, sentiment_output = inference(audio, sentiment_option)
#   return {
#     "language": lang,
#     "text": text,
#     "sentiment": sentiment_output
#   }

# @router.get("/analyzeURL")
# async def analyze_voice_url(url: str, sentiment_option: str):
#   result = inference(url, sentiment_option)
#   return {
#     "language": result[0],
#     "text": result[1],
#     "sentiment": result[2]
#   }
