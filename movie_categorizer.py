movie_ratings = {
    "Inception": 8.8,
    "The Avengers": 8.0,
    "The Room": 3.7,
    "Interstellar": 8.6,
    "Cats": 2.8,
    "Shrek": 7.9
}

worth_watching = {}
for movie in movie_ratings:
    rating = movie_ratings[movie]
    if rating >= 8.5:
        worth_watching[movie] = "Masterpiece"
    elif 7.0 <= rating <= 8.4:
        worth_watching[movie] = "Good Movie"
    else:
        worth_watching[movie] = "Skip It"
print(worth_watching)

