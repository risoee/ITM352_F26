celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 39, 36, 62, 51)

celeb_list = []
for celeb in celebs: 
    celeb_list.append(celeb)

age_list = [age for age in ages]

celebs_dict = {"celebs": celeb_list, "ages": age_list}
print(celebs_dict)