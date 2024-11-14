class Profile:
    # declaring attributes
    username: str
    bio: str
    followers: int
    following: int
    private: bool

    # initializing attributes
    def __init__(self):
        self.username = "usr9"
        self.bio = ""
        self.followers = 0
        self.following = 0
        self.private = False


# construct a new profile (instance of the profile class)
my_prof: Profile = Profile()
