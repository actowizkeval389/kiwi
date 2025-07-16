from DrissionPage import Chromium
import time

# Initialize browser
browser = Chromium()
tab = browser.latest_tab
tab.cookies().clear()


# Start listening for GraphQL requests
tab.listen.start("https://api.skypicker.com/umbrella/v2/graphql?featureName=SearchOneWayItinerariesQuery")

# Open the search results page
tab.get('https://www.kiwi.com/en/search/results/muscat-oman/kuwait-city-kuwait/2025-07-26/no-return')

# Loop to click "Load More" until it disappears
while True:
    load_more = tab.ele(
        'xpath://div[contains(text(), "Load more")]'
    )

    if not load_more:
        print("No more 'Load More' button found.")
        break
    print("Clicking 'Load More'...")
    load_more.click()

    # Wait for content to load (you can optionally listen for a specific request here)
    time.sleep(1)  # Adjust based on your connection speed or use tab.wait()

responses = [packet.response.body for packet in tab.listen.steps()]

# Get the last response body (most recent one)
if responses:
    last_response = responses[-1]
    print("Last GraphQL Response Body:")
    print(last_response)
else:
    print("No GraphQL responses were captured.")

