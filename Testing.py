import webbrowser

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
chrome = webbrowser.get('chrome')
chrome.open_new_tab(url = "chat.openai.com")