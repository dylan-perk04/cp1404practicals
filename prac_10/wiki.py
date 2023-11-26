import wikipedia

search = input("Input page title or search phrase here: ")
while search != "":
    try:
        page_summary = wikipedia.summary(search)
        print(page_summary)
        page = wikipedia.page(search)
        print(f"{page.title} {wikipedia.summary(page)} {page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search = input("Input page title or search phrase here: ")
print("Exit")
