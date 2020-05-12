from connector import Sql
import objects
import re

class Provider:

    def __init__(self):
        self.sql = Sql()
        self.userid = 0
        self.username = ""

    def validate_user(self, username, password):
        correct_password = self.sql.get_user_password(username)

        if correct_password == '':
            return False
        
        if correct_password == password:
            self.userid = self.sql.get_userid(username)
            self.username = username
            return True
        
        else:
            return False
    
    def show_groups(self):
        return self.sql.show_groups(self.userid)
    
    def show_unjoined_groups(self):
        return self.sql.get_unjoined_groups(self.userid)

    def user_exists(self, username):
        return self.sql.user_exists(username)
    
    def add_user(self, username, password):
        return self.sql.create_user(username, password)
    
    def show_posts(self):
        posts = self.sql.show_groups_posts(self.userid)
        posts.sort(key=lambda p: p.timestamp, reverse=True)
        return posts
    
    def show_friends_posts(self):
        posts = self.sql.show_friends_posts(self.userid)
        posts.sort(key=lambda p: p.timestamp, reverse=True)
        return posts        
    
    def join_group(self, gid):
        self.sql.join_group(self.userid, gid)
    
    def create_group(self, groupname):
        self.sql.create_group(self.userid, groupname)

    def get_friends(self):
        return self.sql.show_following(self.userid)
    
    def add_following(self, username):
        userid = self.sql.get_userid(username)
        if userid != -1:
            self.sql.follow(self.userid, userid)
            return True

        else:
            return False
    
    def remove_following(self, username):
        userid = self.sql.get_userid(username)

        if userid != -1:
            self.sql.stop_following(self.userid, userid)
            return True

        else:
            return False
    
    def add_post(self, gid, msg):
        self.sql.add_post(self.userid, gid, msg)

    def get_likes(self, pid):
        return self.sql.show_likes(pid)
    
    def get_comments(self, pid):
        comments = self.sql.show_comments(pid)
        comments.sort(key=lambda c: c.timestamp, reverse=True)
        return comments

    def add_comment(self, gid, pid, msg):
        self.sql.add_comment(self.userid, gid, pid, msg)
    
    def add_like(self, gid, pid, response = 'LIKE'):
        self.sql.create_like(gid, self.userid, pid, response)

    def replace_special_characters(self, msg):
        replaced = re.sub('\{RET\}', '\n   ', msg)
        replaced = re.sub('\{APOST\}', '\'', replaced)
        replaced = re.sub('\{COMMA\}', ',', replaced)

        return replaced
        

