class library:
    
    def __init__(self):
        self.nobooks = 0
        self.books = []
    
    def show_info(self, book):
        self.books.append(book)
        self.nobook = len(self.books)
        
    def num(self):
        print(f"tis library has {self.nobook} books. The books are")
        for book in self.books:
            print(book)
    
a = library()
a.show_info("Quantum Physics")
a.show_info("Nano Technology")
a.show_info("World with AI")
a.show_info("World Economy")
a.num()