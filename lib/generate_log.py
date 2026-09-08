import requests
from datetime import datetime


def fetch_data():
    """Fetch a sample post from JSONPlaceholder API."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(log_data):
    """Write a list of log entries to a dated text file."""
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


def write_log(post):
    """Write API data and activity logs to a timestamped file."""
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported",
        f"Fetched Post Title: {post.get('title', 'No title found')}",
        f"Fetched Post ID: {post.get('id', 'Unknown')}"
    ]

    return generate_log(log_data)


def main():
    print("Starting Python automation tool...")

    post = fetch_data()

    if post:
        print("API data fetched successfully.")
        print("Fetched Post Title:", post.get("title", "No title found"))
    else:
        print("Failed to fetch API data.")

    filename = write_log(post)

    print(f"Log written to {filename}")
    print("Automation completed successfully.")


if __name__ == "__main__":
    main()
