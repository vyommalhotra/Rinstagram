Instructions:

--------------------------------------------------------------------------------------
mysql database:
-> go to 'v9malhot_s6bhatna/mysql' folder
-> Create a new database (ideally with the name ‘social_media’)
-> run ‘createTable.sql’ in the 'mysql' folder using the newly created databases
-> run ‘importData.sql’ (populates the tables using the provided csv files in 'mysql' folder)

python:
-> go to ‘python’ folder
-> edit ‘config.py’ and specify the host, port, database name, user, and password of the mysql database created in the previous step. 
Note: you might want to create a new user in your mysql and provide it all privileges if you don’t want to use your root user.

-> open a terminal/command prompt in the ‘python’ folder
-> run the command to install pip packages dependencies: pip install -r req.txt
-> run the following command to start using the application: python cli.py

--------------------------------------------------------------------------------------
Demo:
Please refer to demo.mp4 in the 'video' folder. The demo videos goes through the following functionalities of the application:

1. Sign up
2. Login (includes validation)
3. Create a post
4. View posts from topics you are following
5. View posts from users you are following
6. Create a new topic
7. Follow a new topic
8. View comments on a post
9. View likes on a post
10. Add a comment on a post
11. Add a like on a post
