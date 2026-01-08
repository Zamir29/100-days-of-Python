from instagram_bot import InstaFollower

def main():
    insta_bot = InstaFollower()

    insta_bot.login()

    insta_bot.find_followers()

    insta_bot.follow()

if __name__ == '__main__':
    main()
