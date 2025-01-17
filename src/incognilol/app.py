from flask import Flask, abort, render_template
from bs4 import BeautifulSoup as bs
import requests as req
import json
from datetime import datetime
from .dev.types import api_type_from_dict

HOMEURL = "https://9gag.com/v1/feed-posts/type/home"
GAGURL = "https://9gag.com/gag/{gag}"
HEADERS = {'User-Agent' : "Mediapartners-Google"}
IMGURL = "https://img-9gag-fun.9cache.com/photo/{}_460swp.webp"
VIDURL = "https://img-9gag-fun.9cache.com/photo/{}_460svwm.webm"

class HomePost:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.upvotes:int
        self.downvotes:int
        self.op = ""
        self.nsfw:int
        self.uploaddate:int
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
        human_uploaddate = datetime.fromtimestamp(uploaddate).strftime('%d.%m.%Y %H:%M')
        likes = postinfo["upVoteCount"]
        dislikes = postinfo["downVoteCount"]
        op = postinfo["creator"]["username"] if postinfo["creator"] else "Anonymous"
        nsfw = postinfo["nsfw"]
        image, video = "", ""
        if isvid:
            video = VIDURL.format(gagid)
        elif not isvid:
            image = IMGURL.format(gagid)
        return render_template("gag.html", gag = gagid, imgurl = image, isvid = isvid, vidurl = video, title = posttitle, op = op, human_uploaddate = human_uploaddate, likes = likes, dislikes = dislikes)

    @app.route("/home", defaults={'after': ""})
    @app.route("/home/<after>")
    def home(after):
        try:
            homereq = req.get(f"{HOMEURL}?after={after}%3D", headers = HEADERS)
            homereq.raise_for_status()
        except Exception as exc:
            return render_template("error.html", error = exc)
        jsontoparse = json.loads(homereq.text)
        homefeed = api_type_from_dict(jsontoparse)
        postlistjson = [post for post in homefeed.data.posts]
        postlist = []
        for post in postlistjson:
            indpost = HomePost()
            indpost.id = post.id
            indpost.title = post.title
            indpost.op = post.creator.username if not post.is_anonymous else "Anonymous"  #type: ignore #TODO: pyright does not understand that we checked it
            indpost.nsfw = post.nsfw
            indpost.upvotes = post.up_vote_count
            indpost.downvotes = post.down_vote_count
            if post.type.value == "Photo":
                indpost.imglink = post.images.image460.webp_url or IMGURL.format(post.id) # .webp_url may return none
            elif post.type.value == "Animated":
                indpost.vidlink = post.images.image460_sv.vp9_url or VIDURL.format(post.id) #TODO: why?
                indpost.vidposter = post.images.image460.webp_url or IMGURL.format(post.id)
            indpost.uploaddate = post.creation_ts
            indpost.nextcursor = homefeed.data.next_cursor.replace("after=","").replace("%3D", "")
            postlist.append(indpost)
        return render_template("home.html", postlist = postlist)

    app.run(debug=True, host = "0.0.0.0")
    # return app

create_app()
