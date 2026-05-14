# Instagram Looter API

> **Instagram Looter is a high-reliability Instagram data API hosted on [RapidAPI](https://rapidapi.com/irrors-apis/api/instagram-looter2). Powered by smart request filtering, it delivers real-time access to public Instagram data with a 99.99% success rate.**  
> Retrieve public profiles, media, reels, hashtag feeds, location data, explore sections, and search results.

## Endpoint Index

### Identity Utilities
- [`/id` — Username from User ID](#username-from-user-id)
- [`/id` — User ID from Username](#user-id-from-username)
- [`/id-media` — Media Shortcode from Media ID](#media-shortcode-from-media-id)
- [`/id-media` — Media ID from Media URL](#media-id-from-media-url)

### User Insights
- [`/profile` — User Info by Username](#user-info-by-username)
- [`/profile2` — User Info (V2) by Username](#user-info-v2-by-username)
- [`/profile` — User Info by User ID](#user-info-by-user-id)
- [`/profile2` — User Info (V2) by User ID](#user-info-v2-by-user-id)
- [`/web-profile` — Web Profile Info by Username](#web-profile-info-by-username)
- [`/user-feeds` — Media List by User ID](#media-list-by-user-id)
- [`/user-feeds2` — Media List (V2) by User ID](#media-list-v2-by-user-id)
- [`/reels` — Reels by User ID](#reels-by-user-id)
- [`/user-reposts` — Reposts by User ID](#reposts-by-user-id)
- [`/user-tags` — Tagged Media by User ID](#tagged-media-by-user-id)
- [`/related-profiles` — Related Profiles by User ID](#related-profiles-by-user-id)
- [`/search?select=users` — Search Users by Keyword](#search-users-by-keyword)

### Media Details
- [`/post` — Media Info by URL](#media-info-by-url)
- [`/post` — Media Info by ID](#media-info-by-id)
- [`/post-dl` — Download Link by Media ID or URL](#download-link-by-media-id-or-url)
- [`/music` — Music Info by Music ID](#music-info-by-music-id)

### Hashtag Lookup
- [`/tag-feeds` — Media by Hashtag](#media-by-hashtag)
- [`/search?select=hashtags` — Search Hashtags by Keyword](#search-hashtags-by-keyword)

### Location Data
- [`/search?select=places` — Search Locations by Keyword](#search-locations-by-keyword)
- [`/location-info` — Location Info by Location ID](#location-info-by-location-id)
- [`/location-feeds` — Media by Location ID](#media-by-location-id)
- [`/cities` — Cities by Country Code](#cities-by-country-code)
- [`/locations` — Locations by City ID](#locations-by-city-id)

### Explore Feed
- [`/sections` — Explore Sections List](#explore-sections-list)
- [`/section` — Media by Explore Section ID](#media-by-explore-section-id)

### Global Search
- [`/search` — Global Search by Keyword](#global-search-by-keyword)

### Other Sections
- [Base URL](#base-url)
- [Authentication](#authentication)
- [Rate Limits](#rate-limits)
- [`fields` Parameter](#fields-parameter)
- [Error Responses](#error-responses)
- [Usage Examples](#usage-examples)
- [Important Remarks](#important-remarks)

## Base URL

```text
https://instagram-looter2.p.rapidapi.com
```

All endpoints are relative to this base URL.

## Authentication

This API is accessed through **RapidAPI**. Every request must include your RapidAPI subscription key in the request headers.

1. Sign up at [RapidAPI](https://rapidapi.com/irrors-apis/api/instagram-looter2).
2. Subscribe to the Instagram Looter2 API.
3. Copy your `X-RapidAPI-Key` from the RapidAPI dashboard.
4. Add the headers shown below to every request.

```http
x-rapidapi-key: YOUR_API_KEY
x-rapidapi-host: instagram-looter2.p.rapidapi.com
```

## Rate Limits

Rate limits and monthly quotas depend on your subscription plan.

| Plan | Price | Requests / Month | Overage | Rate Limit |
| --- | --- | --- | --- | --- |
| Basic | $0.00/mo | 150 | Hard limit | 1000 requests per hour |
| Pro | $9.90/mo | 15,000 | Hard limit | 10 requests per second |
| Ultra | $27.90/mo | 75,000 | + $0.001 per extra request | 30 requests per second |
| Mega | $75.90/mo | 250,000 | + $0.0005 per extra request | 60 requests per second |


### Custom Plans

We offer high-volume custom packages for larger workloads, including:

- 1M monthly requests
- 2M monthly requests
- 5M monthly requests
- 10M monthly requests
- 15M+ monthly requests
- Increased rate limits
- Priority support

**Contact us for custom plans:**

- **Telegram:** [@IrrorSystems](https://t.me/IrrorSystems)
- **Email:** Irrors@proton.me

## `fields` Parameter

**All endpoints** support the optional `fields` query parameter, which lets you cherry-pick the fields you need. This reduces payload size and speeds up your application.

### Syntax

| Pattern | Example | Effect |
| --- | --- | --- |
| Comma-separated fields | `fields=username,biography` | Return only `username` and `biography` |
| Dot notation | `fields=edge_followed_by.count` | Return a specific nested field |
| Array field notation | `fields=bio_links[].url` | Return only the `url` of each bio link |
| Wildcard | `fields=*.count` | Return all `count` sub-fields |
| Combined | `fields=username,bio_links[].url` | Return `username` and all bio link URLs |

### Example

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/profile?username=instagram&fields=username,biography,edge_followed_by.count" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

## Error Responses

The API uses standard HTTP status codes. Most error details are included in the response body.

| HTTP Status | Meaning | Common Cause |
| --- | --- | --- |
| `200 OK` | Success | Request was processed successfully |
| `400 Bad Request` | Invalid request | Missing or malformed required parameter |
| `401 Unauthorized` | Invalid API key | `x-rapidapi-key` is missing, invalid, or expired |
| `403 Forbidden` | Access denied | Subscription plan does not include this endpoint |
| `404 Not Found` | Resource not found | Unknown username, media ID, or location ID |
| `429 Too Many Requests` | Rate limit exceeded | Exceeded the request quota for your plan |
| `500 Internal Server Error` | API-side error | Transient Instagram API error — retry after a short delay |

> **Tip:** Always check the `status` field in the response body as a primary success indicator, in addition to the HTTP status code.

## Endpoints

### 🧩 Identity Utilities

#### Username from User ID

**`GET`** &nbsp; `/id`

Resolve the Instagram username that corresponds to a numeric user ID.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID (e.g. `25025320`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/id?id=25025320" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "username": "instagram",
    "user_id": "25025320"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| username | string | Resolved Instagram username |
| user_id | string | The numeric user ID that was queried |

##### Notes

> Pass `id` to go **ID → username**. Pass `username` instead to go the other direction (see *User ID from Username*).

---

#### User ID from Username

**`GET`** &nbsp; `/id`

Resolve the numeric Instagram user ID that corresponds to a username. Use this before calling any ID-based endpoint when you only have a username.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | Required | Instagram username (e.g. `instagram`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/id?username=instagram" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "username": "instagram",
    "user_id": "25025320"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| username | string | The queried username |
| user_id | string | Resolved numeric user ID |

##### Notes

> Same `/id` path as *Username from User ID* — the direction is controlled by which parameter you supply.

---

#### Media Shortcode from Media ID

**`GET`** &nbsp; `/id-media`

Convert a numeric Instagram media ID into its corresponding shortcode (the string used in `instagram.com/p/<shortcode>`).

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric media ID (e.g. `3040091568624969296`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/id-media?id=3040091568624969296" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "shortcode": "CowkyywjSZQ",
    "media_id": "3040091568624969296"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| shortcode | string | Media shortcode (used in `instagram.com/p/<shortcode>`) |
| media_id | string | The numeric media ID that was queried |

##### Notes

> Same `/id-media` path as *Media ID from Media URL*. Direction is controlled by which parameter you supply (`id` vs `url`).

---

#### Media ID from Media URL

**`GET`** &nbsp; `/id-media`

Extract the numeric media ID and shortcode from a full Instagram post URL. Use this to obtain a media ID before calling other media endpoints.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| url | string | Required | Full Instagram post URL (e.g. `https://www.instagram.com/p/CowkyywjSZQ/`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/id-media?url=https://www.instagram.com/p/CowkyywjSZQ/" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "shortcode": "CowkyywjSZQ",
    "media_id": "3040091568624969296"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| shortcode | string | Shortcode extracted from the URL |
| media_id | string | Resolved numeric media ID |

---

### 👤 User Insights

#### User Info by Username

**`GET`** &nbsp; `/profile`

Retrieve comprehensive V1 profile data for an Instagram user by username. Returns follower/following counts, bio links, business metadata, and account flags.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | Required | Instagram username (e.g. `instagram`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/profile?username=instagram" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "ai_agent_owner_username": null,
    "biography": "Discover what's new on Instagram 🔎✨",
    "bio_links": [
      {
        "title": "...",
        "lynx_url": "...",
        "url": "...",
        "link_type": "..."
      }
    ],
    "fb_profile_biolink": null,
    "biography_with_entities": {
      "raw_text": "Discover what's new on Instagram 🔎✨",
      "entities": []
    },
    "blocked_by_viewer": false,
    "restricted_by_viewer": null,
    "country_block": false,
    "eimu_id": "117943452927407",
    "external_url": "http://help.instagram.com/",
    "external_url_linkshimmed": "https://l.instagram.com/?u=http%3A%2F%2Fhelp.instagram.com%2F&e=AT5B38UerqRrfAcllIC6-pm0aULa5isRx_AMG8HpAtcEebWp_yOK6anTNmaVN9-ujZlDQnH2farY4_Y-HXBF27t5D_zoMf_N",
    "edge_followed_by": {
      "count": 700938922
    },
    "fbid": "17841400039600391",
    "followed_by_viewer": false,
    "edge_follow": {
      "count": 235
    },
    "follows_viewer": false,
    "full_name": "Instagram",
    "...": "(46 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| id | string | Numeric Instagram user ID |
| username | string | Instagram username |
| full_name | string | Display name |
| biography | string | Bio text |
| bio_links | array | Bio link objects — each has `url`, `title`, `link_type` |
| external_url | string | External URL listed in bio |
| profile_pic_url | string | Standard-resolution profile picture URL |
| profile_pic_url_hd | string | High-resolution profile picture URL |
| is_private | boolean | Private account flag |
| is_verified | boolean | Verified badge flag |
| is_business_account | boolean | Business account flag |
| is_professional_account | boolean | Professional account flag |
| edge_followed_by.count | integer | Follower count |
| edge_follow.count | integer | Following count |
| edge_owner_to_timeline_media.count | integer | Total post count |
| highlight_reel_count | integer | Story highlight count |
| business_category_name | string | Business category (business accounts only) |
| business_email | string | Public business e-mail (if set) |

##### Notes

> V1 uses **nested** counts (`edge_followed_by.count`). For flat integers use `/profile2`.

---

#### User Info (V2) by Username

**`GET`** &nbsp; `/profile2`

Retrieve V2 profile data by username. Returns follower/following/media counts, account type, category, and total clips count.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | Required | Instagram username |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/profile2?username=instagram" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "full_name": "Instagram",
    "is_memorialized": false,
    "is_private": false,
    "has_story_archive": null,
    "username": "instagram",
    "is_regulated_c18": false,
    "regulated_news_in_locations": [],
    "text_post_app_badge_label": "instagram",
    "show_text_post_app_badge": true,
    "pk": "25025320",
    "live_broadcast_visibility": null,
    "live_broadcast_id": null,
    "profile_pic_url": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-19/550891366_18667771684001321_1383210656577177067_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gF7hQJ_0eCA3-U69hJTKDJgXYnprH2OjDY859_uIoKXkMqqTEG4MRd5LRElN1-jPQo&_nc_ohc=eh4J-8ukxegQ7kNvwE_uPXT&_nc_gid=s7IE5aAmZekbkxqvJNjYpw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af0Qzjx76IlV_uabuqUlTeWFj34j6moh-zW2-2J4xF_kHQ&oe=69DD8E27&_nc_sid=10d13b",
    "hd_profile_pic_url_info": {
      "url": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-19/550891366_18667771684001321_1383210656577177067_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=1&_nc_oc=Q6cZ2gF7hQJ_0eCA3-U69hJTKDJgXYnprH2OjDY859_uIoKXkMqqTEG4MRd5LRElN1-jPQo&_nc_ohc=eh4J-8ukxegQ7kNvwE_uPXT&_nc_gid=s7IE5aAmZekbkxqvJNjYpw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1wYyGS0bI2rNgD33QyQ8kFoRcUn5hWwiVgLzh9GOt9Cg&oe=69DD8E27&_nc_sid=10d13b"
    },
    "is_unpublished": false,
    "mutual_followers_count": null,
    "profile_context_links_with_user_ids": null,
    "...": "(32 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| pk | string | Numeric user ID (primary key) |
| username | string | Instagram username |
| full_name | string | Display name |
| biography | string | Bio text |
| bio_links | array | Bio link objects |
| external_url | string | External link in bio |
| profile_pic_url | string | Profile picture URL |
| hd_profile_pic_url_info | object | HD profile picture with `url`, `width`, `height` |
| is_private | boolean | Private account flag |
| is_verified | boolean | Verified badge flag |
| is_business | boolean | Business account flag |
| is_professional_account | boolean | Professional account flag |
| follower_count | integer | Follower count |
| following_count | integer | Following count |
| media_count | integer | Total media count |
| total_clips_count | integer | Total Reels count |
| category | string | Account category label |
| account_type | integer | Account type code |
| fbid_v2 | string | Facebook ID V2 |

##### Notes

> V2 exposes `follower_count`, `following_count`, and `media_count` as flat integers. V1 wraps them in `edge_followed_by.count` objects.

---

#### User Info by User ID

**`GET`** &nbsp; `/profile`

Retrieve V1 profile data by numeric user ID. Returns the same fields as *User Info by Username*.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID (e.g. `25025320`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/profile?id=25025320" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "ai_agent_owner_username": null,
    "biography": "Discover what's new on Instagram 🔎✨",
    "bio_links": [
      {
        "title": "...",
        "lynx_url": "...",
        "url": "...",
        "link_type": "..."
      }
    ],
    "fb_profile_biolink": null,
    "biography_with_entities": {
      "raw_text": "Discover what's new on Instagram 🔎✨",
      "entities": []
    },
    "blocked_by_viewer": false,
    "restricted_by_viewer": null,
    "country_block": false,
    "eimu_id": "117943452927407",
    "external_url": "http://help.instagram.com/",
    "external_url_linkshimmed": "https://l.instagram.com/?u=http%3A%2F%2Fhelp.instagram.com%2F&e=AT7SpeJeYE_Bye6NBqhXGCCjNwre-k0AMvqIB3fFTBe4sxSL0IpzPueDAlO7Prsl-Ad46ICYmVQDmhO5J3E7BTNL5OSXeT-q",
    "edge_followed_by": {
      "count": 700938922
    },
    "fbid": "17841400039600391",
    "followed_by_viewer": false,
    "edge_follow": {
      "count": 235
    },
    "follows_viewer": false,
    "full_name": "Instagram",
    "...": "(46 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| id | string | Numeric Instagram user ID |
| username | string | Instagram username |
| full_name | string | Display name |
| biography | string | Bio text |
| profile_pic_url | string | Profile picture URL |
| is_private | boolean | Private account flag |
| is_verified | boolean | Verified badge flag |
| edge_followed_by.count | integer | Follower count |
| edge_follow.count | integer | Following count |
| edge_owner_to_timeline_media.count | integer | Total post count |

##### Notes

> Identical response schema to `/profile?username=...`. Use whichever identifier is available.

---

#### User Info (V2) by User ID

**`GET`** &nbsp; `/profile2`

Retrieve V2 profile data by numeric user ID. Same response structure as *User Info (V2) by Username*.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/profile2?id=25025320" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "full_name": "Instagram",
    "is_memorialized": false,
    "is_private": false,
    "has_story_archive": null,
    "username": "instagram",
    "is_regulated_c18": false,
    "regulated_news_in_locations": [],
    "text_post_app_badge_label": "instagram",
    "show_text_post_app_badge": true,
    "pk": "25025320",
    "live_broadcast_visibility": null,
    "live_broadcast_id": null,
    "profile_pic_url": "https://scontent-mxp2-1.cdninstagram.com/v/t51.82787-19/550891366_18667771684001321_1383210656577177067_n.jpg?stp=dst-jpg_e0_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-mxp2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGcN3plotwSz4snKr-W0cMckdlYJ8TC92cFUkmXGtCIb5pqZz0aFNYgefQx_I4FhXY&_nc_ohc=eh4J-8ukxegQ7kNvwFvyopg&_nc_gid=9ujE6A_tvJZ0yrRDngmDuw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af0X6vGXb4k4yhajz43urz8whS3Slc5IBwfLv19AnG3RSQ&oe=69DD8E27&_nc_sid=10d13b",
    "hd_profile_pic_url_info": {
      "url": "https://scontent-mxp2-1.cdninstagram.com/v/t51.82787-19/550891366_18667771684001321_1383210656577177067_n.jpg?efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMxIn0&_nc_ht=scontent-mxp2-1.cdninstagram.com&_nc_cat=1&_nc_oc=Q6cZ2gGcN3plotwSz4snKr-W0cMckdlYJ8TC92cFUkmXGtCIb5pqZz0aFNYgefQx_I4FhXY&_nc_ohc=eh4J-8ukxegQ7kNvwFvyopg&_nc_gid=9ujE6A_tvJZ0yrRDngmDuw&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af3OJlzoUrmb0_cB1VqEVF8sSazCqHc6TZeul2Lasxcx5Q&oe=69DD8E27&_nc_sid=10d13b"
    },
    "is_unpublished": false,
    "mutual_followers_count": null,
    "profile_context_links_with_user_ids": null,
    "...": "(32 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| pk | string | Numeric user ID |
| username | string | Instagram username |
| full_name | string | Display name |
| follower_count | integer | Follower count |
| following_count | integer | Following count |
| media_count | integer | Total media count |
| is_private | boolean | Private account flag |
| is_verified | boolean | Verified badge flag |

---

#### Web Profile Info by Username

**`GET`** &nbsp; `/web-profile`

Retrieve profile data as served by the Instagram web interface. The full profile object is nested under `data.user`.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| username | string | Required | Instagram username |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/web-profile?username=instagram" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "user": {
        "ai_agent_owner_username": "...",
        "ai_agent_type": "...",
        "biography": "...",
        "bio_links": "...",
        "fb_profile_biolink": "...",
        "biography_with_entities": "...",
        "blocked_by_viewer": "...",
        "restricted_by_viewer": "...",
        "country_block": "...",
        "eimu_id": "...",
        "external_url": "...",
        "external_url_linkshimmed": "...",
        "edge_followed_by": "...",
        "fbid": "...",
        "followed_by_viewer": "...",
        "edge_follow": "...",
        "follows_viewer": "...",
        "full_name": "...",
        "...": "(51 more fields)"
      }
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.user | object | Full profile object from the Instagram web endpoint |
| data.user.biography | string | Bio text |
| data.user.full_name | string | Display name |
| data.user.id | string | Numeric user ID string |
| data.user.username | string | Username |
| data.user.is_private | boolean | Private account flag |
| data.user.is_verified | boolean | Verified account flag |
| data.user.edge_followed_by.count | integer | Follower count |
| data.user.edge_follow.count | integer | Following count |
| data.user.edge_owner_to_timeline_media | object | Media list with `count` and `page_info` |
| status | string | API response status (`ok`) |

##### Notes

> This endpoint uses Instagram's web API path and may return slightly different fields compared to `/profile`.

---

#### Media List by User ID

**`GET`** &nbsp; `/user-feeds`

Retrieve a paginated list of posts from a user's feed (V1). Pagination uses `max_id` / `next_max_id`.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| count | integer | Required | Number of posts per page (e.g. `12`) |
| max_id | string | Optional | Pagination cursor — pass `next_max_id` from the previous response |
| allow_restricted_media | boolean | Optional | Include restricted / sensitive media |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/user-feeds?id=25025320&count=12" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "more_available": true,
    "items": [
      {
        "strong_id__": "...",
        "id": "...",
        "caption_is_edited": "...",
        "device_timestamp": "...",
        "filter_type": "...",
        "is_post_live_clips_media": "...",
        "disable_caption_and_comment": "...",
        "like_and_view_counts_disabled": "...",
        "fbid": "...",
        "deleted_reason": "...",
        "client_cache_key": "...",
        "integrity_review_decision": "...",
        "pk": "...",
        "is_affiliate_commission_eligible": "...",
        "has_delayed_metadata": "...",
        "mezql_token": "...",
        "should_request_ads": "...",
        "has_privately_liked": "...",
        "...": "(98 more fields)"
      },
      {
        "strong_id__": "...",
        "id": "...",
        "caption_is_edited": "...",
        "device_timestamp": "...",
        "filter_type": "...",
        "is_post_live_clips_media": "...",
        "disable_caption_and_comment": "...",
        "like_and_view_counts_disabled": "...",
        "fbid": "...",
        "deleted_reason": "...",
        "client_cache_key": "...",
        "integrity_review_decision": "...",
        "pk": "...",
        "is_affiliate_commission_eligible": "...",
        "has_delayed_metadata": "...",
        "mezql_token": "...",
        "should_request_ads": "...",
        "has_privately_liked": "...",
        "...": "(97 more fields)"
      },
      "... (10 more items)"
    ],
    "next_max_id": "3860100888707399162_25025320"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| more_available | boolean | Whether more pages exist |
| next_max_id | string | Cursor to pass as `max_id` for the next page |
| items | array | Array of media objects |
| items[].id | string | Compound ID in `<media_pk>_<user_pk>` format |
| items[].pk | integer | Numeric media primary key |
| items[].media_type | integer | `1`=photo  `2`=video  `8`=carousel |
| items[].taken_at | integer | Publication Unix timestamp |
| items[].caption.text | string | Caption text |
| items[].like_count | integer | Like count |
| items[].comment_count | integer | Comment count |
| items[].image_versions2 | object | Image resolution variants |
| items[].video_versions | array | Video file variants (video posts only) |

##### Notes

> **Pagination:** save `next_max_id` and pass it as `max_id` until `more_available` is `false`.

---

#### Media List (V2) by User ID

**`GET`** &nbsp; `/user-feeds2`

Retrieve a user's media feed via the Instagram V2 / GraphQL endpoint. Response is nested under `data.user.edge_owner_to_timeline_media`. Pagination uses GraphQL `end_cursor`.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| count | integer | Required | Number of posts per page |
| end_cursor | string | Optional | GraphQL cursor from `page_info.end_cursor` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/user-feeds2?id=25025320&count=12" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "user": {
        "edge_owner_to_timeline_media": "..."
      }
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.user.edge_owner_to_timeline_media.count | integer | Total posts by the user |
| data.user.edge_owner_to_timeline_media.page_info.has_next_page | boolean | Whether more pages exist |
| data.user.edge_owner_to_timeline_media.page_info.end_cursor | string | Cursor for the next page |
| data.user.edge_owner_to_timeline_media.edges | array | Media edge/node objects |
| status | string | API response status (`ok`) |

##### Notes

> Use `page_info.end_cursor` as `end_cursor` in the next request. For simpler `max_id` pagination prefer V1 `/user-feeds`.

---

#### Reels by User ID

**`GET`** &nbsp; `/reels`

Retrieve a paginated list of Reels posted by a user.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| count | integer | Required | Number of Reels per page |
| max_id | string | Optional | Pagination cursor from `paging_info.max_id` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/reels?id=25025320&count=12" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "items": [
      {
        "media": "..."
      },
      {
        "media": "..."
      },
      "... (7 more items)"
    ],
    "paging_info": {
      "max_id": "QVFEeHV3LS0xUm5PSlZOdVhMd2czTFVreXRtOE16ZzNlSFVyS1FndG1yRWMxMTVXV3hEelFZbndBMDZZcXJVMDhiNWZ4T0V5ZmdJM0JXdzA3U18tODV4UQ==",
      "more_available": true
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| items | array | Array of Reel wrapper objects |
| items[].media | object | Reel media — `id`, `pk`, `code`, `taken_at`, `video_versions`, `image_versions2` |
| items[].media.comment_count | integer | Comment count |
| items[].media.play_count | integer | View / play count |
| paging_info.max_id | string | Cursor for the next page |
| paging_info.more_available | boolean | Whether more pages exist |
| status | boolean | Request success indicator |

---

#### Reposts by User ID

**`GET`** &nbsp; `/user-reposts`

Retrieve posts that a user has reposted (shared to their own feed from another account).

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| max_id | string | Optional | Pagination cursor from `next_max_id` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/user-reposts?id=25025320" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "more_available": true,
    "items": [
      {
        "id": "...",
        "all_previous_submitters": "...",
        "carousel_media": "...",
        "carousel_media_count": "...",
        "carousel_media_pending_post_count": "...",
        "channel_tag_data": "...",
        "content_views_count": "...",
        "enable_media_notes_production": "...",
        "enable_waist": "...",
        "facepile_top_likers": "...",
        "gen_ai_detection_method": "...",
        "has_delayed_metadata": "...",
        "image_versions2": "...",
        "is_dismiss_pending_media_banner": "...",
        "main_feed_carousel_starting_media_id": "...",
        "media_cropping_info": "...",
        "media_notes": "...",
        "media_repost_count": "...",
        "...": "(151 more fields)"
      },
      {
        "id": "...",
        "all_previous_submitters": "...",
        "carousel_media": "...",
        "carousel_media_count": "...",
        "carousel_media_pending_post_count": "...",
        "channel_tag_data": "...",
        "content_views_count": "...",
        "enable_media_notes_production": "...",
        "enable_waist": "...",
        "facepile_top_likers": "...",
        "gen_ai_detection_method": "...",
        "has_delayed_metadata": "...",
        "image_versions2": "...",
        "is_dismiss_pending_media_banner": "...",
        "main_feed_carousel_starting_media_id": "...",
        "media_cropping_info": "...",
        "media_notes": "...",
        "media_repost_count": "...",
        "...": "(151 more fields)"
      },
      "... (10 more items)"
    ],
    "next_max_id": "QVFENFJJTzEzVkozRmFqRTJOSmx1NmU5R3dRT0g4Ty1NSHA5Ym9fMUVOOWp6QUdzWmdHSzhCZUJzbFlYT2xXbDdhdGkyYnN0RVpZamI5N2p6NlFLMFN2Ug=="
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| more_available | boolean | Whether more pages exist |
| next_max_id | string | Cursor for the next page |
| items | array | Array of reposted media objects |
| items[].id | string | Media ID |
| items[].image_versions2 | object | Image resolution variants |
| items[].video_versions | array | Video file variants (video reposts only) |
| items[].caption | object | Caption object with `text` |
| items[].like_count | integer | Like count |
| items[].comment_count | integer | Comment count |

---

#### Tagged Media by User ID

**`GET`** &nbsp; `/user-tags`

Retrieve posts in which a specific user has been tagged by other accounts.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| count | integer | Required | Number of posts per page |
| end_cursor | string | Optional | GraphQL pagination cursor |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/user-tags?id=25025320&count=12" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "user": {
        "edge_user_to_photos_of_you": "..."
      }
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.user.edge_user_to_photos_of_you.count | integer | Total posts where the user is tagged |
| data.user.edge_user_to_photos_of_you.page_info.has_next_page | boolean | Whether more pages exist |
| data.user.edge_user_to_photos_of_you.page_info.end_cursor | string | Cursor for the next page |
| data.user.edge_user_to_photos_of_you.edges | array | Tagged media edge/node objects |
| status | string | API response status (`ok`) |

---

#### Related Profiles by User ID

**`GET`** &nbsp; `/related-profiles`

Retrieve profiles that Instagram considers related to the given user (similar accounts / suggested follows).

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram user ID |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/related-profiles?id=25025320" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "viewer": [],
      "user": {
        "edge_related_profiles": "..."
      }
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.user.edge_related_profiles.edges | array | Related profile edge objects |
| data.viewer | array | Viewer-context related profiles (may be empty) |
| status | string | API response status (`ok`) |

##### Notes

> May return empty `edges` for large verified accounts (e.g. `@instagram`) where Instagram does not surface related profiles.

---

#### Search Users by Keyword

**`GET`** &nbsp; `/search`

Search for Instagram user accounts matching a keyword.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Required | Search keyword |
| select | string | Required | Must be `users` to scope results to user accounts |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/search?query=instagram&select=users" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": "ok",
    "users": [
      {
        "position": "...",
        "user": "..."
      },
      {
        "position": "...",
        "user": "..."
      },
      "... (51 more items)"
    ]
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | API response status (`ok`) |
| users | array | Array of user result objects |
| users[].position | integer | Ranking position in search results |
| users[].user.username | string | Username |
| users[].user.full_name | string | Display name |
| users[].user.pk | string | Numeric user ID |
| users[].user.is_verified | boolean | Verified badge flag |
| users[].user.profile_pic_url | string | Profile picture URL |

##### Notes

> `select=users` is required to scope the search. Omit it to get global results across users, hashtags, and places.

---

### 📸 Media Details

#### Media Info by URL

**`GET`** &nbsp; `/post`

Retrieve detailed metadata for an Instagram post (photo, video, or carousel) by its full URL.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| url | string | Required | Full Instagram post URL (e.g. `https://www.instagram.com/p/CqIbCzYMi5C/`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/post?url=https://www.instagram.com/p/CqIbCzYMi5C/" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "__typename": "GraphSidecar",
    "id": "3064818486287150658",
    "shortcode": "CqIbCzYMi5C",
    "thumbnail_src": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-15/655689928_18148306210474104_8408410308735836134_n.jpg?stp=dst-jpg_e35_s640x640_sh0.08_tt6&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2gE46OpcDSWHYsO8H6iKa8gLewH6nbvrRptfec2lmlvbMSUO5m4Kalj9uQ_rwuC3uB4&_nc_ohc=K0PKN57nl6oQ7kNvwECoCmC&_nc_gid=qwZ0YebxpjmD13oIBGst_A&edm=ANTKIIoBAAAA&ccb=7-5&ig_cache_key=MzA2NDgxODQ4MDI0NzMzNzc2MQ%3D%3D.3-ccb7-5&oh=00_Af14w91qPXR1E1FPERAsmON_ukwx8DGB4JCoIZEBpHR1Rg&oe=69DD8AD1&_nc_sid=d885a2",
    "dimensions": {
      "height": 1080,
      "width": 1080
    },
    "gating_info": null,
    "fact_check_overall_rating": null,
    "fact_check_information": null,
    "sensitivity_friction_info": null,
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null
    },
    "media_overlay_info": null,
    "media_preview": null,
    "display_url": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-15/655689928_18148306210474104_8408410308735836134_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08_tt6&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2gE46OpcDSWHYsO8H6iKa8gLewH6nbvrRptfec2lmlvbMSUO5m4Kalj9uQ_rwuC3uB4&_nc_ohc=K0PKN57nl6oQ7kNvwECoCmC&_nc_gid=qwZ0YebxpjmD13oIBGst_A&edm=ANTKIIoBAAAA&ccb=7-5&ig_cache_key=MzA2NDgxODQ4MDI0NzMzNzc2MQ%3D%3D.3-ccb7-5&oh=00_Af3GRM_Mb5-8ScBus7Wz9i7_cdJx9wM6s5mlAXrkQfVjtA&oe=69DD8AD1&_nc_sid=d885a2",
    "display_resources": [
      {
        "src": "...",
        "config_width": "...",
        "config_height": "..."
      },
      {
        "src": "...",
        "config_width": "...",
        "config_height": "..."
      },
      "... (1 more items)"
    ],
    "is_video": false,
    "tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiM2ViOTE2MDdjNjBhNDM0NDkyOTIyZDI3NzdlMDg2ZjUzMDY0ODE4NDg2Mjg3MTUwNjU4In0sInNpZ25hdHVyZSI6IiJ9",
    "upcoming_event": null,
    "...": "(31 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| __typename | string | `GraphImage`, `GraphVideo`, or `GraphSidecar` (carousel) |
| id | string | Numeric media ID |
| shortcode | string | Media shortcode |
| display_url | string | Full-resolution image URL |
| thumbnail_src | string | Thumbnail URL (640 px) |
| display_resources | array | Resolution variants — each has `src`, `config_width`, `config_height` |
| dimensions | object | Media dimensions with `width` and `height` |
| is_video | boolean | Video post flag |
| taken_at_timestamp | integer | Publication Unix timestamp |
| edge_media_to_caption.edges | array | Caption text nodes |
| edge_media_preview_like.count | integer | Like count |
| edge_media_to_parent_comment.count | integer | Comment count |
| owner | object | Author — `id`, `username`, `full_name`, `profile_pic_url` |
| location | object | Tagged location — `id`, `name`, `slug` |
| edge_media_to_tagged_user.edges | array | Users tagged in the media |
| edge_sidecar_to_children | object | Child items for carousel posts |
| accessibility_caption | string | Auto-generated alt text |
| is_ad | boolean | Sponsored post flag |

---

#### Media Info by ID

**`GET`** &nbsp; `/post`

Retrieve detailed metadata for an Instagram post by its numeric media ID or shortcode. Returns the same fields as *Media Info by URL*.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric media ID or media shortcode |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/post?id=3064818486287150658" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": true,
    "__typename": "GraphSidecar",
    "id": "3064818486287150658",
    "shortcode": "CqIbCzYMi5C",
    "thumbnail_src": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-15/655689928_18148306210474104_8408410308735836134_n.jpg?stp=dst-jpg_e35_s640x640_sh0.08_tt6&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2gHJScVW_IM-vcXJhNxhXxneV9JCbfWqRUMHalNxqD7CAJ88XLpd9OFt2JCLg3NRYbI&_nc_ohc=K0PKN57nl6oQ7kNvwGmGKBL&_nc_gid=4qk1CrZROa2kURt5jil3gA&edm=ANTKIIoBAAAA&ccb=7-5&ig_cache_key=MzA2NDgxODQ4MDI0NzMzNzc2MQ%3D%3D.3-ccb7-5&oh=00_Af1MlouUAUGDrFxj8unXp7YWWSHSn9W3Xkul0tApTuY6iQ&oe=69DD8AD1&_nc_sid=d885a2",
    "dimensions": {
      "height": 1080,
      "width": 1080
    },
    "gating_info": null,
    "fact_check_overall_rating": null,
    "fact_check_information": null,
    "sensitivity_friction_info": null,
    "sharing_friction_info": {
      "should_have_sharing_friction": false,
      "bloks_app_url": null
    },
    "media_overlay_info": null,
    "media_preview": null,
    "display_url": "https://instagram.fmil1-1.fna.fbcdn.net/v/t51.82787-15/655689928_18148306210474104_8408410308735836134_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08_tt6&_nc_ht=instagram.fmil1-1.fna.fbcdn.net&_nc_cat=100&_nc_oc=Q6cZ2gHJScVW_IM-vcXJhNxhXxneV9JCbfWqRUMHalNxqD7CAJ88XLpd9OFt2JCLg3NRYbI&_nc_ohc=K0PKN57nl6oQ7kNvwGmGKBL&_nc_gid=4qk1CrZROa2kURt5jil3gA&edm=ANTKIIoBAAAA&ccb=7-5&ig_cache_key=MzA2NDgxODQ4MDI0NzMzNzc2MQ%3D%3D.3-ccb7-5&oh=00_Af2GwHAu7H2wZVyuce_z3LHXUk14joKwVQckRMQeyjiFXg&oe=69DD8AD1&_nc_sid=d885a2",
    "display_resources": [
      {
        "src": "...",
        "config_width": "...",
        "config_height": "..."
      },
      {
        "src": "...",
        "config_width": "...",
        "config_height": "..."
      },
      "... (1 more items)"
    ],
    "is_video": false,
    "tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiYTJiMTliZjc5NDYwNDI1YjhjNDgyNDA2NzJhMDRjOWIzMDY0ODE4NDg2Mjg3MTUwNjU4In0sInNpZ25hdHVyZSI6IiJ9",
    "upcoming_event": null,
    "...": "(31 more fields)"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | boolean | Request success indicator |
| __typename | string | `GraphImage`, `GraphVideo`, or `GraphSidecar` |
| id | string | Numeric media ID |
| shortcode | string | Media shortcode |
| display_url | string | Full-resolution image URL |
| is_video | boolean | Video post flag |
| taken_at_timestamp | integer | Publication Unix timestamp |
| edge_media_preview_like.count | integer | Like count |
| edge_media_to_parent_comment.count | integer | Comment count |
| owner | object | Author object |

##### Notes

> Identical response schema to `/post?url=...`. Use whichever identifier is available.

---

#### Download Link by Media ID or URL

**`GET`** &nbsp; `/post-dl`

Retrieve direct CDN download links for every media file in a post — images and/or video files including all slides in a carousel. Also returns caption, like count, and comment count.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| url | string | Required | Instagram post URL **or** numeric media ID |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/post-dl?url=https://www.instagram.com/p/CqIbCzYMi5C/" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "full_name": "CreativeMobs",
      "username": "creativemobs",
      "medias": [
        "...",
        "...",
        "... (6 more items)"
      ],
      "comment_count": null,
      "like_count": 10856,
      "taken_at_timestamp": 1679574856,
      "caption": "Which one? 1,2,3,4,5,6,7 or 8?\nArtist @jyo_john_mulloor \nSelected by @illusionarybong\nPartner @worldmobs\n••••••••••••••••••••••••••••••••••••••••••••\n.\n.\nShare your best picture with us \nTag us or use #creativemobs\n••••••••••••••••••••••••••••••••••••••••••••\n.\n.\n#ai #aiart #aiartcommunity #aiartwork #aiartist #aiartists #aiartdailytheme #aiartcomm #aiartworks #aiartgenerator #aiartgallery #aiarts #aiartistcommunity #aiartistsoninstagram #aiartlovers #aiartwork_fantasy #aiartisnotart"
    },
    "status": true
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.username | string | Post author username |
| data.full_name | string | Post author display name |
| data.medias | array | One entry per slide — each has `type` (`image`/`video`) and `link` (CDN URL) |
| data.caption | string | Post caption text |
| data.like_count | integer | Like count |
| data.comment_count | integer | Comment count |
| data.taken_at_timestamp | integer | Publication Unix timestamp |
| status | string | API response status |

##### Notes

> For carousel posts `data.medias` contains one entry per slide. Video entries have `link` pointing directly to the MP4 CDN URL. **CDN links are signed and expire — download immediately.**

---

#### Music Info by Music ID

**`GET`** &nbsp; `/music`

Retrieve metadata for an Instagram audio track and a paginated list of Reels that use it.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Instagram music / audio ID |
| max_id | string | Optional | Pagination cursor for the next page of Reels |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/music?id=1234567890" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "items": [
      {
        "media": "..."
      },
      {
        "media": "..."
      },
      "... (10 more items)"
    ],
    "audio_page_reporting_id": "18324516409016492",
    "formatted_media_count": "34K reels",
    "music_canonical_id": "18324516409016492",
    "auto_created_reels_preview_metadata": [],
    "audio_page_segments": [],
    "metadata": {
      "additional_audio_info": null,
      "music_info": null,
      "original_sound_info": {
        "is_eligible_for_vinyl_sticker": "...",
        "fb_downstream_use_xpost_metadata": "...",
        "allow_creator_to_rename": "...",
        "audio_asset_id": "...",
        "audio_filter_infos": "...",
        "audio_parts": "...",
        "audio_parts_by_filter": "...",
        "can_remix_be_shared_to_fb": "...",
        "can_remix_be_shared_to_fb_expansion": "...",
        "consumption_info": "...",
        "dash_manifest": "...",
        "duration_in_ms": "...",
        "formatted_clips_media_count": "...",
        "hide_remixing": "...",
        "ig_artist": "...",
        "is_audio_automatically_attributed": "...",
        "is_eligible_for_audio_effects": "...",
        "is_explicit": "...",
        "...": "(13 more fields)"
      }
    },
    "audio_ranking_info": {
      "best_audio_cluster_id": "1190972161486813"
    },
    "is_music_page_restricted": false,
    "available_tabs": [
      "clips"
    ],
    "media_count": {
      "clips_count": 34462,
      "photos_count": 0
    },
    "paging_info": {
      "max_id": "Gtb4nt6q1NCF8VHQ2KrL_uqthWvY-fKU6oeAwWKSrN7TzJzbwmKS6tyrqMqRxWK4x9WDue28xWLc8rnzmP-AyGKu1KT7tMGNy2K8qKik2u_Iz2K-oqCzr9me0WL-trrbleW902Liz5OKgrvn3GLK5ZfK3-KT5GIm3Pf4qq5nFBg0AikIGAAaCDoGGQwA",
      "more_available": true
    }
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| items | array | Reels using this audio — each has a `media` object |
| items[].media.id | string | Reel media ID |
| items[].media.code | string | Reel shortcode |
| items[].media.taken_at | integer | Publication Unix timestamp |
| items[].media.media_type | integer | Media type code (`2` for video) |
| items[].media.comment_count | integer | Comment count |
| items[].media.video_versions | array | Video file variants |
| items[].media.image_versions2 | object | Image (cover) variants |
| audio_page_reporting_id | string | Internal audio reporting identifier |
| formatted_media_count | string | Human-readable Reels count (e.g. `"5K+"`) |
| music_canonical_id | string | Canonical audio ID |

##### Notes

> Pass `max_id` from the previous response to paginate through more Reels using the same audio.

---

### 🔖 Hashtag Lookup

#### Media by Hashtag

**`GET`** &nbsp; `/tag-feeds`

Retrieve recent and top posts for a given Instagram hashtag. Pagination uses GraphQL `end_cursor`.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Required | Hashtag name **without** the `#` symbol (e.g. `travel`) |
| end_cursor | string | Optional | GraphQL cursor from `edge_hashtag_to_media.page_info.end_cursor` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/tag-feeds?query=travel" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "data": {
      "hashtag": {
        "id": "...",
        "name": "...",
        "allow_following": "...",
        "is_following": "...",
        "is_top_media_only": "...",
        "profile_pic_url": "...",
        "edge_hashtag_to_media": "...",
        "edge_hashtag_to_top_posts": "...",
        "edge_hashtag_to_content_advisory": "...",
        "edge_hashtag_to_null_state": "..."
      }
    },
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| data.hashtag.id | string | Numeric hashtag ID |
| data.hashtag.name | string | Hashtag name |
| data.hashtag.profile_pic_url | string | Hashtag cover image URL |
| data.hashtag.edge_hashtag_to_media.count | integer | Total post count |
| data.hashtag.edge_hashtag_to_media.page_info.has_next_page | boolean | Whether more pages exist |
| data.hashtag.edge_hashtag_to_media.page_info.end_cursor | string | Cursor for the next page |
| data.hashtag.edge_hashtag_to_media.edges | array | Recent posts |
| data.hashtag.edge_hashtag_to_top_posts.edges | array | Top / featured posts |
| status | string | API response status (`ok`) |

---

#### Search Hashtags by Keyword

**`GET`** &nbsp; `/search`

Search for Instagram hashtags matching a keyword.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Required | Search keyword |
| select | string | Required | Must be `hashtags` to scope results |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/search?query=travel&select=hashtags" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": "ok",
    "hashtags": [
      {
        "position": "...",
        "hashtag": "..."
      },
      {
        "position": "...",
        "hashtag": "..."
      },
      "... (52 more items)"
    ]
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | API response status (`ok`) |
| hashtags | array | Hashtag result objects |
| hashtags[].position | integer | Ranking position |
| hashtags[].hashtag.name | string | Hashtag name without `#` |
| hashtags[].hashtag.id | integer | Numeric hashtag ID |
| hashtags[].hashtag.media_count | integer | Total post count for this hashtag |

---

### 🗺️ Location Data

#### Search Locations by Keyword

**`GET`** &nbsp; `/search`

Search for Instagram locations (places) matching a keyword.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Required | Search keyword |
| select | string | Required | Must be `places` to scope results |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/search?query=new+york&select=places" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": "ok",
    "places": [
      {
        "position": "...",
        "place": "..."
      },
      {
        "position": "...",
        "place": "..."
      },
      "... (53 more items)"
    ]
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | API response status (`ok`) |
| places | array | Location result objects |
| places[].position | integer | Ranking position |
| places[].place.title | string | Location display name |
| places[].place.subtitle | string | Address snippet / subtitle |
| places[].place.location.pk | string | Numeric location ID |
| places[].place.location.name | string | Location name |
| places[].place.location.facebook_places_id | string | Associated Facebook Places ID |

---

#### Location Info by Location ID

**`GET`** &nbsp; `/location-info`

Retrieve detailed metadata for a specific Instagram location: coordinates, category, media count, address, and business hours.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram location ID |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/location-info?id=219045149" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "location_info": {
      "name": "Dubai UAE",
      "phone": "",
      "category": "Travel & Transportation",
      "media_count": 12594,
      "price_range": 0,
      "lat": 25.088510700166,
      "lng": 55.147547878986,
      "slug": "dubai-uae",
      "location_id": "219045149",
      "location_address": "",
      "location_city": "",
      "location_zip": "",
      "ig_business": {
        "profile": "..."
      },
      "hours": {
        "status": "..."
      }
    }
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| location_info.location_id | string | Numeric location ID |
| location_info.name | string | Location name |
| location_info.slug | string | URL-friendly slug |
| location_info.category | string | Category (e.g. `"Travel & Transportation"`) |
| location_info.lat | float | Latitude |
| location_info.lng | float | Longitude |
| location_info.media_count | integer | Posts tagged at this location |
| location_info.phone | string | Phone number (if public) |
| location_info.location_address | string | Street address |
| location_info.location_city | string | City |
| location_info.location_zip | string | ZIP / postal code |
| location_info.price_range | integer | Price range indicator (`0` = not set) |
| location_info.hours | object | Business hours with `status` field |
| location_info.ig_business.profile | object | Linked Instagram business profile (if any) |

---

#### Media by Location ID

**`GET`** &nbsp; `/location-feeds`

Retrieve paginated media posts tagged at a specific Instagram location. Choose between recent or top-ranked posts via the `tab` parameter.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Numeric Instagram location ID |
| tab | string | Required | `recent` — chronological order  |  `ranked` — most popular |
| end_cursor | string | Optional | GraphQL cursor from `page_info.end_cursor` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/location-feeds?id=219045149&tab=recent" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "edges": [
      {
        "node": "...",
        "cursor": "..."
      },
      {
        "node": "...",
        "cursor": "..."
      },
      "... (10 more items)"
    ],
    "page_info": {
      "end_cursor": "a7b13800275848929a96cf3549813b25",
      "has_next_page": true
    }
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| edges | array | Media edge/node objects |
| edges[].node.pk | string | Numeric media primary key |
| edges[].node.id | string | Media ID in `<pk>_<owner_pk>` format |
| edges[].node.code | string | Shortcode |
| edges[].node.taken_at | integer | Publication Unix timestamp |
| edges[].node.caption | object | Caption with `text` and `created_at` |
| edges[].node.video_versions | array | Video variants (video posts only) |
| edges[].node.image_versions2 | object | Image resolution variants |
| page_info.has_next_page | boolean | Whether more pages exist |
| page_info.end_cursor | string | Cursor for the next page |

---

#### Cities by Country Code

**`GET`** &nbsp; `/cities`

Retrieve a paginated list of cities in a country that have associated Instagram location data. City IDs are needed for the `/locations` endpoint.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| country_code | string | Required | ISO 3166-1 alpha-2 country code (e.g. `US`, `GB`, `DE`) |
| page | integer | Optional | Page number — default `1` |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/cities?country_code=US" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "country_info": {
      "id": "US",
      "name": "United States",
      "slug": "united-states"
    },
    "city_list": [
      {
        "id": "...",
        "name": "...",
        "slug": "..."
      },
      {
        "id": "...",
        "name": "...",
        "slug": "..."
      },
      "... (94 more items)"
    ],
    "next_page": 2,
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| country_info.id | string | Country code |
| country_info.name | string | Country name |
| country_info.slug | string | URL-friendly country slug |
| city_list | array | City objects |
| city_list[].id | string | City ID — use with `/locations` |
| city_list[].name | string | City name |
| city_list[].slug | string | URL-friendly city slug |
| next_page | integer | Next page number, or `null` if last page |
| status | string | API response status (`ok`) |

##### Notes

> **Location drill-down order:** `/cities` → `/locations` → `/location-info` + `/location-feeds`

---

#### Locations by City ID

**`GET`** &nbsp; `/locations`

Retrieve a paginated list of specific Instagram locations (venues, landmarks) within a city.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| city_id | string | Required | City ID from the `/cities` endpoint |
| page | integer | Optional | Page number for pagination |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/locations?city_id=c2728325" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "country_info": {
      "id": "US",
      "name": "United States",
      "slug": "united-states"
    },
    "city_info": {
      "id": "c2728325",
      "name": "MidtownEast",
      "slug": "midtowneast-united-states"
    },
    "location_list": [
      {
        "id": "...",
        "name": "...",
        "slug": "..."
      },
      {
        "id": "...",
        "name": "...",
        "slug": "..."
      },
      "... (94 more items)"
    ],
    "next_page": 2,
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| country_info | object | Country info — `id`, `name`, `slug` |
| city_info | object | City info — `id`, `name`, `slug` |
| location_list | array | Location objects |
| location_list[].id | string | Location ID — use with `/location-info` and `/location-feeds` |
| location_list[].name | string | Location name |
| location_list[].slug | string | URL-friendly slug |
| next_page | integer | Next page number, or `null` if last page |
| status | string | API response status (`ok`) |

---

### 🔍 Explore Feed

#### Explore Sections List

**`GET`** &nbsp; `/sections`

Retrieve all available Explore topic sections (e.g. "TV & Movies", "Games"). Use the `section_id` values returned here to call `/section`.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/sections" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "sections": [
      {
        "section_id": "...",
        "name": "...",
        "subsections": "..."
      },
      {
        "section_id": "...",
        "name": "...",
        "subsections": "..."
      },
      "... (12 more items)"
    ],
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| sections | array | Section objects |
| sections[].section_id | string | Section ID — use with `/section` |
| sections[].name | string | Section name (e.g. `"TV & Movies"`) |
| sections[].subsections | array | Nested subsections — each has `section_id`, `name`, preview `medias` |
| status | string | API response status (`ok`) |

##### Notes

> Call this endpoint first to discover valid `section_id` values before using `/section`.

---

#### Media by Explore Section ID

**`GET`** &nbsp; `/section`

Retrieve paginated media content from a specific Instagram Explore topic section.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| id | string | Required | Section ID from the `/sections` endpoint |
| count | integer | Required | Number of posts per page |
| max_id | string | Optional | Pagination cursor from the previous response `max_id` field |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/section?id=10155994923880727&count=12" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "section_name": "Games",
    "max_id": "3022944298396964424",
    "more_available": true,
    "items": [
      {
        "strong_id__": "...",
        "id": "...",
        "fbid": "...",
        "deleted_reason": "...",
        "client_cache_key": "...",
        "integrity_review_decision": "...",
        "pk": "...",
        "has_delayed_metadata": "...",
        "mezql_token": "...",
        "should_request_ads": "...",
        "has_privately_liked": "...",
        "collaborator_edit_eligibility": "...",
        "share_count_disabled": "...",
        "is_reshare_of_text_post_app_media_in_ig": "...",
        "is_visual_reply_commenter_notice_enabled": "...",
        "subtype_name_for_REST__": "...",
        "has_views_fetching_on_search_grid": "...",
        "image_versions2": "...",
        "...": "(75 more fields)"
      },
      {
        "strong_id__": "...",
        "id": "...",
        "fbid": "...",
        "deleted_reason": "...",
        "client_cache_key": "...",
        "integrity_review_decision": "...",
        "pk": "...",
        "has_delayed_metadata": "...",
        "mezql_token": "...",
        "should_request_ads": "...",
        "has_privately_liked": "...",
        "collaborator_edit_eligibility": "...",
        "share_count_disabled": "...",
        "is_reshare_of_text_post_app_media_in_ig": "...",
        "is_visual_reply_commenter_notice_enabled": "...",
        "subtype_name_for_REST__": "...",
        "has_views_fetching_on_search_grid": "...",
        "image_versions2": "...",
        "...": "(79 more fields)"
      },
      "... (18 more items)"
    ],
    "subsections": [
      {
        "section_id": "...",
        "name": "..."
      },
      {
        "section_id": "...",
        "name": "..."
      },
      "... (17 more items)"
    ],
    "status": "ok"
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| section_name | string | Name of the section (e.g. `"Games"`) |
| max_id | string | Cursor for the next page |
| more_available | boolean | Whether more pages exist |
| items | array | Media items in this section |
| items[].id | string | Media ID |
| items[].pk | integer | Media primary key |
| items[].media_type | integer | `1`=photo  `2`=video  `8`=carousel |
| subsections | array | Sub-section data (if applicable) |

##### Notes

> Pass `max_id` from the response as `max_id` in the next request to paginate.

---

### 🌐 Global Search

#### Global Search by Keyword

**`GET`** &nbsp; `/search`

Perform a combined search across users, hashtags, and locations simultaneously. Returns ranked results in all three categories in a single request.

##### Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| query | string | Required | Search keyword (e.g. `coffee`) |
| fields | string | Optional | Comma-separated list of fields to return. |


##### Example Request

```bash
curl -X GET "https://instagram-looter2.p.rapidapi.com/search?query=coffee" \
  -H "x-rapidapi-key: YOUR_API_KEY" \
  -H "x-rapidapi-host: instagram-looter2.p.rapidapi.com"
```

##### Example Response

```json
{
  "status": 200,
  "body": {
    "status": "ok",
    "hashtags": [
      {
        "position": "...",
        "hashtag": "..."
      },
      {
        "position": "...",
        "hashtag": "..."
      },
      "... (10 more items)"
    ],
    "places": [
      {
        "position": "...",
        "place": "..."
      }
    ],
    "users": [
      {
        "position": "...",
        "user": "..."
      },
      {
        "position": "...",
        "user": "..."
      },
      "... (41 more items)"
    ]
  }
}
```

##### Response Fields

| Field | Type | Description |
| --- | --- | --- |
| status | string | API response status (`ok`) |
| users | array | Matched user accounts — each has `position` and `user` object |
| hashtags | array | Matched hashtags — each has `position` and `hashtag` object |
| places | array | Matched locations — each has `position` and `place` object |

##### Notes

> Omit the `select` parameter to trigger global search. Add `select=users`, `select=hashtags`, or `select=places` to narrow to a single category.

---

## Usage Examples

### Python

```python
import requests

BASE_URL = "https://instagram-looter2.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-key":  "YOUR_API_KEY",
    "x-rapidapi-host": "instagram-looter2.p.rapidapi.com",
}

# ── 1. Resolve a username to a numeric user ID ─────────────────────────────
def get_user_id(username: str) -> str:
    r = requests.get(f"{BASE_URL}/id", params={"username": username}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["user_id"]

# ── 2. Get V2 profile info by username ────────────────────────────────────
def get_profile(username: str) -> dict:
    r = requests.get(f"{BASE_URL}/profile2", params={"username": username}, headers=HEADERS)
    r.raise_for_status()
    return r.json()

# ── 3. Paginate all posts for a user ──────────────────────────────────────
def get_all_posts(user_id: str, posts_per_page: int = 12):
    posts, max_id = [], None
    while True:
        params = {"id": user_id, "count": posts_per_page}
        if max_id:
            params["max_id"] = max_id
        r = requests.get(f"{BASE_URL}/user-feeds", params=params, headers=HEADERS)
        data = r.json()
        posts.extend(data.get("items", []))
        if not data.get("more_available"):
            break
        max_id = data.get("next_max_id")
    return posts

# ── 4. Get download links for a post ──────────────────────────────────────
def get_download_links(post_url: str) -> list:
    r = requests.get(f"{BASE_URL}/post-dl", params={"url": post_url}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["data"]["medias"]   # [{"type": "image"|"video", "link": "..."}]

# ── 5. Search for users ───────────────────────────────────────────────────
def search_users(keyword: str) -> list:
    r = requests.get(f"{BASE_URL}/search",
                     params={"query": keyword, "select": "users"}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["users"]

# ── 6. Get posts by hashtag ───────────────────────────────────────────────
def get_hashtag_posts(hashtag: str):
    r = requests.get(f"{BASE_URL}/tag-feeds", params={"query": hashtag}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["data"]["hashtag"]["edge_hashtag_to_media"]["edges"]

# ── 7. Location drill-down ────────────────────────────────────────────────
def get_cities(country_code: str) -> list:
    r = requests.get(f"{BASE_URL}/cities",
                     params={"country_code": country_code}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["city_list"]

def get_locations_in_city(city_id: str) -> list:
    r = requests.get(f"{BASE_URL}/locations", params={"city_id": city_id}, headers=HEADERS)
    r.raise_for_status()
    return r.json()["location_list"]

# ── Example usage ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    uid    = get_user_id("instagram")
    print("User ID:", uid)

    profile = get_profile("instagram")
    print("Followers:", profile["follower_count"])

    posts = get_all_posts(uid, posts_per_page=12)
    print("Total posts fetched:", len(posts))

```

### JavaScript (Node.js / Fetch)

```javascript
const BASE_URL  = "https://instagram-looter2.p.rapidapi.com";
const HEADERS   = {
  "x-rapidapi-key":  "YOUR_API_KEY",
  "x-rapidapi-host": "instagram-looter2.p.rapidapi.com",
};

// ── Helper ─────────────────────────────────────────────────────────────────
async function apiGet(path, params = {}) {
  const url = new URL(BASE_URL + path);
  Object.entries(params).forEach(([k, v]) => url.searchParams.set(k, v));
  const res = await fetch(url.toString(), { headers: HEADERS });
  if (!res.ok) throw new Error(`HTTP ${res.status}: ${res.statusText}`);
  return res.json();
}

// ── 1. Resolve username → user ID ─────────────────────────────────────────
async function getUserId(username) {
  const data = await apiGet("/id", { username });
  return data.user_id;   // Treat as string to avoid JS precision loss!
}

// ── 2. V2 profile ─────────────────────────────────────────────────────────
async function getProfile(username) {
  return apiGet("/profile2", { username });
}

// ── 3. All posts for a user (paginated) ───────────────────────────────────
async function getAllPosts(userId, count = 12) {
  let posts = [], maxId = null;
  do {
    const params = { id: userId, count };
    if (maxId) params.max_id = maxId;
    const data = await apiGet("/user-feeds", params);
    posts = posts.concat(data.items ?? []);
    maxId = data.more_available ? data.next_max_id : null;
  } while (maxId);
  return posts;
}

// ── 4. Download links ─────────────────────────────────────────────────────
async function getDownloadLinks(postUrl) {
  const data = await apiGet("/post-dl", { url: postUrl });
  return data.data.medias;  // [{ type, link }]
}

// ── Example usage ─────────────────────────────────────────────────────────
(async () => {
  const uid     = await getUserId("instagram");
  console.log("User ID:", uid);

  const profile = await getProfile("instagram");
  console.log("Followers:", profile.follower_count);

  const posts   = await getAllPosts(uid);
  console.log("Posts fetched:", posts.length);
})();

```

## Important Remarks

### 1. CDN URLs are signed and expire

All image, video, and profile picture URLs returned by the API are signed CDN URLs. They **expire within a short time window** (typically minutes to hours). Do not persist them to a database — download the media immediately or store only the media ID / shortcode and re-fetch the CDN URL when needed.

### 2. Private accounts return limited data

For private Instagram accounts, feed endpoints (`/user-feeds`, `/user-feeds2`, `/reels`, `/user-tags`, `/user-reposts`) will return empty arrays or very limited data. Profile metadata (username, bio, counts) is still accessible.

### 3. Three different pagination systems

The API uses three distinct pagination mechanisms depending on the endpoint:

- **`max_id` / `next_max_id`** — V1 feeds: `/user-feeds`, `/reels`, `/user-reposts`, `/section`
- **`end_cursor` / `page_info.end_cursor`** — GraphQL: `/user-feeds2`, `/user-tags`, `/tag-feeds`, `/location-feeds`
- **`page` / `next_page`** — Location hierarchy: `/cities`, `/locations`

Check the correct cursor field name before building your pagination loop.

### 4. `/search` is a multi-purpose endpoint

The `/search` path serves four different use cases controlled by the optional `select` parameter:

- `select=users` — users only
- `select=hashtags` — hashtags only
- `select=places` — locations only
- *(no `select`)* — global combined results (users + hashtags + places)


### 5. The `fields` parameter works on all endpoints

Every endpoint supports `fields` for response filtering using dot notation, array notation (`bio_links[].url`), and wildcards (`*.count`). Use it to reduce payload size and latency, especially when paginating large feeds.