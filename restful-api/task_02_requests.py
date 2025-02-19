#!/usr/bin/python3

"""
Function to fetch and print posts from the API
"""
import requests
import csv

def fetch_and_print_posts():
    """
    Function to fetch and print posts from the API
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    status_code = response.status_code
    print(f"Status code: {status_code}")
    if status_code == 200:
        json_posts = response.json()
        for post in json_posts:
            print(post['title'])

def fetch_and_save_posts():
    """
    Function to fetch and save posts to a CSV file
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    status_code = response
    if status_code == 200:
        json_posts = response.json()
        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
            writer.writeheader()
            for post in json_posts:
                writer.writerow(post)
