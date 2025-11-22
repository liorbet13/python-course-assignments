# Day 04

## AI Model Used
I used **Copilot AI model "claude sonnet 4.5"**

## Part 1: Removing __pycache__

### My Prompts

1. can you remove the pycache from git and make sure it wont keep making them in the future? 
[copilot finished with "now you can commit those changes"]

2. commit them please

3. can you create a new folder called "day04" with a readme file? 

4. can you add a section (after ai model used) with the title " part 1 removing _pycache_" and a sub- title my promptscan you add a section (after ai model used) with the title " part 1 removing _pycache_" and a sub- title my prompts
[i edit the content manually]

## Part 2: WNBA Team Roster Viewer

### Overview
A GUI application that fetches and displays WNBA team rosters from official team websites. Users can select from 15 WNBA teams (including 2026 expansion teams), fetch roster data from the web, and view detailed player information with photos and statistics.

### How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python roster_gui.py
   ```

3. Use the GUI:
   - Select a team from the dropdown menu
   - Click "Fetch Roster from Web" to download latest roster data (takes ~15-30 seconds per team)
   - Click "Load Saved Roster" to display previously fetched data
   - Scroll through player roster with mouse wheel
   - Click "Clear Display" to reset the view

### Features
- **Team Selection**: Choose from 15 WNBA teams including Portland Fire and Toronto Tempo (2026 expansion)
- **Web Scraping**: Fetches roster data directly from official team pages ([team].wnba.com/roster/)
- **Player Photos**: Displays 60x60px player headshots loaded asynchronously
- **Comprehensive Stats**: Shows PPG, RPG, APG, height, college, and years of experience
- **Local Storage**: Saves roster data as JSON files in `team_rosters/` directory
- **WNBA Branding**: Styled with official WNBA colors (black #000000, orange #FE5000)
- **Scrollable Display**: Canvas-based custom layout with mouse wheel support

### Files
- `roster_gui.py` - Main GUI application (user interface)
- `roster_fetcher.py` - Business logic module (web scraping and data management)
- `requirements.txt` - Python package dependencies (requests, beautifulsoup4, Pillow)
- `team_rosters/` - Directory containing saved roster JSON files
- `trying_stuff/` - Previous WNBA boxscore viewer attempts (deprecated)

### Technical Details
- **Data Source**: Official WNBA team roster pages (https://[team].wnba.com/roster/)
- **Scraping Strategy**: 
  - Roster page: player name, number, position, PPG, RPG, APG
  - Individual player pages: height, college, years of experience
- **GUI Framework**: tkinter with Canvas for custom scrollable display
- **HTML Parsing**: BeautifulSoup4 for extracting player data from structured HTML (dl/dt/dd elements)
- **Image Handling**: PIL (Pillow) for loading and resizing player headshots from CDN
- **Colors**: WNBA Black (#000000), WNBA Orange (#FE5000), Dark Gray (#1A1A1A)
- **Image CDN**: cdn.wnba.com/headshots/wnba/latest/260x190/[player_id].png

### Teams Included
**Current Teams (13):**
- Atlanta Dream
- Chicago Sky
- Connecticut Sun
- Dallas Wings
- Golden State Valkyries
- Indiana Fever
- Las Vegas Aces
- Los Angeles Sparks
- Minnesota Lynx
- New York Liberty
- Phoenix Mercury
- Seattle Storm
- Washington Mystics

**Expansion Teams (2):**
- Portland Fire (joining 2026)
- Toronto Tempo (joining 2026)

### Player Information Displayed
- Player Photo (60x60px headshot)
- Jersey Number
- Full Name
- Position
- Height (e.g., "5-8", "6-0")
- Points Per Game (PPG) - displayed in blue
- Rebounds Per Game (RPG) - displayed in blue
- Assists Per Game (APG) - displayed in blue
- Years of Experience
- College/University

### Notes
- Fetching rosters requires visiting each player's individual page (~16 requests per team)
- Expansion teams (Portland Fire, Toronto Tempo) show placeholder data until 2026
- Roster data is cached locally in JSON format for quick reloading
- Player photos load asynchronously to prevent UI freezing
- WNBA logo attempts to load but falls back to orange "WNBA" text if unavailable

### My Prompts
1. can you create a new program (with a gui) that wll be updateed based on recent ddata from th wnba website and will allow to vie data on recenet games (boxscore) 
teh website link https://www.wnba.com/https://www.wnba.com/

2. thanks! note on the redme file - can you have the part 2 prompts at the end  (after the notes, and copy my prompts exactly?

3. also add all the prompts i give you to this sectioon until ill tell you to stop

4. can you seperate the buisness logic and the ui to seperate files?/

5. now lets get into details, i want to let the user choose frrom multiple options:
    1. viewing recent games data (fromm lets say a weeks period)
    2. viewing a spesific team recent gamees (by choosing the team)
    3. viewing a specific players recent stats by choosing the team and selecting the spesific player from tthe roster.
essentially i want the app to get the team names and rosters so the user will choose from them

6. the data doesnt match, can you make sure to fetch the data from the website i gave you https://www.wnba.com/schedule?season=2025&month=all
even if the most recent game was on may 2025

7. are there any limitations? i see the indiana fever roster is nott good, for example caitlyn clarke isnt there

8. do that for all 13 teams now please

9. we do have some issues here so let's start over and try to creat somehitng else. can you move all files (except the readme) from day04 to a new folder called trying_stuff, and lets start a new project in day04, ill give you the details soon

10. update the prompts in the readme file part to (starting with number 10) from now until ill tell you stop.

11. lets create a new app with a gui.
in the gui, i want a user to choose one of the 15 wnba teams (including the 2 upcoming for 2026) and then i want the gui to fetch the roster details from the wnba website - https://www.wnba.com/teams
i want the program to download the team data and save it locally in a file or multiple files. also i want a seperate file for the gui and the buisness logic.

12. i get the confirmation for the fetching, but when i press load it show no player dadtai get the confirmation for the fetching, but when i press load it show no player dadta

13. okay awesome love it. can we display it in a nicer way? instead of a text display can we have  table with all the teams players?

14. any way we can also add a photo for each player ( a small one near their name, from the same website)

15. love it!!! can we change the general apperence (color scheme mostly) to look a little more like the wnbe website? and add the wnba logo?

16. i cant see the wnba logo, do you know why?

17. doesnt work yet bbut i like the orange so thats okay! 
can we add addditional stats for the roster? like ppg or height? and maybe some other useful stats if theyre available

18. great! except the hiehgt college and experience fields are empty, is it fixable?

19. yayyyy it worked! can you epddate the read me file part 2 from the box score app to this one? (dont touch the my prompts section)

20. can you add the team_rosters (the actual fetched data) to gitignore?