#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Obtain a large set of repository IDs and their watchers, store as YAML"""

from time import sleep
from yaml import safe_dump
from github import github

def get_repositories(page, tries = 0):
  """Get a specific page from the list of repositories"""
  if tries > 3:
    return []
  try:
    return gh.repos.search('*', start_page = page)
  except:
    print "Retrying get_repositories"
    # Wait according to GitHub API policy
    sleep(tries*2+1)
    return get_repositories(page, tries+1)

def get_watchers(repo, tries = 0):
  """Get the list of watchers for a repository"""
  if tries > 3:
    return []
  try:
    return gh.repos.watchers(repo.username, repo.name)
  except:
    print "Retrying get_watchers"
    # Wait according to GitHub API policy
    sleep(tries*2+1)
    return get_watchers(repo, tries+1)

gh = github.GitHub()
# Collect and flatten the first 100 pages of repository (30 repos per page)
total_pages = 100
# Collect the watchers of each repository
repos = {}
for index, page in enumerate(range(1,total_pages+1)):
  print "Retrieving repositories (%d/%d)" % (index, total_pages)
  repos_page = get_repositories(page)
  for repo in repos_page:
    repo_id = "%s/%s" % (repo.username, repo.name)
    watchers = get_watchers(repo)
    repos[repo_id] = watchers
    with open('watchers.yaml', "a") as f:
      safe_dump({repo_id : watchers}, f, default_flow_style=False)
