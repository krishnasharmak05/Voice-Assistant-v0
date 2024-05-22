import webbrowser

# Paths given below are the default locations of the apps. They might have been changed.
browser_paths = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "opera": r"C:\Users\<username>\AppData\Local\Programs\Opera\launcher.exe",
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
}
for i in browser_paths:
    webbrowser.register(i, None, webbrowser.BackgroundBrowser(browser_paths[i]))
chrome = webbrowser.get('chrome')
edge = webbrowser.get('edge')
opera = webbrowser.get('opera')


def google_search(value: int, query_from_speech: str):
    removed_prefix = remove_prefix(query_from_speech, value)
    base_url = "https://www.google.com/search?q="
    final_url = base_url + removed_prefix
    webbrowser.open_new_tab(final_url)


def remove_prefix(temp_query: str, number_of_words_to_be_removed: int = 3):
    query = ""
    for i in range(len(temp_query.split())):
        if i < number_of_words_to_be_removed:
            pass
        else:
            query += temp_query.split()[i] + " "
    if not query:
        query = temp_query
    return query


def browse_a_specific_url(lower_command, browser:str='edge'):
    url = lower_command.removeprefix("open ")
    if browser == 'edge':
        edge.open(url = url,new = 2)
    elif browser == 'chrome':
        chrome.open(url = url,new = 2)
    elif browser == 'opera':
        opera.open(url = url,new = 2)