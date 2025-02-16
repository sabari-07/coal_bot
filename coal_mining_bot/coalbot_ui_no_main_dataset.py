import tkinter as tk
from tkinter import ttk, messagebox, font
import pandas as pd
from PIL import Image, ImageTk

class CoalMineChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Coal Mine Chatbot")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # Full screen

        # Load background image
        self.background_image = Image.open("D:\OneDrive\Desktop\coalbot2\coal_mine.jpeg")  # Replace with your background image
        self.background_image = self.background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas for the background
        self.canvas = tk.Canvas(self.root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Add greeting text in the center
        self.canvas.create_text(
            root.winfo_screenwidth() // 2,
            root.winfo_screenheight() // 2,
            text="Welcome to Coal Mine Chatbot",
            font=("Helvetica", 40, "bold"),
            fill="red"
        )

        # Load chatbot icon
        self.chatbot_icon = Image.open("D:\OneDrive\Desktop\coalbot2\chatbot_logo.png")  # Replace with your chatbot icon
        self.chatbot_icon = self.chatbot_icon.resize((50, 50), Image.ANTIALIAS)
        self.chatbot_icon_photo = ImageTk.PhotoImage(self.chatbot_icon)

        # Add chatbot icon to the bottom-right corner
        self.chatbot_button = tk.Button(self.root, image=self.chatbot_icon_photo, command=self.open_chatbot, borderwidth=0)
        self.chatbot_button_window = self.canvas.create_window(
            root.winfo_screenwidth() - 60,  # 60 pixels from the right
            root.winfo_screenheight() - 60,  # 60 pixels from the bottom
            anchor="se", window=self.chatbot_button
        )

        # File map for different sections
        self.file_map = {
            'Safety': 'Safety.csv',
            'Acts': 'Acts.csv',
            'Environment': 'Environment.csv',
            'Rules': 'Rules.csv',
            'Policies': 'Policies.csv'
        }

        # Initialize chatbot window
        self.chatbot_window = None
        self.current_section_df = None  # To store the current section's DataFrame

    def open_chatbot(self):
        # Create a floating chatbot window
        if self.chatbot_window is None or not self.chatbot_window.winfo_exists():
            self.chatbot_window = tk.Toplevel(self.root)
            self.chatbot_window.title("CoalBot")
            self.chatbot_window.geometry("400x500+{0}+{1}".format(
                self.root.winfo_screenwidth() - 460,  # 460 pixels from the right
                self.root.winfo_screenheight() - 560  # 560 pixels from the bottom
            ))
            self.chatbot_window.resizable(False, False)

            # Chat display area
            self.chat_display = tk.Text(
                self.chatbot_window, height=20, width=45, wrap=tk.WORD, state=tk.DISABLED,
                bg="#f0f0f0", fg="#333333", font=("Verdana", 12)
            )
            self.chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

            # Configure tags for bot and user messages
            self.chat_display.tag_configure("bot", foreground="#004080", font=("Verdana", 12, "bold"), justify="left")
            self.chat_display.tag_configure("user", foreground="#006600", font=("Verdana", 12, "italic"), justify="right")

            # User input area
            self.user_input = tk.Entry(
                self.chatbot_window, width=40, font=("Verdana", 12), bg="#ffffff", fg="#333333"
            )
            self.user_input.pack(pady=10, padx=10, fill=tk.X)
            self.user_input.bind("<Return>", lambda event: self.process_user_input())  # Bind Enter key

            # Greet the user
            self.display_bot_message("Hello! Welcome to CoalBot. How can I assist you today?")
            #self.display_bot_message("Please type 'Hi' to continue.")

    def display_bot_message(self, message):
        # Display a message from the bot in the chat display area (left-aligned)
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{message}\n\n", "bot")  # Use "bot" tag for styling
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)  # Auto-scroll to the bottom

    def display_user_message(self, message):
        # Display a message from the user in the chat display area (right-aligned)
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{message}\n\n", "user")  # Use "user" tag for styling
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.yview(tk.END)  # Auto-scroll to the bottom

    def process_user_input(self):
        # Get user input
        user_text = self.user_input.get().strip().lower()  # Convert input to lowercase
        self.user_input.delete(0, tk.END)  # Clear the input field

        # Display the user's message in the chat
        self.display_user_message(f"You: {user_text}")

        if user_text == "hi":
            self.display_bot_message("Here are the available sections:")
            self.display_sections()
            self.display_bot_message("Please type the number of the section you're interested in.")
        elif user_text.isdigit():
            if self.current_section_df is None:
                self.handle_section_by_number(user_text)
            else:
                self.handle_subsection_by_number(user_text)
        else:
            # Check if the input matches a subsection
            found = False
            for section, file in self.file_map.items():
                df = pd.read_csv(file)
                df['Questions'] = df['Questions'].str.lower()  # Convert questions to lowercase for case-insensitive comparison
                if user_text in df['Questions'].values:
                    self.display_subsection_description(df, user_text)
                    found = True
                    break
            if not found:
                self.display_bot_message("Sorry, I couldn't find that in the dataset. Please contact 9473626270 for further assistance.")

    def display_sections(self):
        # Display sections with numbers in a single message
        sections = list(self.file_map.keys())
        sections_message = "Here are the available sections:\n"
        for i, section in enumerate(sections, start=1):
            sections_message += f"{i}. {section}\n"
        self.display_bot_message(sections_message)

    def handle_section_by_number(self, section_number):
        # Handle section selection by number
        sections = list(self.file_map.keys())
        try:
            section_number = int(section_number)
            if 1 <= section_number <= len(sections):
                section_name = sections[section_number - 1]
                self.handle_section(section_name)
            else:
                self.display_bot_message("Invalid section number. Please try again.")
        except ValueError:
            self.display_bot_message("Please enter a valid number.")

    def handle_section(self, section_name):
        # Load the corresponding CSV file
        try:
            self.current_section_df = pd.read_csv(self.file_map[section_name])
            self.current_section_df['Questions'] = self.current_section_df['Questions'].str.lower()  # Convert questions to lowercase
            self.display_bot_message(f"Here are the subsections in '{section_name}':")
            self.display_subsections(self.current_section_df)
            self.display_bot_message("Please type the number of the subsection you want to know about.")
        except FileNotFoundError:
            self.display_bot_message(f"Sorry, the file for section '{section_name}' was not found.")

    def display_subsections(self, df):
        # Display subsections with numbers in a single message
        subsections = df['Questions'].values
        subsections_message = "Here are the subsections:\n"
        for i, subsection in enumerate(subsections, start=1):
            subsections_message += f"{i}. {subsection}\n"
        self.display_bot_message(subsections_message)

    def handle_subsection_by_number(self, subsection_number):
        # Handle subsection selection by number
        if self.current_section_df is None:
            self.display_bot_message("No section selected. Please type 'Hi' to start again.")
            return

        try:
            subsection_number = int(subsection_number)
            subsections = self.current_section_df['Questions'].values
            if 1 <= subsection_number <= len(subsections):
                subsection_name = subsections[subsection_number - 1]
                self.display_subsection_description(self.current_section_df, subsection_name)
            else:
                self.display_bot_message("Invalid subsection number. Please try again.")
        except ValueError:
            self.display_bot_message("Please enter a valid number.")

    def display_subsection_description(self, df, subsection):
        # Display the description of the selected subsection
        matching_rows = df[df['Questions'] == subsection]
        if not matching_rows.empty:
            response = matching_rows['Response'].values[0]
            self.display_bot_message(f"Description for '{subsection}':")
            self.display_bot_message(response)

            # Add "Know More" button
            self.know_more_button = tk.Button(
                self.chatbot_window, text="Know More", command=self.reset_and_show_sections,
                bg="#004080", fg="white", font=("Verdana", 12, "bold")
            )
            self.know_more_button.pack(pady=10)
        else:
            self.display_bot_message(f"Sorry, no description found for '{subsection}'.")

    def reset_and_show_sections(self):
        # Remove the "Know More" button
        self.know_more_button.destroy()

        # Reset the current section DataFrame
        self.current_section_df = None

        # Show sections again
        self.display_bot_message("Here are the available sections:")
        self.display_sections()
        self.display_bot_message("Please type the number of the section you're interested in.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = CoalMineChatbot(root)
    root.mainloop()