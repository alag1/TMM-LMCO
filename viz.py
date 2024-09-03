import matplotlib.pyplot as plt
import matplotlib.patches as patches
import tkinter as tk
from tkinter import scrolledtext

# Function to plot the map with robots
def plot_map():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title('GTA-like Map with Robots')
    
    # Define robot positions (start and end points)
    robots = {
        'Robot1': {'start': (1, 9), 'end': (8, 2)},
        'Robot2': {'start': (2, 8), 'end': (7, 3)},
        'Robot3': {'start': (3, 7), 'end': (6, 4)}
    }
    
    # Plot robots
    for robot, pos in robots.items():
        for key, point in pos.items():
            ax.plot(point[0], point[1], 'ro')  # Robot as red dot
            ax.text(point[0], point[1], f'{robot} ({key})', fontsize=12, ha='right')
    
    # Draw the start and end points with lines
    for robot, pos in robots.items():
        start = pos['start']
        end = pos['end']
        ax.add_patch(patches.FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=15, color='blue'))
    
    plt.grid(True)
    plt.show()

# Function to update chat box with messages
def update_chat(message):
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, message + '\n')
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

# Function to handle command input
def handle_command(event):
    command = command_entry.get()
    command_entry.delete(0, tk.END)
    update_chat(f"Player: {command}")
    # Process command here (this is just a placeholder response)
    response = "Commander: Command received!"
    update_chat(response)

# Create main window
root = tk.Tk()
root.title("GTA-like Map with Robots and Chat Box")

# Create a frame for the chat box
chat_frame = tk.Frame(root)
chat_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a scrolled text widget for the chat box
chat_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20, state=tk.DISABLED)
chat_box.pack()

# Create an entry widget for command input
command_entry = tk.Entry(root, width=50)
command_entry.pack(side=tk.LEFT, padx=10, pady=10)
command_entry.bind('<Return>', handle_command)

# Plot the map in a separate window
plot_map()

# Start the main loop
root.mainloop()
