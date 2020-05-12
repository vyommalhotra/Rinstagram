from objects import *

class State(object):

    def __init__(self):
        print ()

    def on_event(self):

        pass

    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__

class InitialState():
    def on_event(self, action):
        if action == 'login':
            return LoginState()
        elif action == 'signup':
            return SignupState()
        elif action == 'exit':
            return ExitState()

class SignupState():
    def on_event(self, provider, username, password):
        if provider.add_user(username, password):
            print("successfully created user {}\n".format(username))
            return InitialState()
        else:
            print("username already exists.\n")
            return InitialState()

class LoginState(State):
    def on_event(self, provider, username, password):
        if provider.validate_user(username, password):
            return GroupsState()
        
        else:
            print("invalid login\n")
            return InitialState()

class ShowPostsState(State):
    def on_event(self, action):
        if (action == 'exit\n'):
            return ExitState()
        elif (action == 'back\n'):
            return GroupsState()
        else:
            pid = action.split()[0]
            gid = action.split()[1]
            return SelectPostState(pid, gid)
            

class JoinGroupState(State):
    def on_event(self, provider, action):
        if action == 'exit':
            return ExitState()
        elif action == 'back':
            return GroupsState()
        else:
            provider.join_group(action)
            return GroupsState()

class CreateGroupState():
    def on_event(self, provider, groupname):
        provider.create_group(groupname)
        print('succesfully created group {}'.format(groupname))
        return GroupsState()
        

class FriendsPostsState(State):
    def on_event(self, action):
        if (action == 'exit\n'):
            return ExitState()
        elif (action == 'back\n'):
            return GroupsState()
        else:
            pid = action.split()[0]
            gid = action.split()[1]
            return SelectPostState(pid, gid)

class AddFollowerState(State):
    def on_event(self, provider, username):
        if provider.add_following(username):
            print('successfully following {}'.format(username))
            return GroupsState()
        else:
            print('invalid user')
            return GroupsState()

class ViewFollowerState(State):
    def on_event(self, action):
        if action == 'exit':
            return ExitState()

        if action == 'back':
            return GroupsState()

class RemoveFollowerState(State):
    def on_event(self, provider, username):
        if provider.remove_following(username):
            print('succesfully stopped following {}'.format(username))
            return GroupsState()
        else:
            print("invalid user")
            return GroupsState()

class CreatePostSelectState(State):
    def on_event(self, provider, gid, msg):
        provider.add_post(gid, msg)
        print("succesfully posted")
        return ShowPostsState()

class SelectPostState(State):
    def __init__(self, pid, gid):
        self.pid = pid
        self.gid = gid

    def on_event(self, action):
        if action == 'show likes':
            return PostShowLikesState(self.pid, self.gid)
        if action == 'show comments\n':
            return PostShowCommentsState(self.pid, self.gid)
        if action == 'add a like':
            return PostAddLikeState(self.pid, self.gid)
        if action == 'add a comment\n':
            return PostAddCommentState(self.pid, self.gid)
        if action == 'exit':
            return ExitState()
        if action == 'back':
            return GroupsState()
        pass

class PostShowLikesState(State):
    def __init__(self, pid, gid):
        self.pid = pid
        self.gid = gid

    def on_event(self, action):
        if action == 'back':
            return SelectPostState(self.pid, self.gid)
        else:
            return ExitState()

class PostAddLikeState(State):
    def __init__(self, pid, gid):
        self.pid = pid
        self.gid = gid

    def on_event(self, provider, action):
        provider.add_like(self.gid, self.pid, action)
        print("like added")
        return PostShowLikesState(self.pid, self.gid)

class PostAddCommentState(State):
    def __init__(self, pid, gid):
        self.pid = pid
        self.gid = gid

    def on_event(self, provider, comment):
        provider.add_comment(self.gid, self.pid, comment)
        print("comment created")
        return PostShowCommentsState(self.pid, self.gid)

class PostShowCommentsState(State):
    def __init__(self, pid, gid):
        self.pid = pid    
        self.gid = gid

    def on_event(self, action):
        if action == 'back':
            return SelectPostState(self.pid, self.gid)
        else:
            return ExitState()

class GroupsState(State):
    def on_event(self, provider, action):
        if action == 'view posts from topics you follow':
            return ShowPostsState()
        elif action == 'create a post':
            return CreatePostSelectState()
        elif action == 'view posts from users you follow\n':
            return  FriendsPostsState()
        elif action == 'follow a new topic':
            return JoinGroupState()    
        elif action == 'create a topic\n':
            return CreateGroupState()
        elif action == 'view users you are following':
            return ViewFollowerState()
        elif action == 'follow a new user':
            return AddFollowerState()
        elif action == 'stop following a user\n':
            return RemoveFollowerState()
        elif action == 'exit':
            print("goodbye.")
            return ExitState()

class ExitState(State):
    pass




