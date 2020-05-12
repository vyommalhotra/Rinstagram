import pandas as pd
import numpy as np
from random import choice
from string import ascii_uppercase

post = pd.read_csv('reduced_member.csv')

post = post.drop_duplicates(subset='id', keep='last')

post.drop(['gid', 'name'], axis=1, inplace = True)

post['friendID'] = 0

post.reset_index(inplace=True)

friends = pd.DataFrame(0, index = np.arange(len(post)*11), columns = ['id', 'friendId'])
print(len(friends))

index = 0

for i, row in post.iterrows():
   if i > 8325:
       break

   for x in range(i + 1, i + 12):
       friends.at[index, 'id'] = post.at[i, 'id']
       index = index + 1
       friends.at[index, 'friendId'] = post.at[x, 'id']

friends.drop_duplicates(subset = ['id', 'friendId'],keep='last')

friends.to_csv('friend.csv', index=False)