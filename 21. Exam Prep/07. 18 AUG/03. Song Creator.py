def add_songs(*songs):
    db = {}
    for song in songs:
        name = song[0]
        lyrics = song[1]
        if name in db:
            db[name] = db[name] + lyrics
        else:
            db[name] = lyrics

    result = ""
    for song_lyrics in db.items():
        result += f"- {song_lyrics[0]}\n"
        for line in song_lyrics[1]:
            result += f"{line}\n"

    return result

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))