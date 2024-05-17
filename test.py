from flask import Flask, jsonify, request
from flask_cors import CORS
import time
from clickScreen import executeCommand
from threading import Timer


app = Flask(__name__)
CORS(app)  
url_timestamp = {}
url_viewtime = {}
prev_url = ""

def url_strip(url):
    if "http://" in url or "https://" in url:
        url = url.replace("https://", '').replace("http://", '').replace('\"', '')
    if "/" in url:
        url = url.split('/', 1)[0]
    return url


banned_tabs = []

def execute_command(url, type):
    global banned_tabs_count

    platform = None
    if "facebook" in url.lower():
        platform = "facebook"
    elif "instagram" in url.lower():
        platform = "instagram"
    elif "reddit" in url.lower():
        platform = "reddit"
    elif "twitter" in url.lower():
        platform = "twitter"
    elif "netflix" in url.lower():
        platform = "netflix"
    elif "pornhub" in url.lower():
        platform = "pornhub"
    elif "tiktok" in url.lower():
        platform = "tiktok"
    
    if platform:
        if(type == "DEL"):
            print("Closed ${platform}")
            banned_tabs.remove(platform)
        elif (type == "TAB") :
            banned_tabs.append(platform)
        print(banned_tabs)



def execute_commands_periodically():
    global banned_tabs
    if banned_tabs:
        for platform in banned_tabs:
            # Call execute_command with a dummy URL and type (adjust as needed)
            executeCommand(platform)

    # Reset timer to run after 3 minutes again
    Timer(180.0, execute_commands_periodically).start()

execute_commands_periodically()


@app.route('/send_url', methods=['POST'])
def send_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    global url_timestamp
    global url_viewtime
    global prev_url

    execute_command(parent_url, "TAB")

    """print("initial db prev tab: ", prev_url)
    print("initial db timestamp: ", url_timestamp)
    print("initial db viewtime: ", url_viewtime)"""

    if parent_url not in url_timestamp.keys():
        url_viewtime[parent_url] = 0

    if prev_url != '':
        time_spent = int(time.time() - url_timestamp[prev_url])
        url_viewtime[prev_url] = url_viewtime[prev_url] + time_spent

    x = int(time.time())
    url_timestamp[parent_url] = x
    prev_url = parent_url
    #print("final timestamps: ", url_timestamp)
    #print("final viewtimes: ", url_viewtime)

    return jsonify({'message': 'success!'}), 200

@app.route('/quit_url', methods=['POST'])
def quit_url():
    resp_json = request.get_data()
    params = resp_json.decode()
    url = params.replace("url=", "")
    print("currently viewing: " + url_strip(url))
    parent_url = url_strip(url)

    execute_command(parent_url, "DEL")
    resp_json = request.get_data()
    print("Url closed: " + resp_json.decode())
    return jsonify({'message': 'quit success!'}), 200

app.run(host='0.0.0.0', port=5000)

