import time, vk

session = vk.Session(access_token='040be1e2040be1e2040be1e235046cee8d0040b040be1e25fe4ce9a170dd5813a8c6acc')
api = vk.API(session, v='5.87',  lang='ru', timeout=10)
owners_id = input("Enter group/user id: ")
post_id = input("Enter post id: ")

while (True):
    likes = api.likes.getList(type='post', owner_id=owners_id, item_id=post_id)['count']
    comments = api.wall.getComments(owner_id=owners_id, need_likes=0, count=1, post_id=post_id)['count']
    reposts = api.likes.getList(type='post', owner_id=owners_id, filter='copies', item_id=post_id)['count']
    print('Number of likes:', likes, ', comments:', comments, ', reposts:', reposts)
    time.sleep(1)