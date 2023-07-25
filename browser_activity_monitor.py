import webbrowser
import time
import datetime

def log_website_activity(url, page_title, start_time, end_time):
    # Calculate the time duration
    time_duration = end_time - start_time

    # Log the information for the visited website
    print("Timestamp:", end_time)
    print("Website URL:", url)
    print("Page Title:", page_title)
    print("Total time duration:", time_duration)
    print("=" * 50)

def main():
    while True:
        # Ask the user to input a website URL
        url = input("Enter the URL of the website you want to visit (or 'exit' to quit): ")

        if url.lower() == 'exit':
            break

        # Open the website in the default web browser
        webbrowser.open(url)

        # Get the start time
        start_time = datetime.datetime.now()

        # Ask the user to input when they are done visiting the website
        input("Press Enter when you are done visiting the website: ")

        # Get the end time
        end_time = datetime.datetime.now()

        # Get the page title of the website
        page_title = None  # TODO: You can use a library like BeautifulSoup to extract the page title.

        # Log the website activity
        log_website_activity(url, page_title, start_time, end_time)

if __name__ == "__main__":
    main()
