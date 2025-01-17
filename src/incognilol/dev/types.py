from enum import Enum
from typing import Any, Optional, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    # assert isinstance(x, list)
    return [f(y) for y in x]


class AccentColor(Enum):
    EMPTY = ""
    PURPLE = "Purple"


class Preferences:
    hide_pro_badge: int
    hide_active_ts: int
    accent_color: AccentColor
    background_color: str

    def __init__(self, hide_pro_badge: int, hide_active_ts: int, accent_color: AccentColor, background_color: str) -> None:
        self.hide_pro_badge = hide_pro_badge
        self.hide_active_ts = hide_active_ts
        self.accent_color = accent_color
        self.background_color = background_color

    @staticmethod
    def from_dict(obj: Any) -> 'Preferences':
        assert isinstance(obj, dict)
        hide_pro_badge = from_int(obj.get("hideProBadge"))
        hide_active_ts = from_int(obj.get("hideActiveTs"))
        accent_color = AccentColor(obj.get("accentColor"))
        background_color = from_str(obj.get("backgroundColor"))
        return Preferences(hide_pro_badge, hide_active_ts, accent_color, background_color)

    def to_dict(self) -> dict:
        result: dict = {}
        result["hideProBadge"] = from_int(self.hide_pro_badge)
        result["hideActiveTs"] = from_int(self.hide_active_ts)
        result["accentColor"] = to_enum(AccentColor, self.accent_color)
        result["backgroundColor"] = from_str(self.background_color)
        return result


class AwardUser:
    user_id: int
    account_id: int
    username: str
    full_name: str
    emoji_status: str
    about: str
    avatar_url: str
    profile_url: str
    is_active_pro: bool
    is_active_pro_plus: bool
    is_verified_account: bool
    creation_ts: int
    active_ts: int
    preferences: Preferences

    def __init__(self, user_id: int, account_id: int, username: str, full_name: str, emoji_status: str, about: str, avatar_url: str, profile_url: str, is_active_pro: bool, is_active_pro_plus: bool, is_verified_account: bool, creation_ts: int, active_ts: int, preferences: Preferences) -> None:
        self.user_id = user_id
        self.account_id = account_id
        self.username = username
        self.full_name = full_name
        self.emoji_status = emoji_status
        self.about = about
        self.avatar_url = avatar_url
        self.profile_url = profile_url
        self.is_active_pro = is_active_pro
        self.is_active_pro_plus = is_active_pro_plus
        self.is_verified_account = is_verified_account
        self.creation_ts = creation_ts
        self.active_ts = active_ts
        self.preferences = preferences

    @staticmethod
    def from_dict(obj: Any) -> 'AwardUser':
        assert isinstance(obj, dict)
        user_id = int(from_str(obj.get("userId")))
        account_id = int(from_str(obj.get("accountId")))
        username = from_str(obj.get("username"))
        full_name = from_str(obj.get("fullName"))
        emoji_status = from_str(obj.get("emojiStatus"))
        about = from_str(obj.get("about"))
        avatar_url = from_str(obj.get("avatarUrl"))
        profile_url = from_str(obj.get("profileUrl"))
        is_active_pro = from_bool(obj.get("isActivePro"))
        is_active_pro_plus = from_bool(obj.get("isActiveProPlus"))
        is_verified_account = from_bool(obj.get("isVerifiedAccount"))
        creation_ts = from_int(obj.get("creationTs"))
        active_ts = from_int(obj.get("activeTs"))
        preferences = Preferences.from_dict(obj.get("preferences"))
        return AwardUser(user_id, account_id, username, full_name, emoji_status, about, avatar_url, profile_url, is_active_pro, is_active_pro_plus, is_verified_account, creation_ts, active_ts, preferences)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userId"] = from_str(str(self.user_id))
        result["accountId"] = from_str(str(self.account_id))
        result["username"] = from_str(self.username)
        result["fullName"] = from_str(self.full_name)
        result["emojiStatus"] = from_str(self.emoji_status)
        result["about"] = from_str(self.about)
        result["avatarUrl"] = from_str(self.avatar_url)
        result["profileUrl"] = from_str(self.profile_url)
        result["isActivePro"] = from_bool(self.is_active_pro)
        result["isActiveProPlus"] = from_bool(self.is_active_pro_plus)
        result["isVerifiedAccount"] = from_bool(self.is_verified_account)
        result["creationTs"] = from_int(self.creation_ts)
        result["activeTs"] = from_int(self.active_ts)
        result["preferences"] = to_class(Preferences, self.preferences)
        return result


