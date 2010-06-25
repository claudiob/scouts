#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Read a set of repositories and watchers, find the most talented ones"""

import yaml

# From http://stackoverflow.com/questions/429162
def streamInYAML(stream):
  y = stream.readline()
  cont = 1
  while cont:
    l = stream.readline()
    if len(l) == 0:
      cont = 0
    else:
      if l.startswith(' '):
        y = y + l
      else:
        try:
          yield yaml.load(y)
        except:
          print "Unicode mismatch"
        y = l

# Collect the position of each user in the list of watchers of each repository
scores = {}
with open('watchers.yaml', "r") as f:
  data = streamInYAML(f)
  for repos in data:
    for repo, watchers in repos.items():
      # Exclude repositories with very few watchers
      print "repo: %s" % repo
      if watchers and len(watchers) > 4:
        for index, watcher in enumerate(watchers):
          score = [index, len(watchers)]
          if watcher in scores:
            scores[watcher][repo] = score
          else:
            scores[watcher] = {repo : score} 
    
# Find the most talented scouts
scouts = []
for watcher, score in scores.items():
  # Exclude self-watchers
  for repo in score.keys():
    if repo.split("/")[0] == watcher:
      del score[repo]
  # Exclude watchers of repositories of a few creators
  if len(list(set([s.split("/")[0] for s in score.keys()]))) > 4:
    # TODO: Weaken watchers of repositories of the same user (e.g., your company)
    degree = sum([float(pos)/length for pos, length in score.values()])/float(len(score))
    scouts.append([degree, watcher])

scouts.sort()
print [s[1] for s in scouts[:10]]  

# Load users' info to limit scouts to those created in 2010
with open('users.yaml', "r") as f:
  data = streamInYAML(f)
  for chunk in data:
    u = users

recent_scouts = []
for scout in scouts:
  user = scout[1]
  if user in users and users[user] != [] and users[user]['created_at'][:4] == '2010':
    recent_scouts.append(scout)
    
print [s[1] for s in recent_scouts[:10]]  
