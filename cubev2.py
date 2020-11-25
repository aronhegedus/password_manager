import subprocess
import os
import git

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PASSWORD_DIR = os.path.join(ROOT_DIR, 'passwords')

repo = git.Repo(os.path.join(ROOT_DIR, '.git'))

def git_pull():
    """
    Do a git pull
    TODO think about what could go wrong
    """
    repo.git.pull('origin')

def get_password(server, user='root'):
    """
    Gets the text inside the file of user@server
    """
    with open(os.path.join(PASSWORD_DIR, server, user, 'password'), 'r') as f:
        password = f.readline().strip()
    
    print(password, 'is password')

def add_password(server, user='root', password='1234'):
    """
    Change the password for something
    """
    password_folder = os.path.join(PASSWORD_DIR, server, user)
    try:
        os.makedirs(password_folder)
    except OSError as e:
        print('already exists, skipping')

    with open(os.path.join(PASSWORD_DIR, server, user, 'password'), 'w') as f:
        f.write(password)
    print('Changed the password to ', server)
    git_add_commit_push(os.path.join('passwords', server, user, 'password'))
    # TODO add git commit and git push

def git_add_commit_push(filepath):
    """
    pushing a file
    """
    print('about to do git stuff')
    repo.git.add(os.path.join(ROOT_DIR, filepath))
    #TODO better commit messages
    repo.index.commit('Changing the password to {}'.format(filepath))
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == '__main__':
    # Parse the arguments, and run
    # TODO add a git pull here
    get_password(server='lurch')
    add_password(server='lurch')
    get_password(server='lurch')
    
    add_password(server='new_eas_git')
    get_password(server='new_eas_git')

