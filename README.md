# IncogniLOL

IncogniLOL is a free and open source front end for [9GAG](https://9gag.com) that is lightweight without JS, uses modern formats (such as webp instead of jpg and webm instead of mp4) to save on bandwidth and does not include any tracking elements or bloat of 9GAG.

Currently, it is in very early development and does not support browsing tags, or proxying the images. The interface is also subject to active and heavy change.

### Progress:
If you wish to follow the updates to the project, you can do so at [ilol.m3r.one](https://ilol.m3r.one) (not up yet).

This project is subject to breaking changes at the moment. Please use and deploy it at your own risk.

Also feel free to open an issue or pr for a functionality/design change you may want to see.

### Installing (primarily for development):
This project currently does not have prebuilt binaries or docker images. However, you can clone the repo and `docker compose up -d` to have the app up and running on port 22416 (or `python3 start.py` on port 5000 if you do not wish to use docker). Keep in mind that the server is Flask's builtin one, so do not expose it to the internet freely just to be safe.

### TODO:

 - [ ] Configurable proxy option for images/videos
 - [ ] Move to tailwind
 - [ ] Support for tag scrolling (maybe)
 - [ ] Support for comments (maybe)
 - [ ] Server-wide support to disable NSFW posts (most likely, I dont know)
