# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=12000,
                                    min_followers=0,
                                    min_following=0)

    session.set_skip_users(skip_private=False,
                           private_percentage=0)

    session.follow_user_followers(
        [''],
        amount=125,
        randomize=False, interact=False)

    session.join_pods()
