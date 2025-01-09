import os 

def export_vars(request):
    data = {}
    data['APP_NAME'] = os.environ['APP_NAME']
    data['FACEBOOK_URL'] = os.environ['FACEBOOK_URL']
    data['INSTAGRAM_URL'] = os.environ['INSTAGRAM_URL']
    data['LINKEDIN_URL'] = os.environ['LINKEDIN_URL']
    data['TWITTER_URL'] = os.environ['TWITTER_URL']
    data['YOUTUBE_URL'] = os.environ['YOUTUBE_URL']
    data['APP_ADDRESS'] = os.environ['APP_ADDRESS']
    data['APP_EMAIL_ID'] = os.environ['APP_EMAIL_ID']
    data['APP_PHONE_NO'] = os.environ['APP_PHONE_NO']
    data['APP_EMBEDED_URL'] = os.environ['APP_EMBEDED_URL']
    return data