import tkinter as tk
from tkinter import filedialog

def describe_mood():
    mood = mood_entry.get()
    print(f"Current mood: {mood}")

def upload_past():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    print(f"Uploaded file: {file_path}")

def ask_claude():
    import subprocess
    print("Executing script...")
    process = subprocess.Popen(["python", "function_calling.py"], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output.decode())

# Create the main window
window = tk.Tk()
window.title("My App")

# Create the mood input section
mood_label = tk.Label(window, text="Describe current mood:")
mood_label.pack()
mood_entry = tk.Entry(window)
mood_entry.pack()
mood_button = tk.Button(window, text="Submit", command=describe_mood)
mood_button.pack()

# Create the file upload section
upload_button = tk.Button(window, text="Upload past", command=upload_past)
upload_button.pack()

# Create the execute button
execute_button = tk.Button(window, text="Ask Claude", command=ask_claude)
execute_button.pack()

# Create the output text box
output_text = tk.Text(window, height=10, width=50)
output_text.pack()

# Run the main event loop
window.mainloop()