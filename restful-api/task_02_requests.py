#!/usr/bin/python3
# task_02_requests.py

import requests
import csv

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print their titles."""
    try:
        response = requests.get(API_URL)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()  # Parse JSON data
            for post in posts:
                print(post.get("title"))
        else:
            print("Failed to fetch posts.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them as posts.csv."""
    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            posts = response.json()

            # Structure the data as a list of dictionaries
            structured_posts = [
                {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
                for post in posts
            ]

            # Write to CSV
            with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["id", "title", "body"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(structured_posts)

            print("Posts have been saved to posts.csv")
        else:
            print(f"Failed to fetch posts. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
