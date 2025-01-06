import pandas as pd
import random
import uuid

# Updated hashtags list based on new topics
updated_hashtags = {
    "podcasts": ["#podcast", "#podcastlife", "#podcastersofinstagram", "#podcasts", "#spotify", "#newpodcast", "#applepodcast", "#listentothis"],
    "technology": ["#tech", "#technology", "#innovation", "#gadgets", "#AI", "#machinelearning", "#technews", "#futuretech", "#startup"],
    "memes": ["#memes", "#funny", "#meme", "#humor", "#viral", "#dankmemes", "#lol", "#funnymemes", "#memeoftheday", "#comedy"],
    "dance": ["#dance", "#dancer", "#choreography", "#hiphop", "#dancechallenge", "#dancevideo", "#dancecommunity", "#dancefloor", "#instadance"],
    "sports": ["#sports", "#football", "#cricket", "#basketball", "#sportsnews", "#soccer", "#sportslife", "#athlete", "#fitness", "#worldcup"],
    "fashion": ["#fashion", "#style", "#ootd", "#fashionblogger", "#fashionista", "#streetstyle", "#fashionphotography", "#fashionaddict", "#instafashion"]
}

# Updated post types for each topic
topics_post_types = {
    "podcasts": ["static_image", "carousel", "video", "reel"],
    "technology": ["static_image", "video", "carousel", "reel"],
    "memes": ["static_image", "carousel", "reel"],
    "dance": ["video", "reel"],
    "sports": ["video", "carousel", "reel"],
    "fashion": ["static_image", "carousel", "reel", "video"]
}

# Function to determine engagement based on post type and audio type
def generate_engagement(post_type, audio_type):
    # Define engagement ranges for likes, comments, shares, and saves
    if post_type in ["reel", "video"]:
        base_likes = random.randint(1000, 10000)
        base_comments = random.randint(500, 5000)
        base_shares = random.randint(200, 3000)
        base_saves = random.randint(100, 2000)
    else:
        if post_type == "carousel":
            multiplier = 1.2
        else:
            multiplier = 1.0

        base_likes = int(random.randint(500, 5000) * multiplier)
        base_comments = int(random.randint(100, 1500) * multiplier)
        base_shares = int(random.randint(50, 1000) * multiplier)
        base_saves = int(random.randint(10, 500) * multiplier)

    # Apply audio type multiplier
    if audio_type == "trending_audio":
        audio_multiplier = 1.3
    else:
        audio_multiplier = 0.9

    likes = int(base_likes * audio_multiplier)
    comments = int(base_comments * audio_multiplier)
    shares = int(base_shares * audio_multiplier)
    saves = int(base_saves * audio_multiplier)

    return likes, comments, shares, saves

# Generate dataset
data_with_audio = []

for _ in range(20):  # Generate 100 entries
    topic = random.choice(list(topics_post_types.keys()))
    post_type = random.choice(topics_post_types[topic])
    audio_type = random.choice(["trending_audio", "original_audio"])
    post_id = str(uuid.uuid4())
    hashtags_used = random.sample(updated_hashtags[topic], random.randint(2, 5))
    likes, comments, shares, saves = generate_engagement(post_type, audio_type)
    reach = random.randint(max(likes, 1000), max(likes * 10, 10000))  # Reach scales with engagement
    engagement_rate = (likes + comments + shares + saves) / reach

    data_with_audio.append({
        "post_id": post_id,
        "post_type": post_type,
        "topic": topic,
        "hashtags_used": ",".join(hashtags_used),
        "audio_type": audio_type,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "saves": saves,
        "reach": reach,
        "engagement_rate": round(engagement_rate, 4)  # Rounded for clarity
    })

# Create DataFrame
df_with_audio = pd.DataFrame(data_with_audio)

# Save to CSV
df_with_audio.to_csv("social_media_engagement_with_audio_and_carousel.csv", index=False)

print("Dataset created and saved to 'social_media_engagement_with_audio_and_carousel.csv'")