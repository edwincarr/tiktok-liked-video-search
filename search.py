from TikTokApi import TikTokApi
api = TikTokApi()

username = input('Enter your username: ')
print('Searching in @' + username + '\'s liked videos...')

user = api.user(username=username)
liked_vids = user.liked(username=username, count=3000)

search_query = input('Search: ').lower()

for tik in liked_vids:
	tiktok = tik.info()
	search_values = [tiktok['desc'], tiktok['author']['uniqueId'], tiktok['author']['nickname'], tiktok['music']['title'], tiktok['music']['authorName']]
	search_values1 = [str.lower() for str in search_values]

	for search_val in search_values1:
		if search_query in search_val:
			URL = 'https://www.tiktok.com/@' + tiktok['author']['uniqueId'] + '/video/' + tiktok['id']
			print(URL)
			break
		else:
			print('.')
			break
# End
