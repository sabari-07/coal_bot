# Coal Mine Chatbot

A Python-based chatbot application designed to provide information about coal mine safety, acts, environment, rules, and policies. The chatbot uses a graphical user interface (GUI) built with `tkinter` and allows users to interactively explore various sections and subsections related to coal mines.

## Features

- Interactive Chat Interface: Users can interact with the chatbot through a user-friendly GUI.
- Section and Subsection Navigation: Users can select sections (e.g., Safety, Acts) and subsections to view detailed descriptions.
- Case-Insensitive Input: The chatbot accepts user input in any case (uppercase or lowercase).
- Sequential Numbering: Sections and subsections are displayed in a numbered list for easy navigation.
- Dynamic Recommendations: After viewing a subsection, users can click "Know More" to reset and explore other sections.
- Responsive Design: The chatbot window is responsive and adapts to the screen size.



## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  - `pandas`
  - `Pillow`
  - `tkinter` (usually comes pre-installed with Python)

You can install the required libraries using `pip`:

```bash
pip install pandas Pillow
```

## Project Structure

```
coal-mine-chatbot/
├── main.py                # Main Python script for the chatbot
├── Safety.csv             # CSV file for Safety section
├── Acts.csv               # CSV file for Acts section
├── Environment.csv        # CSV file for Environment section
├── Rules.csv              # CSV file for Rules section
├── Policies.csv           # CSV file for Policies section
├── background.jpg         # Background image for the chatbot
├── chatbot_icon.png       # Chatbot icon
├── README.md              # Project documentation
└── screenshots/           # Folder for screenshots
```

## Demo Video for Chatbot
URL : https://youtu.be/LycXeydK0vM

## How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/sabari-07/coal_bot.git
   cd coal_bot
   ```

2. Run the `main.py` script:

   ```bash
   python main.py
   ```

3. The chatbot window will open. Click the chatbot icon to start interacting.

## Usage

1. Type `Hi` to start the conversation.
2. The chatbot will display a list of sections. Type the number corresponding to the section you're interested in.
3. The chatbot will display subsections for the selected section. Type the number of the subsection to view its description.
4. After viewing a subsection, click the "Know More" button to reset and explore other sections.

## Customization

- CSV Files: You can modify the `.csv` files (`Safety.csv`, `Acts.csv`, etc.) to add or update questions and responses.
- Images: Replace `background.jpg` and `chatbot_icon.png` with your own images to customize the chatbot's appearance.
- Sections: Add or remove sections by updating the `file_map` dictionary in the `main.py` script.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

## Contact

For any questions or feedback, feel free to reach out:

- Sabareesan R 
- Email : sabarisabari5845@gmail.com  
- GitHub:(https://github.com/sabari-07)  

