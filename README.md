# Nepal Zone Guessing Game

Welcome to the **Nepal Zone Guessing Game**, an interactive Python project that challenges you to identify and guess the zones of Nepal on a map. This project is built using the `turtle` graphics module and the `pandas` library, making it both visually engaging and educational.

## Features

- **Interactive Map**: The game uses a graphical representation of Nepal, where players can guess the zones by typing their names.
- **Progress Tracking**: The game displays the number of correct guesses made so far, helping you keep track of your progress.
- **Watermark**: A custom watermark is displayed on the screen, adding a personalized touch to the game.
- **Learning Feature**: If you choose to exit the game before identifying all the zones, a CSV file named `zones_to_learn.csv` will be generated. This file contains the zones you missed, allowing you to study and improve.

## How to Play

1. **Setup**: Make sure you have Python installed on your system along with the required libraries (`turtle`, `pandas`).
2. **Run the Game**: Execute the Python script in your preferred IDE or terminal.
3. **Guessing Zones**: A map of Nepal will be displayed. You need to guess the names of the zones by typing them into the text box that appears.
   - The game will track the number of correct guesses.
   - If you guess a correct zone, it will be marked on the map in green.
4. **Exiting the Game**: Type "Exit" when you wish to stop playing. The game will save the zones you missed into a CSV file for future learning.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `turtle`
  - `pandas`

You can install the required libraries using pip:

```bash
pip install pandas

## Files in the Project

- **nepal_zone.gif**: The image file of Nepal that will be used as the map in the game.
- **zone.csv**: A CSV file containing the names of the zones along with their respective x and y coordinates on the map.
- **zones_to_learn.csv**: This file is generated when you exit the game and contains the names of zones that you didn't guess correctly.

## Example of `zone.csv` File Structure

The `zone.csv` file should have the following structure:

| zone  |  x  |  y  |
|-------|-----|-----|
| Zone1 |  50 |  60 |
| Zone2 | 120 | 300 |
| ...   | ... | ... |

## Code Breakdown

- **Setup the Screen**: The turtle screen is set up with the map of Nepal as the background.
- **Watermark**: A watermark is added to the bottom of the screen using turtle graphics.
- **Game Loop**: The game enters a loop where it prompts the user to guess a zone until all zones are correctly identified or the user chooses to exit.
- **Zone Marking**: When a correct zone is guessed, a turtle object is used to mark the zone's name on the map at its corresponding coordinates.
- **Exit and Save**: If the player exits, a CSV file with the missed zones is created to help them learn the zones they didn't guess.

## How to Customize

- **Change the Map**: Replace `nepal_zone.gif` with another map image to create a similar guessing game for a different region.
- **Update Zones**: Modify the `zone.csv` file to include different zones or regions, along with their respective coordinates.
- **Adjust Watermark**: The watermark text and position can be customized in the code to reflect a different name or location.

## Future Enhancements

- **Add Timer**: Introduce a timer to challenge players to guess all the zones within a limited time.
- **Hints**: Provide hints for difficult zones after a few incorrect guesses.
- **Scoreboard**: Implement a high-score system to track the best performances.

## License

This project is open-source and available for personal or educational use. Feel free to modify and share it as you like.

---

Enjoy playing the Nepal Zone Guessing Game and enhance your knowledge of Nepal's geography!

