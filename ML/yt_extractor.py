import yt_dlp as youtube_dl

ydl = youtube_dl.YoutubeDL()

def get_video_info(url):
    with ydl:
        result = ydl.extract_info(
            url,
            download=False  # We just want to extract the info
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    return video

def get_audio_url(url):
    video = get_video_info(url)
    for f in video['formats']:
        if f['format_id'] == '140':
            return f['url']

    return None

# print(get_video_info('https://www.youtube.com/watch?v=MRtg6A1f2Ko'))
print(get_audio_url('https://www.youtube.com/watch?v=3AysfXKBJW8'))