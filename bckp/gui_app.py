#!/usr/bin/env python3

import tkinter as tk
import subprocess

class ScriptRunnerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Script Runner")

        self.display_var = tk.StringVar()
        self.display_var.set("Click 'Automate' to run the script")

        self.create_widgets()

    def create_widgets(self):
        # Display label
        self.display_label = tk.Label(self.root, textvariable=self.display_var, padx=10, pady=10)
        self.display_label.pack()

        # Automate button
        self.automate_button = tk.Button(self.root, text="Automate", command=self.run_script)
        self.automate_button.pack()

    def run_script(self):
        try:
            # Run the script using subprocess
            subprocess.run(["sudo","python3", "automation.py"])

            # Update the display message
            self.display_var.set("Script is running...")
        except Exception as e:
            # Display an error message if the script fails to run
            self.display_var.set(f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScriptRunnerApp(root)
    root.mainloop()
