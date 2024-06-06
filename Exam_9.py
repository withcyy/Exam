class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

    def del_page(self, page):
        if page in self.pages:
            self.pages.remove(page)
        else:
            print("Error!!!")

    def display_site(self):
        print("Website name: ", self.name)
        print("URL: ", self.url)
        print("Pages: ")
        for i in self.pages:
            print("-", i.title)

class WebPage:
    def __init__(self, title, content, date):
        self.title = title
        self.content = content
        self.date = date

    def display_page(self):
        print("Title: ", self.title)
        print("Content: ", self.content)
        print("Date: ", self.date)

def main():
    print("Menu of the site: ")
    website_name = input("Name: ")
    website_url = input("URL: ")
    website = WebSite(website_name, website_url)

    while True:
        print("Menu: ")
        print("1. Append page")
        print("2. Delete page")
        print("3. Display info")
        print("4. Display page")
        print("0. Exit")
        user_choice = input("(1-4): ")

        if user_choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            date = input("Date: ")
            web_page = WebPage(title, content, date)
            website.add_page(web_page)
        elif user_choice == "2":
            if website.pages:
                for i, page in enumerate(website.pages):
                    print(f"{i + 1}. {page.title}")
                user_choice_del = int(input("Choice index of the page: ")) - 1
                if 0 <= user_choice_del < len(website.pages):
                    website.del_page(website.pages[user_choice_del])
                else:
                    print("Error!!!")
            else:
                print("Error!!!")
        elif user_choice == "3":
            print("Website info:")
            website.display_site()
        elif user_choice == "4":
            if website.pages:
                for i, page in enumerate(website.pages):
                    print(f"{i + 1}. {page.title}")
                user_choice_page = int(input("Choice index of page: ")) - 1
                if 0 <= user_choice_page < len(website.pages):
                    website.pages[user_choice_page].display_page()
                else:
                    print("Error!!!")
            else:
                print("Error!!!")
        elif user_choice == "0":
            print("Exiting...")
            break
        else:
            print("Error!!!")

if __name__ == "__main__":
    main()


