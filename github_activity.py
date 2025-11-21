import sys
import requests


def get_username():
    # Check if a username argument was provided
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)  # Exit with an error code

    # The username is the second argument (index 1)
    username = sys.argv[1]
    return username


if __name__ == "__main__":
    username = get_username()
    # Now you have the username, e.g., 'octocat'


def fetch_activity(username):
    # Construct the API URL
    api_url = f"https://api.github.com/users/{username}/events/public"

    try:
        # Make the GET request to the API
        response = requests.get(api_url)

        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # Return the parsed JSON data as a Python list/dictionary
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle network errors, connection issues, or HTTP errors (like 404 Not Found)
        print(f"Error fetching data: {e}")
        sys.exit(1)

# Function to clean up the event type string for display


def format_event_type(event_type):
    # Example: 'CreateEvent' -> 'Created'
    # Example: 'PushEvent' -> 'Pushed'
    if event_type.endswith('Event'):
        return event_type[:-5]
    return event_type


def display_activity(activity_data):
    if not activity_data:
        print("No recent public activity found for this user.")
        return

    print(f"\n✨ Recent Activity ({len(activity_data)} events):")
    print("-" * 30)

    # We will only display the first 5 events for brevity
    for event in activity_data[:5]:
        # Get the event type (e.g., 'PushEvent')
        event_type = event.get('type', 'Unknown Event')

        # Get the repository name (e.g., 'octocat/Spoon-Knife')
        repo_name = event.get('repo', {}).get('name', 'N/A')

        # Get the creation time
        timestamp = event.get('created_at', 'N/A')

        # Format the output
        formatted_type = format_event_type(event_type)

        print(f"[{timestamp[:10]}] **{formatted_type}** in **{repo_name}**")

    print("-" * 30)
    print("For a full list of events, check the GitHub profile.")


# Final main block to tie it all together
if __name__ == "__main__":
    username = get_username()
    print(f"🔍 Searching for activity for GitHub user: **{username}**...")

    activity_data = fetch_activity(username)
    display_activity(activity_data)
