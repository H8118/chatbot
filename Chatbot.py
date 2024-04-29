import tkinter as tk
import re


responses = {
    "hello": ["Hi there! Welcome to chatbot for Chandigarh University.\nAsk me about:\nCourses\nCampus Life\nAdmissions\nFaculty\nPlacements\nAcademics", None],
    "hi": ["Hi there! Welcome to chatbot for Chandigarh University.\nAsk me about:\nCourses\nCampus Life\nAdmissions\nFaculty\nPlacements\nAcademics", None],
    "courses": ["We offer a wide range of courses! Here click on below link to check courses:", "https://www.cuchd.in/admissions/course-fee.php"],
    "campus": ["Our beautiful campus provides a vibrant learning environment. Click on below link to see campus life at Chandigarh University", "https://www.cuchd.in/campus-life/"],
    "admissions": ["Our admissions process is streamlined! Click on below link for admission process", "https://www.cuchd.in/admissions/"],
    "help": ["I'm happy to assist! What can I help you with today?", None],
    "goodbye": ["Thank you for using the chatbot! Have a great day.", None],
    "faculty": ["Our faculty members are highly experienced","https://www.cuchd.in/uie/computer-science-and-engg/faculty-list.php"],
    "placements":["Placements are great at Chandigarh University!! Have a look here","https://www.cuchd.in/placements/"],
    "academics":["Chandigarh University's academic focus isn't just about learning; it's about empowerment. From embracing diversity and emerging technologies to offering interdisciplinary insights and blending expertise with practicality.","https://www.cuchd.in/academics/"],
}


def get_response(user_input):

    user_input = user_input.lower()  # Make input case-insensitive

    for keyword, (response, url) in responses.items():
        if re.search(r'\b{}\b'.format(keyword), user_input):
            return response, url
    
    return "I'm still under development, but I'm learning! Can you rephrase your question?", None

def send_message(event=None):
    """Sends the user's message to the chatbot and displays the response.

    Args:
        event (tk.Event, optional): The event that triggered the function (button click). Defaults to None.
    """

    user_input = entry.get()
    entry.delete(0, tk.END)  # Clear the entry field after sending

    chat_window.insert(tk.END, "You: " + user_input + "\n")

    bot_response, url = get_response(user_input)
    chat_window.insert(tk.END, "UniBot: " + bot_response + "\n")

    if url:
        chat_window.insert(tk.END, "UniBot: " + url + "\n", "hyperlink")
        chat_window.tag_config("hyperlink", foreground="blue", underline=1)
        chat_window.tag_bind("hyperlink", "<Button-1>", lambda event: open_url(url))

    chat_window.see(tk.END)  # Scroll to the bottom of the chat window

def open_url(url):
    """Opens the provided URL in a web browser.

    Args:
        url (str): The URL to open.
    """
    import webbrowser
    webbrowser.open(url)

# Create the main window
window = tk.Tk()
window.title("UniBot - Your University Chatbot")

# Create the chat window (text area)
chat_window = tk.Text(window, width=75, height=10)
chat_window.pack(side=tk.LEFT, fill=tk.Y, expand=True)

# Create the scrollbar
scrollbar = tk.Scrollbar(window, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.config(yscrollcommand=scrollbar.set)

# Create the input field
entry = tk.Entry(window, width=40)
entry.bind("<Return>", send_message)  # Send message on Enter key press
entry.pack(side=tk.LEFT, padx=98, pady=98)

# Create the send button (optional)
send_button = tk.Button(window, text="Send", command=send_message)
# send_button.pack(side=tk.BOTTOM, fill=tk.X)  # Uncomment to add a button

# Start the main event loop
window.mainloop()
