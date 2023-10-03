class Article:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return f"Title: {self.title}\nContent:\n{self.content}\n"


def create_article():
    title = input("Enter the article title: ")
    content = input("Enter the article content: ")
    article = Article(title, content)
    with open(f"{title}.txt", "w") as file:
        file.write(str(article))
    print("Article created successfully!")

def read_article():
    title = input("Enter the article title: ")
    try:
        with open(f"{title}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Article '{title}' not found.")

def update_article():
    title = input("Enter the article title: ")
    try:
        with open(f"{title}.txt", "r") as file:
            article = Article(title, file.read())
            new_content = input("Enter the updated content: ")
            article.content = new_content
        with open(f"{title}.txt", "w") as file:
            file.write(str(article))
        print("Article updated successfully!")
    except FileNotFoundError:
        print(f"Article '{title}' not found.")

def delete_article():
    title = input("Enter the article title: ")
    try:
        os.remove(f"{title}.txt")
        print(f"Article '{title}' deleted successfully!")
    except FileNotFoundError:
        print(f"Article '{title}' not found.")



while True:
    print("\nOptions:")
    print("1. Create Article")
    print("2. Read Article")
    print("3. Update Article")
    print("4. Delete Article")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        create_article()
    elif choice == '2':
        read_article()
    elif choice == '3':
        update_article()
    elif choice == '4':
        delete_article()
    elif choice == '5':
        print("Exiting the CMS. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