class ListType(Enum):
    COMMENT = "comment"


class Comment:
    list_type: ListType
    update_ts: int
    latest_comment_text: str
    op_token: str
    can_anonymous: bool
    pinned_comment_count: int

    def __init__(self, list_type: ListType, update_ts: int, latest_comment_text: str, op_token: str, can_anonymous: bool, pinned_comment_count: int) -> None:
        self.list_type = list_type
        self.update_ts = update_ts
        self.latest_comment_text = latest_comment_text
        self.op_token = op_token
        self.can_anonymous = can_anonymous
        self.pinned_comment_count = pinned_comment_count

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        list_type = ListType(obj.get("listType"))
        update_ts = from_int(obj.get("updateTs"))
        latest_comment_text = from_str(obj.get("latestCommentText"))
        op_token = from_str(obj.get("opToken"))
        can_anonymous = from_bool(obj.get("canAnonymous"))
        pinned_comment_count = from_int(obj.get("pinnedCommentCount"))
        return Comment(list_type, update_ts, latest_comment_text, op_token, can_anonymous, pinned_comment_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["listType"] = to_enum(ListType, self.list_type)
        result["updateTs"] = from_int(self.update_ts)
        result["latestCommentText"] = from_str(self.latest_comment_text)
        result["opToken"] = from_str(self.op_token)
        result["canAnonymous"] = from_bool(self.can_anonymous)
        result["pinnedCommentCount"] = from_int(self.pinned_comment_count)
        return result


class Image:
    width: int
    height: int
    url: str
    webp_url: Optional[str]

    def __init__(self, width: int, height: int, url: str, webp_url: Optional[str]) -> None:
        self.width = width
        self.height = height
        self.url = url
        self.webp_url = webp_url

    @staticmethod
    def from_dict(obj: Any) -> 'Image':
        assert isinstance(obj, dict)
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        url = from_str(obj.get("url"))
        webp_url = from_union([from_str, from_none], obj.get("webpUrl"))
        return Image(width, height, url, webp_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["url"] = from_str(self.url)
        if self.webp_url is not None:
            result["webpUrl"] = from_union([from_str, from_none], self.webp_url)
        return result


class Image460Sv:
    width: int
    height: int
    url: str
    has_audio: int
    duration: int
    vp8_url: str
    h265_url: str
    vp9_url: str
    av1_url: Optional[str]

    def __init__(self, width: int, height: int, url: str, has_audio: int, duration: int, vp8_url: str, h265_url: str, vp9_url: str, av1_url: Optional[str]) -> None:
        self.width = width
        self.height = height
        self.url = url
        self.has_audio = has_audio
        self.duration = duration
        self.vp8_url = vp8_url
        self.h265_url = h265_url
        self.vp9_url = vp9_url
        self.av1_url = av1_url

    @staticmethod
    def from_dict(obj: Any) -> 'Image460Sv':
        assert isinstance(obj, dict)
        width = from_int(obj.get("width"))
        height = from_int(obj.get("height"))
        url = from_str(obj.get("url"))
        has_audio = from_int(obj.get("hasAudio"))
        duration = from_int(obj.get("duration"))
        vp8_url = from_str(obj.get("vp8Url"))
        h265_url = from_str(obj.get("h265Url"))
        vp9_url = from_str(obj.get("vp9Url"))
        av1_url = from_union([from_str, from_none], obj.get("av1Url"))
        return Image460Sv(width, height, url, has_audio, duration, vp8_url, h265_url, vp9_url, av1_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["width"] = from_int(self.width)
        result["height"] = from_int(self.height)
        result["url"] = from_str(self.url)
        result["hasAudio"] = from_int(self.has_audio)
        result["duration"] = from_int(self.duration)
        result["vp8Url"] = from_str(self.vp8_url)
        result["h265Url"] = from_str(self.h265_url)
        result["vp9Url"] = from_str(self.vp9_url)
        if self.av1_url is not None:
            result["av1Url"] = from_union([from_str, from_none], self.av1_url)
        return result


class Images:
    image700: Image
    image460: Image
    image_fb_thumbnail: Image
    image460_sv: Optional[Image460Sv]

    def __init__(self, image700: Image, image460: Image, image_fb_thumbnail: Image, image460_sv: Optional[Image460Sv]) -> None:
        self.image700 = image700
        self.image460 = image460
        self.image_fb_thumbnail = image_fb_thumbnail
        self.image460_sv = image460_sv

    @staticmethod
    def from_dict(obj: Any) -> 'Images':
        assert isinstance(obj, dict)
        image700 = Image.from_dict(obj.get("image700"))
        image460 = Image.from_dict(obj.get("image460"))
        image_fb_thumbnail = Image.from_dict(obj.get("imageFbThumbnail"))
        image460_sv = from_union([Image460Sv.from_dict, from_none], obj.get("image460sv"))
        return Images(image700, image460, image_fb_thumbnail, image460_sv)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image700"] = to_class(Image, self.image700)
        result["image460"] = to_class(Image, self.image460)
        result["imageFbThumbnail"] = to_class(Image, self.image_fb_thumbnail)
        if self.image460_sv is not None:
            result["image460sv"] = from_union([lambda x: to_class(Image460Sv, x), from_none], self.image460_sv)
        return result


class PostSection:
    name: str
    url: str
    image_url: str

    def __init__(self, name: str, url: str, image_url: str) -> None:
        self.name = name
        self.url = url
        self.image_url = image_url

    @staticmethod
    def from_dict(obj: Any) -> 'PostSection':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        url = from_str(obj.get("url"))
        image_url = from_str(obj.get("imageUrl"))
        return PostSection(name, url, image_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["url"] = from_str(self.url)
        result["imageUrl"] = from_str(self.image_url)
        return result


class Tag:
    key: str
    url: str

    def __init__(self, key: str, url: str) -> None:
        self.key = key
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'Tag':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        url = from_str(obj.get("url"))
        return Tag(key, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        result["url"] = from_str(self.url)
        return result


class TypeEnum(Enum):
    ANIMATED = "Animated"
    PHOTO = "Photo"


class Post:
    id: str
    url: str
    title: str
    description: str
    type: TypeEnum
    nsfw: int
    up_vote_count: int
    down_vote_count: int
    creation_ts: int
    promoted: int
    badges: List[Any]
    gam_flagged: bool
    is_vote_masked: int
    has_long_post_cover: int
    images: Images
    source_domain: str
    source_url: str
    award_users: List[AwardUser]
    award_state: int
    award_users_count: int
    super_vote_points: int
    super_vote_users_count: int
    creator: Optional[AwardUser]
    is_anonymous: bool
    comments_count: int
    comment: Comment
    post_section: PostSection
    tags: List[Tag]
    annotation_tags: List[str]
    interests: List[str]

    def __init__(self, id: str, url: str, title: str, description: str, type: TypeEnum, nsfw: int, up_vote_count: int, down_vote_count: int, creation_ts: int, promoted: int, badges: List[Any], gam_flagged: bool, is_vote_masked: int, has_long_post_cover: int, images: Images, source_domain: str, source_url: str, award_users: List[AwardUser], award_state: int, award_users_count: int, super_vote_points: int, super_vote_users_count: int, creator: Optional[AwardUser], is_anonymous: bool, comments_count: int, comment: Comment, post_section: PostSection, tags: List[Tag], annotation_tags: List[str], interests: List[str]) -> None:
        self.id = id
        self.url = url
        self.title = title
        self.description = description
        self.type = type
        self.nsfw = nsfw
        self.up_vote_count = up_vote_count
        self.down_vote_count = down_vote_count
        self.creation_ts = creation_ts
        self.promoted = promoted
        self.badges = badges
        self.gam_flagged = gam_flagged
        self.is_vote_masked = is_vote_masked
        self.has_long_post_cover = has_long_post_cover
        self.images = images
        self.source_domain = source_domain
        self.source_url = source_url
        self.award_users = award_users
        self.award_state = award_state
        self.award_users_count = award_users_count
        self.super_vote_points = super_vote_points
        self.super_vote_users_count = super_vote_users_count
        self.creator = creator
        self.is_anonymous = is_anonymous
        self.comments_count = comments_count
        self.comment = comment
        self.post_section = post_section
        self.tags = tags
        self.annotation_tags = annotation_tags
        self.interests = interests

    @staticmethod
    def from_dict(obj: Any) -> 'Post':
        assert isinstance(obj, dict)
        id = from_str(obj.get("id"))
        url = from_str(obj.get("url"))
        title = from_str(obj.get("title"))
        description = from_str(obj.get("description"))
        type = TypeEnum(obj.get("type"))
        nsfw = from_int(obj.get("nsfw"))
        up_vote_count = from_int(obj.get("upVoteCount"))
        down_vote_count = from_int(obj.get("downVoteCount"))
        creation_ts = from_int(obj.get("creationTs"))
        promoted = from_int(obj.get("promoted"))
        badges = from_list(lambda x: x, obj.get("badges"))
        gam_flagged = from_bool(obj.get("gamFlagged"))
        is_vote_masked = from_int(obj.get("isVoteMasked"))
        has_long_post_cover = from_int(obj.get("hasLongPostCover"))
        images = Images.from_dict(obj.get("images"))
        source_domain = from_str(obj.get("sourceDomain"))
        source_url = from_str(obj.get("sourceUrl"))
        award_users = from_list(AwardUser.from_dict, obj.get("awardUsers"))
        award_state = from_int(obj.get("awardState"))
        award_users_count = from_int(obj.get("awardUsersCount"))
        super_vote_points = from_int(obj.get("superVotePoints"))
        super_vote_users_count = from_int(obj.get("superVoteUsersCount"))
        creator = from_union([AwardUser.from_dict, from_none], obj.get("creator"))
        is_anonymous = from_bool(obj.get("isAnonymous"))
        comments_count = from_int(obj.get("commentsCount"))
        comment = Comment.from_dict(obj.get("comment"))
        post_section = PostSection.from_dict(obj.get("postSection"))
        tags = from_list(Tag.from_dict, obj.get("tags"))
        annotation_tags = from_list(from_str, obj.get("annotationTags"))
        interests = from_list(from_str, obj.get("interests"))
        return Post(id, url, title, description, type, nsfw, up_vote_count, down_vote_count, creation_ts, promoted, badges, gam_flagged, is_vote_masked, has_long_post_cover, images, source_domain, source_url, award_users, award_state, award_users_count, super_vote_points, super_vote_users_count, creator, is_anonymous, comments_count, comment, post_section, tags, annotation_tags, interests)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_str(self.id)
        result["url"] = from_str(self.url)
        result["title"] = from_str(self.title)
        result["description"] = from_str(self.description)
        result["type"] = to_enum(TypeEnum, self.type)
        result["nsfw"] = from_int(self.nsfw)
        result["upVoteCount"] = from_int(self.up_vote_count)
        result["downVoteCount"] = from_int(self.down_vote_count)
        result["creationTs"] = from_int(self.creation_ts)
        result["promoted"] = from_int(self.promoted)
        result["badges"] = from_list(lambda x: x, self.badges)
        result["gamFlagged"] = from_bool(self.gam_flagged)
        result["isVoteMasked"] = from_int(self.is_vote_masked)
        result["hasLongPostCover"] = from_int(self.has_long_post_cover)
        result["images"] = to_class(Images, self.images)
        result["sourceDomain"] = from_str(self.source_domain)
        result["sourceUrl"] = from_str(self.source_url)
        result["awardUsers"] = from_list(lambda x: to_class(AwardUser, x), self.award_users)
        result["awardState"] = from_int(self.award_state)
        result["awardUsersCount"] = from_int(self.award_users_count)
        result["superVotePoints"] = from_int(self.super_vote_points)
        result["superVoteUsersCount"] = from_int(self.super_vote_users_count)
        result["creator"] = from_union([lambda x: to_class(AwardUser, x), from_none], self.creator)
        result["isAnonymous"] = from_bool(self.is_anonymous)
        result["commentsCount"] = from_int(self.comments_count)
        result["comment"] = to_class(Comment, self.comment)
        result["postSection"] = to_class(PostSection, self.post_section)
        result["tags"] = from_list(lambda x: to_class(Tag, x), self.tags)
        result["annotationTags"] = from_list(from_str, self.annotation_tags)
        result["interests"] = from_list(from_str, self.interests)
        return result


class Data:
    next_cursor: str
    feed_id: str
    posts: List[Post]
    tags: List[Tag]

    def __init__(self, next_cursor: str, feed_id: str, posts: List[Post], tags: List[Tag]) -> None:
        self.next_cursor = next_cursor
        self.feed_id = feed_id
        self.posts = posts
        self.tags = tags

    @staticmethod
    def from_dict(obj: Any) -> 'Data':
        assert isinstance(obj, dict)
        next_cursor = from_str(obj.get("nextCursor"))
        feed_id = from_str(obj.get("feedId"))
        posts = from_list(Post.from_dict, obj.get("posts"))
        # tags = from_list(Tag.from_dict, obj.get("tags"))
        tags = []
        return Data(next_cursor, feed_id, posts, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nextCursor"] = from_str(self.next_cursor)
        result["feedId"] = from_str(self.feed_id)
        result["posts"] = from_list(lambda x: to_class(Post, x), self.posts)
        result["tags"] = from_list(lambda x: to_class(Tag, x), self.tags)
        return result


class Meta:
    timestamp: int
    status: str
    sid: str

    def __init__(self, timestamp: int, status: str, sid: str) -> None:
        self.timestamp = timestamp
        self.status = status
        self.sid = sid

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        timestamp = from_int(obj.get("timestamp"))
        status = from_str(obj.get("status"))
        sid = from_str(obj.get("sid"))
        return Meta(timestamp, status, sid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["timestamp"] = from_int(self.timestamp)
        result["status"] = from_str(self.status)
        result["sid"] = from_str(self.sid)
        return result


class APIType:
    meta: Meta
    data: Data

    def __init__(self, meta: Meta, data: Data) -> None:
        self.meta = meta
        self.data = data

    @staticmethod
    def from_dict(obj: Any) -> 'APIType':
        assert isinstance(obj, dict)
        meta = Meta.from_dict(obj.get("meta"))
        data = Data.from_dict(obj.get("data"))
        return APIType(meta, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["meta"] = to_class(Meta, self.meta)
        result["data"] = to_class(Data, self.data)
        return result


def api_type_from_dict(s: Any) -> APIType:
    return APIType.from_dict(s)


def api_type_to_dict(x: APIType) -> Any:
    return to_class(APIType, x)
