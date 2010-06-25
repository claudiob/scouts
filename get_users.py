#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Obtain information (name, email, created_at) of repositories' watchers"""

from time import sleep
import yaml
from github import github

def get_info(user, tries = 0):
  """Get the information of a user"""
  if tries > 3:
    return []
  try:
    return gh.users.show(user).__dict__
  except:
    print "Retrying get_user_info"
    # Wait according to GitHub API policy
    sleep(tries*2+1)
    return get_info(user, tries+1)

# From http://stackoverflow.com/questions/429162
def streamInYAML(stream):
  y = stream.readline()
  cont = 1
  while cont:
    l = stream.readline()
    if len(l) == 0:
      cont = 0
    else:
      if l.startswith('-'):
        y = y + l
      else:
        yield yaml.load(y)
        y = l

gh = github.GitHub()
# Collect the position of each user in the list of watchers of each repository
users = []
with open('watchers.yaml', "r") as f:
  data = streamInYAML(f)
  for repos in data:
    for repo, watchers in repos.items():
      # Exclude repositories with very few watchers
      print "repo: %s" % repo
      if watchers and len(watchers) > 4:
        for watcher in watchers:
          if not watcher in users:
            users.append(watcher)
            user = get_info(watcher)
            with open('users.yaml', "a") as f:
              yaml.safe_dump({watcher : user}, f, default_flow_style=False)
