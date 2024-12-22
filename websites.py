import requests


class Stack_of_websites:
    def __init__(self):
        self.websites = []
        self.size = -1
    def push(self,element):
        self.websites.append(element)
        self.size += 1
    def pop(self):
        if self.size < 0:
            return "No pages"
        self.websites.remove(self.websites[self.size])
        self.size -= 1
    def view(self):
        if self.size < 0:
            return "No pages"
        for i in self.websites:
            print(i)
    




def main():
    pages = Stack_of_websites()
    print("WEB BROWSER")
    while True:
        opening = input("Type A to Abort session , V to view pages, S to search: ")
        if opening == "V":
            pages.view()
        if opening == 'A':
            break
        search = input("Enter web page domain: ")
        pages.push(search)

    

        

        # Fetch the web page
        page = input("Enter F to fetch: ")
        if page == "F":
            url = f"http://{search}"
            try:
                response = requests.get(url)
    
                # Check if the request was successful
                if response.status_code == 200:
                    print("Page content fetched successfully!")
                    print(response.text)  # Display the content of the page
                else:
                    print(f"Failed to fetch the page. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        previous = input("Undo to go to to previous page: ")
        if previous == 'U':
            pages.pop()

if __name__ == "__main__":
    main()




    