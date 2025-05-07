import re


from dotsi import Dict
def json_to_dotsi(data):
    
    return Dict(data)


    

def is_youtube_video_link(link):
    if not link or not isinstance(link, str):
        return False

    link = link.strip()

    pattern = r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]{11}'

    return re.match(pattern, link) is not None