# Taylor Swift Album Finder GUI
In that GUI, a user will enter a month (maybe ttheir birth month) and find the corresponding Taylor Swift album.

## AI Model Used
I used **Copilot AI model "claude sonnet 4.5"**

## Setup
To use my gui I created a virtual enviorment venv in which copilot installed the library **"pillow"**

## How to Run

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the program:**
   ```bash
   python taylor_swift_month.py
   ```

3. **Use the GUI:**
   - Choose one of 3 input methods to enter your birth month
   - Option 1: Type the month name and click "Find My Album"
   - Option 2: Select from the dropdown menu and click "Go"
   - Option 3: Click directly on a month button (Jan, Feb, etc.)
   - Your Taylor Swift album and cover will be displayed!

---

## My Prompts

1. can yyou copy all files related to my  taylor_swift_month.py to a new folder called day03?

2. can you identify the  "business logic" (the computation) in this project and transfer it to a seperate file so the main progrem will use that file?

3. what kind of tests can i use for this logic?
    [copilot gave me a list and asked if i want it to create a file for all of them]

4. yes, also i would like for you to add an explaintionn on all test types to the readme file, do it under the number 5. (it''s in the file, empty)

5. can you move the test types explanation from 5. to the reflection section and rename it ""testing the logic"? also add the test results you gave me to this section

6. i dontt want the title reflection, i want it to be the testing the logic ttitle

7. thanks, do i need to remove one # so it will be ### instead of #### from the next sub-titles?

---

## Testing the Logic

After separating the business logic into `album_logic.py`, I can test it using different types of tests:

### **Unit Tests** (Basic Testing)
Tests individual functions with specific inputs to check if they return expected outputs.
- Example: Testing if `get_album_for_month("January")` returns `"Taylor Swift"`
- Why use it: Simple and straightforward, tests one thing at a time
- File: `test_album_logic.py` uses Python's `unittest` framework

### **Parameterized Tests**
Tests the same function with many different inputs efficiently.
- Example: Testing all 12 months with one test function instead of 12 separate tests
- Why use it: Reduces code duplication, easier to add more test cases
- Tools: `pytest` with `@pytest.mark.parametrize`

### **Property-Based Tests**
Automatically generates random test inputs to find edge cases.
- Example: Feeding random text to see if the function ever crashes
- Why use it: Finds bugs you didn't think to test for
- Tools: `hypothesis` library

### **Integration Tests**
Tests how different parts of the code work together.
- Example: Testing that the GUI can successfully get album data from the logic module
- Why use it: Makes sure the pieces fit together correctly

### **Edge Case Tests**
Tests unusual or extreme inputs that might break the code.
- Example: Empty strings, special characters, numbers, misspellings
- Why use it: Makes code more robust and user-friendly

### **Data Validation Tests**
Tests that the data structures are consistent and complete.
- Example: Checking that every album has a corresponding image file
- Why use it: Prevents data integrity issues

### **Running the tests:**
```bash
python -m unittest test_album_logic.py -v
```

### **Test Results:**
✅ **All 24 tests passed in 0.003 seconds!**

The tests verify that the business logic:
- Correctly maps all 12 months to albums
- Handles case-insensitive input (august, AUGUST, August all work)
- Handles whitespace properly
- Returns None for invalid inputs
- Maps albums to correct image filenames
- Has complete data integrity (every album has an image)

