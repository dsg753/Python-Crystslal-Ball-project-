# Crystal Ball Oracle

Welcome to the **Crystal Ball Oracle**! This mystical application allows you to ask questions and receive answers from the oracle, just like a Magic 8-Ball. Using Python's `tkinter` for the GUI and `PIL` for image handling, this fun and interactive application provides users with a simple yet enchanting experience.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Mystical Interface**: A simple yet visually appealing user interface with a crystal ball image to enhance the mystical experience.
- **Randomized Responses**: The application provides one of 15 possible answers to your questions, simulating the classic Magic 8-Ball experience.
- **Custom Message Box**: The answer is presented in a custom-styled message box to keep the mystical theme consistent.
- **Easy to Use**: Intuitive controls with buttons to ask the oracle or leave the application.

## Installation

**Install Required Libraries**:
    Ensure you have Python installed. You also need `tkinter` and `PIL` (Pillow) for the GUI and image handling:
    ```sh
    pip install Pillow
    ```

 **Run the Application**:
    ```sh
    python crystal_ball.py

 ## Usage

1. **Start the Application**:
   - Run `crystal_ball.py`.
   - A window will appear with a crystal ball image and two buttons: "Ask the Oracle" and "Leave the Realm."

2. **Ask a Question**:
   - Click on "Ask the Oracle" and think of a question.
   - The oracle will provide a randomized answer in a styled message box.

3. **Exit the Application**:
   - Click on "Leave the Realm" to close the application.

## Code Explanation

The project is built using Python's `tkinter` for creating the GUI and `PIL` (Pillow) for handling images. Below is an overview of the main components:

- **Answers**: A list of possible responses from the oracle.
- **`ask_question` Function**: Selects a random answer from the list and displays it in a custom-styled message box.
- **Main Window**: The main application window is styled with a mystical theme, featuring a crystal ball image and buttons with thematic colors and fonts.
- **Buttons**:
  - **Ask the Oracle**: Triggers the `ask_question` function to display an answer.
  - **Leave the Realm**: Exits the application.
  
### Custom Message Box
A `tk.Toplevel` window is used to create a custom message box, styled to match the mystical theme. The answer is displayed with a custom font and color, and the user can close this window by clicking an "OK" button.

### Image Handling
The crystal ball image is loaded using `PIL` (Pillow), resized to fit the window, and displayed at the top of the main window.

## Known Issues

- **Image Path**: The path to the crystal ball image is hardcoded. If the image is not found, the application will raise an error. This path should be updated or handled more flexibly in future versions.
- **Window Resizing**: The window is not dynamically resizable, which could cause layout issues on smaller or larger screens.
- **Limited Answers**: The application currently offers only 15 possible answers. Adding more could increase the variety and fun.

## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to fork the repository and submit a pull request. You can also open an issue to discuss potential changes.

## License

This project is licensed under the MIT License.