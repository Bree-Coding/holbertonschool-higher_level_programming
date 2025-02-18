#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    status_code = response.status_code
    print(f"Status code: {status_code}")
    if status_code == 200:
        json_posts = response.json()
        for post in json_posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    status_code = response
    if status_code == 200:
        json_posts = response.json()
        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['userId', 'id', 'title', 'body'])
            writer.writeheader()
            for post in json_posts:
                writer.writerow(post)
