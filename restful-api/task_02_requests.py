#!/usr/bin/python3
"""
Functions that fetch and print posts from the API and save them to a CSV file
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
    status_code = response.status_code
    if status_code == 200:
        json_posts = response.json()
        with open('posts.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            for post in json_posts:
                filtered = {key: post[key] for key in ['id', 'title', 'body']}
                writer.writerow(filtered)


if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
