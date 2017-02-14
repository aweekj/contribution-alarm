# -*- coding: utf-8 -*-
import configparser
import datetime

import tweepy
from github import Github


class AlarmBot():
    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read('config.ini')

        self.username = parser['github']['username']
        self.password = parser['github']['password']
        self.consumer_key = parser['twitter_application']['consumer_key']
        self.consumer_secret = parser['twitter_application']['consumer_secret']
        self.access_token = parser['twitter_application']['access_token']
        self.access_token_secret = parser['twitter_application']['access_token_secret']
        self.username_to_mention = parser['twitter_account']['username_to_mention']

    def connect_to_github(self):
        user = Github(self.username, self.password).get_user(self.username)
        return user

    def get_contributions(self, user):
        today = datetime.datetime.today()
        today_date = datetime.datetime(today.year, today.month, today.day)
        today_date_ko = today_date - datetime.timedelta(hours=9)

        contributions = []

        for event in user.get_events():
            if event.created_at > today_date_ko:
                if event.type in ['PushEvent', 'PullRequestEvent']:
                    contributions.append(event)
            else:
                break

        return contributions

    def connect_to_twitter(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        return api

    def send_tweet(self, message):
        self.connect_to_twitter().update_status(status=message)

    def contribution_alarm(self):
        user = self.connect_to_github()
        today_contributions = self.get_contributions(user)

        if len(today_contributions) == 0:
            message = "@"+self.username_to_mention+" 아니"

        else:
            message = "@"+self.username_to_mention+" 응"

        self.send_tweet(message)


if __name__ == '__main__':
    bot = AlarmBot()
    bot.contribution_alarm()