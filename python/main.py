from connector import Sql

if __name__ == "__main__":

    def tests():

        sql = Sql()

        #1
        #print(sql.get_user_password('AaronBass15164'))

        #2
        #print(sql.show_friends_posts('660791208540'))

        #3
        #print(len(sql.show_groups_posts('660791208540')))

        #4
        #print(sql.show_following('1172919682829981218917638120420'))

        #5
        #print(sql.show_comments('1172919682829981218917638120420'))

        #6
        # print(sql.get_highest_pid())
        # print(sql.add_post('117291968282998', '10216646959432839', 'test from backend 2'))
        # print(sql.get_highest_pid())

        #7
        # print(sql.add_comment('660791208540' , '117291968282998', '1172919682829981218917638120420', 'comment from backend 2'))

        #8
        # print(sql.follow('503442187183', '521026065681'))

        #9
        #print(sql.create_user('sarthak', 'password'))

        #10
        #print(sql.create_like('117291968282998', '660791208540', '1172919682829981218917638120420', 'TEST'))

        #11
        #print(sql.stop_following('660791208540', '1460241457335169'))

        #12
        #print(sql.show_groups('521026065681'))

        #13
        #print(sql.join_group('521026065681', '335787510131917'))

        #14
        #print(sql.show_likes('1172919682829981000197413325778'))

        #15
        #print(sql.create_group('521026065681','backend3'))

        #16
        #print(sql.get_userid('vyom'))

        #17
        #print (sql.get_unjoined_groups('1'))


    tests()