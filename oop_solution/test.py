# Library Management System - Procedural Style

class Book:
    def __init__(self, id, title, author, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies
    
    def create_template(self):
        book = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'available_copies': self.available_copies,
            'total_copies': self.total_copies
        }
        return book
    
class Member:
    def __init__(self, id, name, email, borrowed_books_list):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books_list = borrowed_books_list
        
    def create_template(self):
        member = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'borrowed_books': []
        }
        return member
    
class Library:
    def __init__(self, collections_of_books, members):
        self.collections_of_books = collections_of_books
        self.members = members
        
    def add_book(self, book_id, title, author, available_copies):
        
        this_ = Book(book_id, title, author, available_copies, available_copies).create_template()

        self.collections_of_books.append(this_)
        print(f"Book '{title}' added successfully!")
        
    def add_member(self, member_id, name, email):
        """Register a new library member"""

        this_ = Member(member_id, name, email, []).create_template()

        self.members.append(this_)
        print(f"Member '{name}' registered successfully!")
        
    def borrow_book(self, member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book['available_copies'] <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member['borrowed_books']) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        book['available_copies'] -= 1
        member['borrowed_books'].append(book_id)
        
        transaction = {
            'member_id': member_id,
            'book_id': book_id,
            'member_name': member['name'],
            'book_title': book['title']
        }
        borrowed_books.append(transaction)
        
        print(f"{member['name']} borrowed '{book['title']}'")
        return True

    def return_book(self, member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member['borrowed_books']:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        # Process the return
        book['available_copies'] += 1
        member['borrowed_books'].remove(book_id)
        
        # Remove from borrowed_books list
        for i, transaction in enumerate(borrowed_books):
            if transaction['member_id'] == member_id and transaction['book_id'] == book_id:
                borrowed_books.pop(i)
                break
        
        print(f"{member['name']} returned '{book['title']}'")
        return True
    
    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.collections_of_books:
            if book['available_copies'] > 0:
                print(f"{book['title']} by {book['author']} - {book['available_copies']} copies available")

    def display_member_books(self, member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member['name']} ===")
        if not member['borrowed_books']:
            print("No books currently borrowed")
        else:
            for book_id in member['borrowed_books']:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book['title']} by {book['author']}")
                    
    def find_book(self, book_id):
        """Find a book by ID"""
        for book in self.collections_of_books:
            if book['id'] == book_id:
                return book
        return None
    
    def find_member(self, member_id):
        """Find a member by ID"""
        for member in self.members:
            if member['id'] == member_id:
                return member
        return None

books = []
members = []
borrowed_books = []

# Test Code for Procedural Library System
def test_library_system():
    
    lib_ = Library(books, members)
    
    """Comprehensive test of all library functions"""
    
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM - COMPREHENSIVE TEST")
    print("=" * 60)
    
    # Test 1: Add Books
    print("\n--- TEST 1: Adding Books ---")
    lib_.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib_.add_book(2, "Clean Code", "Robert Martin", 2)
    lib_.add_book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1)
    lib_.add_book(4, "Design Patterns", "Gang of Four", 2)
    # print(books)
    
    # Test 2: Add Members
    print("\n--- TEST 2: Registering Members ---")
    lib_.add_member(101, "Alice Smith", "alice@email.com")
    lib_.add_member(102, "Bob Jones", "bob@email.com")
    lib_.add_member(103, "Carol White", "carol@email.com")
    
    # Test 3: Display Available Books
    print("\n--- TEST 3: Display Available Books ---")
    lib_.display_available_books()
    
    # # Test 4: Successful Book Borrowing
    print("\n--- TEST 4: Successful Borrowing ---")
    lib_.borrow_book(101, 1)  # Alice borrows Python Crash Course
    lib_.borrow_book(101, 2)  # Alice borrows Clean Code
    lib_.borrow_book(102, 1)  # Bob borrows Python Crash Course
    
    # Test 5: Display Member's Borrowed Books
    print("\n--- TEST 5: Display Member's Books ---")
    lib_.display_member_books(101)  # Alice's books
    lib_.display_member_books(102)  # Bob's books
    lib_.display_member_books(103)  # Carol's books (none)
    
    # Test 6: Display Available Books After Borrowing
    print("\n--- TEST 6: Available Books After Borrowing ---")
    lib_.display_available_books()
    
    # Test 7: Borrow Last Available Copy
    print("\n--- TEST 7: Borrowing Last Copy ---")
    lib_.borrow_book(103, 3)  # Carol borrows the only copy of Pragmatic Programmer
    lib_.display_available_books()
    
    # Test 8: Try to Borrow Unavailable Book
    print("\n--- TEST 8: Attempting to Borrow Unavailable Book ---")
    lib_.borrow_book(102, 3)  # Bob tries to borrow unavailable book
    
    # Test 9: Borrowing Limit Test
    print("\n--- TEST 9: Testing Borrowing Limit (3 books max) ---")
    lib_.borrow_book(101, 4)  # Alice's 3rd book
    lib_.display_member_books(101)
    lib_.borrow_book(101, 3)  # Alice tries to borrow 4th book (should fail)
    
    # Test 10: Return Books
    print("\n--- TEST 10: Returning Books ---")
    lib_.return_book(101, 1)  # Alice returns Python Crash Course
    lib_.return_book(102, 1)  # Bob returns Python Crash Course
    lib_.display_member_books(101)
    lib_.display_available_books()
    
    # Test 11: Try to Return Book Not Borrowed
    print("\n--- TEST 11: Attempting Invalid Return ---")
    lib_.return_book(102, 2)  # Bob tries to return book he didn't borrow
    
    # Test 12: Return and Borrow Again
    print("\n--- TEST 12: Return and Re-borrow ---")
    lib_.return_book(103, 3)  # Carol returns Pragmatic Programmer
    lib_.borrow_book(102, 3)  # Bob borrows it
    lib_.display_member_books(102)
    
    # Test 13: Error Cases - Non-existent Member/Book
    print("\n--- TEST 13: Error Handling ---")
    lib_.borrow_book(999, 1)  # Non-existent member
    lib_.borrow_book(101, 999)  # Non-existent book
    lib_.return_book(999, 1)  # Non-existent member
    lib_.display_member_books(999)  # Non-existent member
    
    # Test 14: Final Status
    print("\n--- TEST 14: Final Library Status ---")
    print("\nAll Borrowed Books:")
    for transaction in borrowed_books:
        print(f"  {transaction['member_name']} has '{transaction['book_title']}'")
    
    print("\nAll Members and Their Books:")
    for member in members:
        print(f"\n{member['name']} ({member['id']}):")
        if member['borrowed_books']:
            for book_id in member['borrowed_books']:
                book = lib_.find_book(book_id)
                print(f"  - {book['title']}")
        else:
            print("  (No books borrowed)")
    
    lib_.display_available_books()
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE")
    print("=" * 60)

# Run the comprehensive test
if __name__ == "__main__":
    test_library_system()