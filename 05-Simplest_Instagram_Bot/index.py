from instabot import Bot

bot = Bot()

# to login the instagram
bot.login(username='ha_ider0101', password='PagalgadhA')

# to follow anyone
# bot.follow('magnetbrains')

# to upload photo
# bot.upload_photo('Enter path of the photo', caption='Enter caption of the photo')

# to do unfollow anyone
# bot.unfollow('magnetbrains')

# to send message to the followers
# bot.send_message('this is instagram bot using python', ["Abdullah Mirza", "Mohammad mujammil"])

# to get information about followers
# followers = bot.get_user_followers('ha_ider0101')
# for follower in followers:
#     print('\n\n\n',bot.get_user_info(follower), '\n\n\n')

# to get information about following
following = bot.get_user_following('ha_ider0101')
for follow in following:
    print('\n\n\n',bot.get_user_info(follow), '\n\n\n')