# ==> Intially Setup proxies in your system so that Website doesn't blocks you. #
# ==> Edit the Username in the given code #
# ==> Run it to fetch user details #
# ==> This is a OSINT tool that can be used by Cybercells to get more info about the accused. #
# ==> Use this tool for ethical purposes only . We Do Not promote any illegal activity. #



				"THIS TOOL IS CREATED BY MANSHA NEGI,SHUBHAM SHARMA AND GURU PRASAD PATTANAIK"





import instaloader

# Define the username you want to scrape
username = "guru.p05"

# Create an instance of the Instaloader class
L = instaloader.Instaloader()

# Fetch the user details
profile = instaloader.Profile.from_username(L.context, username)

# Scrape the profile data
profile_data = {
    "username": profile.username,
    "full_name": profile.full_name,
    "biography": profile.biography,
    "followers": profile.followers,
    "followees": profile.followees,
    "posts": profile.mediacount,
    "profile_pic_url": profile.profile_pic_url,
    "is_private": profile.is_private,
    "is_verified": profile.is_verified
}

# Print the profile data
print("The Juicy Info is below ")
print(profile_data)