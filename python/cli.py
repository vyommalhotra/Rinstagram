from middle import Provider
from objects import *
from whaaaaat import prompt
from state import *
import json

class CLI:

    def __init__(self):
        self.state = InitialState()
        self.provider = Provider()
        print("Welcome to rinstagram. A simple social media platform.\n")
    
    def run(self):

        if isinstance(self.state, InitialState):
            self.initial_page()
            self.run()
        
        elif isinstance(self.state, SignupState):
            self.signup_page()
            self.run()
        
        elif isinstance(self.state, LoginState):
            self.login_page()
            self.run()

        elif isinstance(self.state, GroupsState):
            self.groups_page()
            self.run()
        
        elif isinstance(self.state, JoinGroupState):
            self.join_group_page()
            self.run()
        
        elif isinstance(self.state, ShowPostsState):
            self.show_posts_page()
            self.run()
        
        elif isinstance(self.state, ViewFollowerState):
            self.show_following_page()
            self.run()

        elif isinstance(self.state, FriendsPostsState):
            self.show_friends_posts_page()
            self.run()
        
        elif isinstance(self.state, CreateGroupState):
            self.show_create_group_page()
            self.run()
        
        elif isinstance(self.state, AddFollowerState):
            self.show_add_follow_page()
            self.run()
        
        elif isinstance(self.state, RemoveFollowerState):
            self.show_remove_follow_page()
            self.run()
        
        elif isinstance(self.state, CreatePostSelectState):
            self.show_create_post_select_page()
            self.run()

        elif isinstance(self.state, SelectPostState):
            self.show_select_post_page()
            self.run()

        elif isinstance(self.state, PostShowLikesState):
            self.show_post_like_page()
            self.run()
        
        elif isinstance(self.state, PostShowCommentsState):
            self.show_comments_page()
            self.run()

        elif isinstance(self.state, PostAddLikeState):
            self.show_add_like_page()
            self.run()
        
        elif isinstance(self.state, PostAddCommentState):
            self.show_add_comment_page()
            self.run()

        elif isinstance(self.state, ExitState):
            print('goodbye.')
            pass
    
    def initial_page(self):
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'Please select one of the options:',
                'choices': 
                [
                    'login',
                    'signup',
                    'exit'
                ]
            }
        ]

        answers = prompt(questions)
        action = answers['action']

        self.state = self.state.on_event(action)
    
    def signup_page(self):
        questions = [{'type': 'input','name': 'username','message': 'username:',},
                        {'type': 'password', 'name': 'password', 'message': 'password:'}]
        answers = prompt(questions)
        username = answers['username']
        password = answers['password']

        self.state = self.state.on_event(self.provider, username, password)

    def login_page(self):
        questions = [{'type': 'input','name': 'username','message': 'username:',},
                        {'type': 'password', 'name': 'password', 'message': 'password:'}]
        answers = prompt(questions)
        username = answers['username']
        password = answers['password']
        
        self.state = self.state.on_event(self.provider, username, password)       

    def groups_page(self):
        groups = self.provider.show_groups()
        print("Welcome {} \n \nTopics you are currently part of :".format(self.provider.username))
        for group in groups:
            print( '-' + group.groupname)
        print()
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What do you want to do?',
                'choices': 
                [
                    'create a post',
                    'view posts from topics you follow',
                    'view posts from users you follow\n',
                    'follow a new topic',
                    'create a topic\n',
                    'view users you are following',
                    'follow a new user',
                    'stop following a user\n',
                    'exit'
                ]
            }
        ]

        answers = prompt(questions)  
        action = answers['action']

        self.state = self.state.on_event(self.provider, action)

    def join_group_page(self):
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'select a topic to follow:',
                'choices': []
            }
        ]        

        for group in self.provider.show_unjoined_groups():
            questions[0]['choices'].append({'name': '-' + group.groupname, 'value': group.gid})
        
        questions[0]['choices'].append('exit')
        questions[0]['choices'].append('back')

        answers = prompt(questions)
        action = answers['action']

        self.state = self.state.on_event(self.provider, action)
    
    def show_posts_page(self):
        posts = self.provider.show_posts()
        
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'select a post to see likes/comments:',
                'choices': []
            }
        ]

        questions[0]['choices'].append('exit\n')
        questions[0]['choices'].append('back\n')

        for post in posts:
            msg = str(post.msg)
            message ='topic:  ' + post.groupname + '\n   time:  ' + post.timestamp.strftime('%H:%M %b %d %Y') + '\n   user:  ' + post.username + '\n   ' + self.provider.replace_special_characters(msg) + '\n   likes: ' + str(post.likes) + '\n'
            questions[0]['choices'].append({'name': message, 'value': post.pid + ' ' + str(post.gid) })

        answers = prompt(questions)
        self.state = self.state.on_event(answers['action'])
    
    def show_following_page(self):
        print("Here are all the users you are currently following:\n")

        following = self.provider.get_friends()

        for user in following:
            print(user)
        
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What do you want to do?',
                'choices': 
                [
                    'back',
                    'exit'
                ]
            }
        ]

        answers = prompt(questions)  
        self.state = self.state.on_event(answers['action'])
    
    def show_friends_posts_page(self):
        print("Here all the posts from users you follow\n")

        posts = self.provider.show_friends_posts()

        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'select a post to see likes/comments:',
                'choices': []
            }
        ]

        questions[0]['choices'].append('exit\n')
        questions[0]['choices'].append('back\n')

        for post in posts:
            message ='topic:  ' + post.groupname + '\n   time:  ' + post.timestamp.strftime('%H:%M %b %d %Y') + '\n   user:  ' + post.username + '\n   ' + self.provider.replace_special_characters(post.msg) + '\n   likes: ' + str(post.likes) + '\n'
            questions[0]['choices'].append({'name': message, 'value': post.pid + ' ' + str(post.gid)})

        if(len(posts) < 1):
            print("there are no posts here. try following more people.")

        answers = prompt(questions)
        self.state = self.state.on_event(answers['action'])
    
    def show_create_group_page(self):
        questions = [{'type': 'input','name': 'groupname','message': 'new topic name: ',}]
        answers = prompt(questions)
        groupname = answers['groupname']
        
        self.state = self.state.on_event(self.provider, groupname)
    
    def show_add_follow_page(self):
        questions = [{'type': 'input','name': 'username','message': 'user to start following: ',}]
        answers = prompt(questions)
        username = answers['username']
        
        self.state = self.state.on_event(self.provider, username)
    
    def show_create_post_select_page(self):
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'select a topic to post to:',
                'choices': []
            }
        ]        

        for group in self.provider.show_groups():
            questions[0]['choices'].append({'name': '-' + group.groupname, 'value': group.gid})
        
        questions[0]['choices'].append('exit')
        questions[0]['choices'].append('back')

        answers = prompt(questions)
        action = answers['action']

        if action == 'exit':
            self.state = ExitState()
        elif action == 'back':
            self.state = GroupsState()
        else:
            gid = action    
            
            questions = [{'type': 'input','name': 'msg','message': 'message:'}]
            answers = prompt(questions)
            msg = answers['msg']

            self.state = self.state.on_event(self.provider, gid, msg)
    
    def show_select_post_page(self):
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'Please select one of the options:',
                'choices': 
                [
                    'show likes',
                    'show comments\n',
                    'add a like',
                    'add a comment\n',
                    'exit',
                    'back'
                ]
            }
        ]

        answers = prompt(questions)
        action = answers['action']

        self.state = self.state.on_event(action)
    
    def show_post_like_page(self):
        print('likes:\n')
        
        for like in self.provider.get_likes(self.state.pid):
            print(like.username + '   ' + like.response)

        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What do you want to do?',
                'choices': 
                [
                    'back',
                    'exit'
                ]
            }
        ]

        answers = prompt(questions) 
        self.state = self.state.on_event(answers['action'])
        
    def show_comments_page(self):
        print('comments:\n')
        
        comments = self.provider.get_comments(self.state.pid)

        if len(comments) > 0:
            for comment in comments:
                print(comment.username + '   ' + comment.timestamp.strftime('%H:%M %b %d %Y') + '\n       ' + self.provider.replace_special_characters(comment.msg) + '\n')

        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'What do you want to do?',
                'choices': 
                [
                    'back',
                    'exit'
                ]
            }
        ]

        answers = prompt(questions) 
        self.state = self.state.on_event(answers['action'])

    def show_add_comment_page(self):
        questions = [{'type': 'input','name': 'comment','message': 'comment: ',}]
        answers = prompt(questions)
        comment = answers['comment']
        
        self.state = self.state.on_event(self.provider, comment)        

    def show_add_like_page(self):
        questions = [
            {
                'type': 'list',
                'name': 'action',
                'message': 'Please select a type of response:',
                'choices': 
                [
                    'LIKE',
                    'LOVE',
                    'SAD'
                ]
            }
        ]

        answers = prompt(questions)
        action = answers['action']

        self.state = self.state.on_event(self.provider, action)
        
    def show_remove_follow_page(self):
        questions = [{'type': 'input','name': 'username','message': 'user to stop following: ',}]
        answers = prompt(questions)
        username = answers['username']
        
        self.state = self.state.on_event(self.provider, username)

CLI().run()