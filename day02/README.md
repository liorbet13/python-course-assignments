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

1. hi, create a new ffile in the folder day02. in that file create a gui in which a user will give a month (their birth month) and they gui will tell them what ttheir correspondding Taylor Swiftt album is (for now give it numbere 1-12, we will updatte tthe acttual aalbum naames soon)

2. okay great, now lets change the input to month names: 1 is January aand so on with a capital letter at the begining of each month

3. Great! now let's updatte tthe album names, do you need me to give a list or can you find them?

4. Greaat! one correction - the 12th album is "The Life of a Showgirl"

5. is it possible to display a picture with the result?/ i want to display album coovers, i caan provide images

6. [to installing the pillow package] yes thank you

7. [for the images] can you creat the folder? i will add the files

8. i added all the images, can you find them?>

9. whenn i run it it says image is not found. any ideas?

10. Amazing! now we style it a little different? remove the little icons and change the font?

11. can you set the image backround.jpg from album_covers as the backround and put tthe interface on the left side of the character?

12. the image doesnt appear as backround, why? [i had a ttypo in the file name]

13. thanks! can you remove the white frame and make the font ADLaM Display in BOLD?

14. can you update the code? i dont see those changes  
    [AI couldnt do it and gave me a list for available fonts]

15. can yoou make the Title in IMPACT and the rest in georgia?

16. can you also change 'find my album'' to impact? and enlarge the title font?

17. can you also make the buttton font (and sizze) bigger? not by much but by 2 points

18. change the buttun tto 18pt

19. can you remove the ' yoour taylor swiftt album is' linne and only leave the name and image?

20. also change the album name font to impact and make it 18pt

21. change the title to ' What is you Taylor Swift Album?'

22. can you put the word album in a new line below?

23. can you increase the gui size so the album image would not be crropped at the bottom?

24. Amazing! one last thing, can you remove the white frame?  
    [AI couldnt do it since it required another package to make the frame transperent I decided to leave it as is and reveret that change]

25. can you adjust tthe code so it caan recieve 3 input mechanisms?  
    [gives me 5 options] 1 2 and 3 sound good

26. [an errror massage appears when i run the gui, i copy and pasted the massage] Whats thee problem:  
    ```
    File "C:\Users\Lior Batat\AppData\Local\Programs\Python\Python313\Lib\tkinter\__init__.py", line 3367, in __init__
        Widget.__init__(self, master, 'label', cnf, kw)
        ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "C:\Users\Lior Batat\AppData\Local\Programs\Python\Python313\Lib\tkinter\__init__.py", line 2780, in __init__
        self.tk.call(
        ~~~~~~~~~~~~^
            (widgetName, self._w) + extra + self._options(cnf))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ```
    [copilot fixed it by removing empty background color commands]

27. Thank you tthat's great! can you fixe tthe gui size so theresult image isnt cropped froom the bottom?

28. perfect!

29. Hi can you reorganize the lines in this file (README inside the day022 folder) so each number will be a line drop ( and style it using MMARKDOWN)?

30. can you leave the typos though? change the restcan you leave the typos though? change the rest

31. do yyou know how to create a requirements.txt for the dependencies declaration? i think in this file the only thing is the pillow library...

32. can you add a little guide (explain what line you need to run) in th README.md file ?

33. thanks!, now for the gui file, in the month typing field, can you enable the use of months without a capital leetter too? (make both August and august valid inputs for example)

---

## Reflection
Maybe I could've done it in less prompts but I feel as if the AI understands me better when I tell it what I want in stages.
I decided to keep tthe typos cause the AI understood me with all my typos! ( I love that tool!)
