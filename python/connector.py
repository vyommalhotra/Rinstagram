import mysql.connector
from objects import Post
from objects import Comment
from objects import Group
from objects import Like
from datetime import datetime
import config as cfg

HOST = cfg.db['host']
PORT = cfg.db['port']
DATABASE = cfg.db['database']
USER = cfg.db['user']
PASSWORD = cfg.db['password']

class Sql:
        
    def connected(self):
        return self.cnx.is_connected()

    #1
    def get_user_password(self, username):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select pw from login "
                "where username = %s ")

        cursor.execute(query, (username, ))

        password = ""

        for (row) in cursor:
            password = row[0]

        cursor.close()
        self.disconnect()

        return password
    
    #2
    def show_friends_posts(self, userid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select post.pid, person.username, groupname.groupname, msg, post.postTimeStamp, post.likes, post.gid from post "
                    "left join friend on post.id = friend.friendID "
                    "left join groupname on post.gid = groupname.gid "
                    "left join person on post.id = person.id "
                    "where friend.id = %s and person.username IS NOT NULL;")

        cursor.execute(query, (userid, ))

        posts = []

        for (row) in cursor:
            post = Post(pid = row[0], username=row[1], groupname = row[2], msg = row[3], timestamp = row[4], likes = row[5], gid=row[6]) 
            posts.append(post)
        
        cursor.close()
        self.disconnect()

        return posts
    
    #3
    def show_groups_posts(self, userid):

        self.connect()
        cursor = self.cnx.cursor()

        query = ("select post.pid, person.username, groupname.groupname, msg, post.postTimeStamp, post.likes, post.gid from post "
                "left join persongroup on post.gid = persongroup.gid "
                "left join person on post.id = person.id "
                "left join groupname on post.gid = groupname.gid "
                "where persongroup.id = %s and person.username IS NOT NULL;")

        cursor.execute(query, (userid, ))

        posts = []

        for (row) in cursor:
            post = Post(pid = row[0], username=row[1], groupname = row[2], msg = row[3], timestamp = row[4], likes = row[5], gid=row[6]) 
            posts.append(post)
        
        cursor.close()
        self.disconnect()

        return posts        
    
    #4
    def show_following(self, userid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select person.username "
                "from friend left join person on friend.friendID = person.ID "
                "where friend.ID = %s;")

        cursor.execute(query, (userid, ))

        followings = []

        for (row) in cursor:
            followings.append(row[0])

        cursor.close()
        self.disconnect()

        return followings

    #5
    def show_comments(self, pid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select person.username, postcomment.msg, postcomment.commentTimeStamp from postcomment "
                "join person on postcomment.id = person.id "
                "where pid = %s")

        cursor.execute(query, (pid, ))

        comments = []

        for (row) in cursor:
            comment = Comment(username=row[0], msg=row[1], timestamp=row[2])
            comments.append(comment)

        cursor.close()
        self.disconnect()

        return comments
    
    #6
    def get_highest_pid(self):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select pid from post order by pid desc limit 1;")

        cursor.execute(query)

        pid = ""

        for (row) in cursor:
            pid = row[0]

        cursor.close()
        self.disconnect()

        return pid

    def add_post(self, userid, gid, msg):
        new_pid = str(int(self.get_highest_pid()) + 1)

        self.connect()
        cursor = self.cnx.cursor()

        query = ("insert into post "
        "(gid, pid, id, postTimeStamp, msg, likes) "
        "values (%s, %s , %s, %s, %s, %s);")

        cursor.execute(query, (gid, new_pid, userid, datetime.now(), msg, 0))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return new_pid

    #7
    def add_comment(self, userid, gid, pid, msg):
        self.connect()
        cursor = self.cnx.cursor()   

        query = ("insert into postcomment "
        "(gid, pid, commentTimeStamp, id, msg) "
        "values (%s, %s, %s, %s, %s);")

        cursor.execute(query, (gid, pid, datetime.now(), userid, msg))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return pid

    #8
    def follow(self, current_user, user_to_follow):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("INSERT INTO Friend "
                "VALUES (%s, %s);")
        
        cursor.execute(query, (current_user, user_to_follow))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return user_to_follow
    
    #9
    def user_exists(self, username):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("SELECT username from login "
                "WHERE username = %s")
        
        cursor.execute(query, (username,))

        for (row) in cursor:
            important_do_nothing = 1

        if(cursor.rowcount < 1):
            cursor.close()
            self.disconnect()
            return False

        else:
            cursor.close()
            self.disconnect()
            return True

    #9
    def create_user(self, username, password):
        if self.user_exists(username):
            return False

        self.connect()
        cursor = self.cnx.cursor()

        query1 = ("insert into login "
                "values (%s, %s);")

        query2 = ("insert into person "
                "values (%s, NULL , %s);")
        
        query3 = ("insert into persongroup "
                "values (%s, %s);")

        cursor.execute(query1, (username, password))
        cursor.execute(query2, (1, username))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        #new users join group 1
        userid = self.get_userid(username)
        self.join_group(userid, 1)

        return True

    #10
    def create_like(self, gid, userid, pid, response="LIKE"):
        self.connect()
        cursor = self.cnx.cursor()

        query1 = ("update post "
                "set likes = likes + 1 "
                "where pid = %s;")
        
        query2 = ("insert into postlike "
                "values (%s, %s, %s, %s);")
        
        cursor.execute(query1, (pid, ))
        cursor.execute(query2, (gid, pid, response, userid))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return pid
    
    #11
    def stop_following(self, userid, user_to_stop_following):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("delete from friend "
                "where friend.id = %s and friend.friendID = %s;")

        cursor.execute(query, (userid, user_to_stop_following))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return user_to_stop_following
    
    #12
    def show_groups(self, userid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("SELECT groupname.gid, groupname.groupname "
                "FROM persongroup "
                "join groupname on persongroup.gid = groupname.gid "
                "WHERE id = %s")

        cursor.execute(query, (userid, ))

        groups = []

        for (row) in cursor:
            group = Group(gid=row[0], groupname=row[1])
            groups.append(group)
        

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return groups
    
    #13
    def join_group(self, userid, gid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("INSERT INTO PersonGroup VALUES (%s,%s);")

        cursor.execute(query, (gid, userid))

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return gid
    
    #14
    def show_likes(self, pid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("SELECT PostLike.response, Person.username "
                "FROM Post INNER JOIN PostLike ON Post.pid = PostLike.pid "
                "LEFT JOIN GroupName ON GroupName.gid = Post.gid "
                "LEFT JOIN Person ON Person.id = PostLike.id "
                "WHERE Person.username IS NOT NULL AND Post.pid = %s;")
        
        cursor.execute(query, (pid, ))

        likes  = []

        for (row) in cursor:
            like = Like(response = row[0], username = row[1])
            likes.append(like)
        
        cursor.close()
        self.disconnect()

        return likes
    
    #15
    def create_group(self, userid, groupname):
        self.connect()
        cursor = self.cnx.cursor()

        query1 = ("insert into groupname "
                "values (NULL, %s)")
        
        query2 = ("select * from groupname "
                "order by gid desc limit 1")
        
        cursor.execute(query1, (groupname, ))

        cursor.execute(query2)

        new_gid = 1

        for (row) in cursor:
            new_gid = row[0]
        
        self.cnx.commit()
        self.disconnect()

        gid = self.join_group(userid, new_gid)
        return gid
    
    #16
    def get_userid(self, username):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select id from person where username = %s limit 1")

        cursor.execute(query, (username, )) 
        userid = -1

        for (row) in cursor:
            userid = row[0]

        cursor.close()
        self.disconnect()        
        return userid
    
    #17
    def get_unjoined_groups(self, userid):
        self.connect()
        cursor = self.cnx.cursor()

        query = ("select distinct groupname.gid, groupname.groupname from groupname "
                "join persongroup on groupname.gid = persongroup.gid "
                "where groupname.gid not in (select gid from persongroup where id = %s)")
        
        cursor.execute(query, (userid, ))

        groups = []

        for (row) in cursor:
            group = Group(gid=row[0], groupname=row[1])
            groups.append(group)
        

        cursor.close()
        self.cnx.commit()
        self.disconnect()

        return groups


    def connect(self):
        self.cnx = mysql.connector.connect(user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
    
    def disconnect(self):
        self.cnx.close()
