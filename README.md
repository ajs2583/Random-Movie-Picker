# Random Movie Picker

## Description
This Python script fetches a list of top movies from a historical snapshot of the Empire Online website and selects a random movie from the list. It uses web scraping with BeautifulSoup to extract movie titles from the archived webpage. The script ensures error handling in case of request failures and changes in the website's structure.

## Features
- Scrapes movie titles from an archived Empire Online webpage
- Selects a random movie from the extracted list
- Implements error handling for network requests and webpage changes
- Uses Tkinter for a simple graphical interface (future implementation)

## Requirements
Ensure you have the necessary dependencies installed before running the script. Install them using:

```bash
pip install -r requirements.txt
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ajs2583/random-movie-picker.git
   cd random-movie-picker
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script using Python:

```bash
python movie_tracker.py
```

The script will output a randomly selected movie title from the fetched list.

## File Structure
```
random-movie-picker/
│-- movie_picker.py          # Main script
│-- requirements.txt   # Dependencies list
│-- README.md          # Documentation
```

## Future Enhancements
- Implement a Tkinter GUI to display random movies interactively.
- Add an option to filter movies by genre (if available).
- Store movies in a local file for offline access.

## Notes
- The script relies on an archived webpage. If the structure of the page changes or becomes unavailable, the script may need modifications.
- If no movies are found, a warning message will be displayed.
- A `requirements.txt` file is included to simplify dependency installation.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.


