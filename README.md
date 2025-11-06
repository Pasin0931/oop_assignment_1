## What is this lab all about?

- Practice converting procedural-style code into object-oriented code.  
- Demonstrates how to organize code using classes and objects (`Book`, `Member`, and `Library`) instead of purely procedural functions.  
- Reinforce encapsulation and class interaction concepts by organizing logic within appropriate classes.

---

## Project Structure

|--- oop_solution # File contained refactored code
| |--- library_oop.py # Answer
| |--- test.py # Testing file for refactored OOP code
|
|--- procedural_version # The analysis code
| |--- library_procedural.py # Original code
| |--- test.py # Testing file for original code (empty)
|
|--- README.md # Current file

---

## Design Overview

### Book
- **Purpose:** Store book details (ID, title, author, copies) and creates a template for book record.  
- **Attributes:** `id`, `title`, `author`, `total_copies`, `available_copies`  
- **Key Method:** `create_template()` returns a structured dictionary for storing in the library collection.

---

### Member
- **Purpose:** Stores member info (ID, name, email) and create a template for each valid member.  
- **Attributes:** `id`, `name`, `email`, `borrowed_books_list`  
- **Key Method:** `create_template()` creates a standardized member record for library tracking.

---

### Library
- **Purpose:** Contains all important operations, such as adding books/members, borrowing, returning, and displaying information.  
- **Responsibilities:**
  - Add new books and members  
  - Borrow and return books  
  - Display available books and member borrowing info  
  - Handle lookups for members and books

---

## Testing

### Basic Operations
- Adding books and members  
- Borrowing and returning books  
- Displaying available books and member borrowed lists  

### Edge Cases
- Borrowing unavailable books  
- Exceeding borrowing limit (max 3 books)  
- Returning books not borrowed  
- Handling non-existent books or members  

---

## Running the Code

You can run the code by typing the following command inside the terminal:

```bash
python library_oop.py