📌 Project Summary: GitHub User Activity Viewer

This Python script fetches and displays the recent public activity of any GitHub user using the GitHub Events API.

✔️ What the script does

Accepts a GitHub username as a command-line argument.

Sends a request to the GitHub API to retrieve the user’s recent public events.

Cleans and formats event types (e.g., PushEvent → Pushed).

Displays up to the five most recent activities, showing:

Event type

Repository name

Date of the event

Handles errors such as missing usernames, network issues, or invalid GitHub users.

🚀 How it works

Get Username
The script reads the GitHub username from the command line:
python github_activity.py <username>

It calls the GitHub API:
https://api.github.com/users/<username>/events/public

and retrieves the JSON event data.

Format Event Types
Converts raw API event types (e.g., CreateEvent, PushEvent) into friendly text.

Display Results
Shows a clean, readable list of the user’s latest activity with timestamps and repo names.

🛑 Error Handling

The script gracefully handles:

Missing username input

Invalid API responses

Network errors

Users with no recent activity

https://roadmap.sh/projects/github-user-activity
