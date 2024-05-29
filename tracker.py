from datetime import datetime
import time
from twitchAPI.helper import first
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticationStorageHelper
from twitchAPI.type import AuthScope
import asyncio

### ⬇️ ENTER YOUR INFO HERE ⬇️ ###
client_id = 'YOUR CLIENT ID'
client_secret = 'YOUR CLIENT SECRET'


TARGET_SCOPES = [AuthScope.MODERATOR_READ_FOLLOWERS]


async def run():
	# create the api instance and get user auth either from storage or website
	twitch = await Twitch(client_id, client_secret)
	helper = UserAuthenticationStorageHelper(twitch, TARGET_SCOPES)
	await helper.bind()

	# get the currently logged in user
	user = await first(twitch.get_users())

	# make a loop, that can be quit with ctrl+c
	try:
		while True:
			# get the followers
			followers = await twitch.get_channel_followers(user.id)
			with open("count.txt", "w") as follower_file:
				# save to file
				follower_file.write(str(followers.total))

			# logging
			curr_time = datetime.now().strftime("%H:%M:%S")
			print(f"[{curr_time}]: Follow count updated to {followers.total}")
			# and do it all again in 30 seconds
			time.sleep(30)
	except KeyboardInterrupt:
		pass
	finally:
		# stopping both eventsub as well as gracefully closing the connection to the API
		await twitch.close()


asyncio.run(run())
