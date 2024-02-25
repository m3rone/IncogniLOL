from flask import Flask, abort, render_template
from bs4 import BeautifulSoup as bs
import requests as req
import json

HOMEURL = "https://9gag.com/v1/feed-posts/type/home"
GAGURL = "https://9gag.com/gag/{gag}"
HEADERS = {'User-Agent' : "Mediapartners-Google"}
IMGURL = "https://img-9gag-fun.9cache.com/photo/{}_460swp.webp"
VIDURL = "https://img-9gag-fun.9cache.com/photo/{}_460svwm.webm"

class HomePost:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.upvotes = ""
        self.downvotes = ""
        self.op = ""
        self.nsfw = ""
        self.uploaddate = ""
        self.imglink = ""
        self.vidlink = ""
        self.vidposter = ""
        self.nextcursor = ""

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/contact")
    def contact():
        return render_template("contact.html")
    
    @app.route("/privacy")
    def privacy():
        return render_template("privacy.html")
    
    @app.route("/disclaimer")
    def disclaimer():
        return render_template("disclaimer.html")

    @app.route("/gag/<gagid>")
    def gag(gagid):
        if not len(gagid) == 7:
            abort(403)
        try:
            gagreq = req.get(GAGURL.format(gag = gagid), headers = HEADERS)
            gagreq.raise_for_status()
        except Exception as exc:
            return render_template("error.html", error = exc)
        gagreqhtml = gagreq.text
        isvid = True if "webm" in gagreqhtml else False
        soup = bs(gagreqhtml, 'html.parser')
        gag = str(soup.find_all('script')[-1])
        # with open("tmp/postinfo.txt", "w") as post:
        #     post.write(gag)
        postdata = json.loads(gag.replace("<script type=\"text/javascript\">window._config = JSON.parse(\"", "").replace("\");</script>", "").replace("\\", ""))
        postinfo = postdata["data"]["post"]
        posttitle = postinfo["title"]
        uploaddate = postinfo["creationTs"]
        likes = postinfo["upVoteCount"]
        dislikes = postinfo["downVoteCount"]
        op = postinfo["creator"]["username"]
        nsfw = postinfo["nsfw"]
        image, video = "", ""
        if isvid:
            video = VIDURL.format(gagid)
        elif not isvid:
            image = IMGURL.format(gagid)
        return render_template("gag.html", gag = gagid, imgurl = image, isvid = isvid, vidurl = video, title = posttitle, op = op, uploaddate = uploaddate, likes = likes, dislikes = dislikes)

    @app.route("/home", defaults={'after': ""})
    @app.route("/home/<after>")
    def home(after):
        try:
            homereq = req.get(f"{HOMEURL}?after={after}%3D", headers = HEADERS)
            homereq.raise_for_status()
        except Exception as exc:
            return render_template("error.html", error = exc)
        homejson = json.loads(homereq.text)
        postlistjson = [post for post in homejson["data"]["posts"]]
        postlist = []
        for post in postlistjson:
            indpost = HomePost()
            indpost.id = post["id"]
            indpost.title = post['title']
            indpost.op = post['creator']['username']
            indpost.nsfw = post['nsfw']
            indpost.upvotes = post['upVoteCount']
            indpost.downvotes = post['downVoteCount']
            if post['type'] == "Photo":
                indpost.imglink = IMGURL.format(post["id"])
            elif post['type'] == "Animated":
                indpost.vidlink = VIDURL.format(post["id"])
                indpost.vidposter = IMGURL.format(post['id'])
            indpost.uploaddate = post['creationTs']
            indpost.nextcursor = homejson['data']['nextCursor'].replace("after=","").replace("%3D", "")
            postlist.append(indpost)
        return render_template("home.html", postlist = postlist)

    app.run(debug=True)
    # return app

create_app()
