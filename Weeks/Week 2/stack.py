# Create an empty list to represent a browsing session
browsing_session = []
browsing_session.append("youtube.com")
browsing_session.append("google.com")
browsing_session.append("twitter.com")
print(browsing_session)

last = browsing_session.pop()
print("Last visited site:", last)
print(browsing_session)
print("Number of sites visited:", len(browsing_session))
print("redirecting to", browsing_session[-1])
if not browsing_session:
    print("Disable browsing session yet")