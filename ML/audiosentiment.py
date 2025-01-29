# API_KEY_ASSEMBLYAI = "927184ddfa9d40c683e53cec3ff668e2"

# import json
# from yt_extractor import get_audio_url, get_video_info
# import assemblyai as aai
# import requests
# import time

# upload_endpoint = 'https://api.assemblyai.com/v2/upload'
# transcript_endpoint = 'https://api.assemblyai.com/v2/transcript'

# headers_auth_only = {'authorization': API_KEY_ASSEMBLYAI}

# headers = {
#     "authorization": API_KEY_ASSEMBLYAI,
#     "content-type": "application/json"
# }

# CHUNK_SIZE = 5_242_880  # 5MB


# def upload(filename):
#     def read_file(filename):
#         with open(filename, 'rb') as f:
#             while True:
#                 data = f.read(CHUNK_SIZE)
#                 if not data:
#                     break
#                 yield data

#     upload_response = requests.post(upload_endpoint, headers=headers_auth_only, data=read_file(filename))
#     return upload_response.json()['upload_url']


# def transcribe(audio_url, sentiment_analysis):
#     transcript_request = {
#         'audio_url': audio_url,
#         'sentiment_analysis': sentiment_analysis
#     }

#     transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
#     return transcript_response.json()['id']

        
# def poll(transcript_id):
#     polling_endpoint = transcript_endpoint + '/' + transcript_id
#     polling_response = requests.get(polling_endpoint, headers=headers)
#     return polling_response.json()


# def get_transcription_result_url(url, sentiment_analysis):
#     transcribe_id = transcribe(url, sentiment_analysis)
#     while True:
#         data = poll(transcribe_id)
#         if data['status'] == 'completed':
#             print("Transcription completed:", data)  # Debugging: print the response
#             return data, None
#         elif data['status'] == 'error':
#             print("Error in transcription:", data)  # Debugging: print the error response
#             return data, data['error']
            
#         print("Waiting for 30 seconds...")
#         time.sleep(30)

        
        
# def save_transcript(url, title, sentiment_analysis=False):
#     data, error = get_transcription_result_url(url, sentiment_analysis)
#     if data:
#         if 'text' in data and data['text']:  # Check if 'text' exists and is not None
#             filename = title + '.txt'
#             with open(filename, 'w') as f:
#                 f.write(data['text'])
#             print(f'Transcript saved to {filename}')
#         else:
#             print(f"Transcript text is missing in the response: {data}")

#         if sentiment_analysis and 'sentiment_analysis_results' in data:   
#             filename = title + '_sentiments.json'
#             with open(filename, 'w') as f:
#                 sentiments = data['sentiment_analysis_results']
#                 json.dump(sentiments, f, indent=4)
#             print(f"Sentiment analysis results saved to {filename}")

#         return True
#     elif error:
#         print("Error:", error)
#         return False


# def save_video_sentiments(url):
#     video_info = get_video_info(url)
#     url = get_audio_url(url)
#     if url:
#         title = video_info['title']
#         title = title.strip().replace(" ", "_")
#         title = "data/" + title
#         save_transcript(url, title, sentiment_analysis=True)

# if __name__ == "__main__":
#     save_video_sentiments("https://youtu.be/e-kSGNzu0hM")
    

import gradio as gr
import whisper
from transformers import pipeline

model = whisper.load_model("base")

sentiment_analysis = pipeline(
  "sentiment-analysis",
  framework="pt",
  model="SamLowe/roberta-base-go_emotions"
)

def analyze_sentiment(text):
  results = sentiment_analysis(text)
  sentiment_results = {
    result['label']:result['score'] for result in results
  }
  return sentiment_results

def get_sentiment_emoji(sentiment):
  # Define the mapping of sentiments to emojis
  emoji_mapping = {
    "disappointment": "😞",
    "sadness": "😢",
    "annoyance": "😠",
    "neutral": "😐",
    "disapproval": "👎",
    "realization": "😮",
    "nervousness": "😬",
    "approval": "👍",
    "joy": "😄",
    "anger": "😡",
    "embarrassment": "😳",
    "caring": "🤗",
    "remorse": "😔",
    "disgust": "🤢",
    "grief": "😥",
    "confusion": "😕",
    "relief": "😌",
    "desire": "😍",
    "admiration": "😌",
    "optimism": "😊",
    "fear": "😨",
    "love": "❤️",
    "excitement": "🎉",
    "curiosity": "🤔",
    "amusement": "😄",
    "surprise": "😲",
    "gratitude": "🙏",
    "pride": "🦁"
  }
  return emoji_mapping.get(sentiment, "")

def display_sentiment_results(sentiment_results, option):
  sentiment_text = ""
  for sentiment, score in sentiment_results.items():
    emoji = get_sentiment_emoji(sentiment)
    if option == "Sentiment Only":
      sentiment_text += f"{sentiment} {emoji}\n"
    elif option == "Sentiment + Score":
      sentiment_text += f"{sentiment} {emoji}: {score}\n"
  return sentiment_text

print(analyze_sentiment("I am very happy"))

def inference(audio, sentiment_option):
  audio = whisper.load_audio(audio)
  audio = whisper.pad_or_trim(audio)

  mel = whisper.log_mel_spectrogram(audio).to(model.device)

  _, probs = model.detect_language(mel)
  lang = max(probs, key=probs.get)

  options = whisper.DecodingOptions(fp16=False)
  result = whisper.decode(model, mel, options)

  sentiment_results = analyze_sentiment(result.text)
  sentiment_output = display_sentiment_results(sentiment_results, sentiment_option)

  return lang.upper(), result.text, sentiment_output

result = inference("https://rr3---sn-qxaelned.googlevideo.com/videoplayback?expire=1738104385&ei=4QmZZ_OzOcnP9fwPxNf3kAU&ip=139.5.198.26&id=o-ACqJVc2N2vMYxjK_7W17Q8gPB0U3l66wvovApzu0OB8-&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1738082785%2C&mh=6o&mm=31%2C26&mn=sn-qxaelned%2Csn-cvh7knzr&ms=au%2Conr&mv=m&mvi=3&pl=24&rms=au%2Cau&initcwndbps=1220000&bui=AY2Et-OrErOHKFw0r0BE4IsFPdwu0FAnR53-wzMG5skbrWO6mK-9JQgXT3bCBR0lnaacX4M-8SoJbfwG&vprv=1&svpuc=1&mime=audio%2Fmp4&ns=m-nSeNDHswUViNndLY-Q538Q&rqh=1&gir=yes&clen=2299830&dur=142.059&lmt=1703336187893809&mt=1738082475&fvip=5&keepalive=yes&lmw=1&fexp=51326932%2C51353498%2C51371294&c=TVHTML5&sefc=1&txp=6308224&n=iENC2FSmq0TLXw&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgU3QlYdUN2K6XdBE8PxDV_hWjbDusQq33mihLdGAjqbYCIDo-5X2DJHWPH_lCPz3lg3k3NtyC3SXFBUasX60IJgZ_&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=AGluJ3MwRAIgY5yDOQ32me5jNKuela8y4qYWMtqVOIOlvFjTepDJwWICIHYOBBFDB3blttNRNvsLEA_l5JIV5nI2_580QNbsc-zu", "Sentiment Only")

print(result[1])