#!/usr/bin/env python3
REGION = True  # I AM ONLY HERE TO SHOW AND HIDE CODE
debug = False

version = "V1.0.0"
last_change = "2024-03-22-2320"

import tkinter as tk
from PIL import Image, ImageTk

# ------------------------------------------------------------------------------------------
# MAIN APP
# ------------------------------------------------------------------------------------------
class MainApplication(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title(version)
        self.resizable(0, 0)
        self.current_frame = None
        # Create timer label
        self.timer_label = tk.Label(self, borderwidth=4, relief="groove", bg="#2222FF", fg="#FFFFFF", text="60", font=("Federation", 24))
        self.timer_label.place(x=380, y=180)
        # Start the timer
        self.remaining_time = 105
        self.update_timer()
        self.switch_frame(PAGE_00)
        # Remove maximize, minimize, and close buttons
        self.overrideredirect(True)
        # Set window state to maximize
        self.state("zoomed")
        self.allow_close = False

    def on_closing(self):
        if self.allow_close:
            self.destroy()

    def update_timer(self):
        if self.remaining_time > 0:
            # Use str.zfill() to pad the time with leading zeros
            formatted_time = str(self.remaining_time).zfill(3)
            self.timer_label.config(text=formatted_time)
            self.remaining_time -= 1
            self.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="00")
            self.switch_frame(PAGE_06)

    def switch_frame(self, frame_class):
        frame_mapping = {
            0: PAGE_00,
            1: PAGE_01,
            2: PAGE_02,
            3: PAGE_03,
            4: PAGE_04,
            5: PAGE_05,
            6: PAGE_06
        }
        new_frame = frame_mapping.get(frame_class, frame_class)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame(self, self.timer_label)
        self.current_frame.place(x=0, y=0, width=1920, height=1080)

# Base class for pages
class BasePage(tk.Frame):
    background_image = None  # Global variable to store the image reference

    def __init__(self, master, timer_label, page_name):
        tk.Frame.__init__(self, master)
        # Store the image reference as an instance attribute
        self.background_image = None
        
        # Add timer label
        self.timer_label = timer_label

        # Add buttons at the bottom
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X)

        if isinstance(self, PAGE_00):
            self.show_background(page_name)
            self.timer_label.place(x=380, y=180)
        else:
            self.show_black_background()
            self.timer_label.configure(bg="#000000")
            self.timer_label.place(x=1800, y=20)
        
        self.timer_label.lift()  # Bring the timer label to the front
        for page_num, page_class in enumerate([PAGE_00, PAGE_01, PAGE_02, PAGE_03, PAGE_04, PAGE_05, PAGE_06]):
            button = tk.Button(button_frame, text="Page {}".format(page_num), command=lambda pc=page_class: master.switch_frame(pc))
            button.pack(side=tk.LEFT)

    def show_background(self, page_name):
        try:
            if isinstance(self, PAGE_00):
                pil_image = Image.open('images/bg/00_INTRO.png')
                tk_image = ImageTk.PhotoImage(pil_image)

                if not BasePage.background_image:
                    # Store the image reference in the global variable to prevent garbage collection
                    BasePage.background_image = tk_image

                canvas = tk.Canvas(self, width=1920, height=1080, bd=0, highlightthickness=0)
                canvas.pack(fill='both', expand=True)

                # Draw the background image on the canvas
                canvas.create_image(0, 0, anchor=tk.NW, image=BasePage.background_image)
            else:
                self.show_black_background()
        except Exception as e:
            print(f"Error: Could not load background image. {e}")

    def show_black_background(self):
        canvas = tk.Canvas(self, bg="#000000", bd=0, highlightthickness=0)
        canvas.pack(fill='both', expand=True)

class PAGE_00(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_00")

        # Create the text label with specified properties
        text_label = tk.Label(self, text="OPERATION TROJAN HORSE", font=("Federation", 28, "bold"), bg="#22548E", fg="#94B5F2", height=2, bd=1, relief=tk.SOLID, anchor="w", padx=20)
        text_label.place(x=20, y=100, width=1900, height=50)  # Adjusted x position

        # Create the rainbow color gradient rectangle
        rainbow_canvas = tk.Canvas(self, bd=0, highlightthickness=0)
        rainbow_canvas.place(x=20, y=1000, width=1880, height=40)

        # Draw the rainbow color gradient
        self.draw_rainbow_gradient(rainbow_canvas)

        # Draw horizontal lines
        horizontal_line1 = tk.Canvas(self, bd=0, highlightthickness=0, bg="white")
        horizontal_line1.create_line(0, 0, 0, 0, width=2)
        horizontal_line1.place(x=500, y=200, width=1320, height=2)
        horizontal_line2 = tk.Canvas(self, bd=0, highlightthickness=0, bg="white")
        horizontal_line2.create_line(0, 0, 0, 0, width=2)
        horizontal_line2.place(x=500, y=950, width=1320, height=2)

        # Draw vertical lines
        vertical_line1 = tk.Canvas(self, bd=0, highlightthickness=0, bg="white")
        vertical_line1.create_line(0, 0, 0, 0, width=2)
        vertical_line1.place(x=500, y=200, width=2, height=750)
        vertical_line1 = tk.Canvas(self, bd=0, highlightthickness=0, bg="white")
        vertical_line1.create_line(0, 0, 0, 0, width=2)
        vertical_line1.place(x=1820, y=200, width=2, height=750)
        
        # Schedule automatic switch to PAGE_01 after 10 seconds
        self.after(10000, self.auto_switch_to_page_01)

    def draw_rainbow_gradient(self, canvas):
        num_steps = 1920  # Number of color steps in the rainbow
        step_size = 1920 / num_steps

        colors = [(128, 0, 128), (0, 0, 255), (0, 255, 255), (0, 255, 0), (255, 255, 0)]  # RGB values for purple, blue, turquoise, green, yellow

        for i in range(num_steps):
            fraction = i / (num_steps - 1)  # Adjusted to ensure the last step is yellow

            # Determine the range for color transitions
            color_range = len(colors) - 1
            sub_fraction = fraction * color_range
            color_index = int(sub_fraction)
            remainder = sub_fraction - color_index

            # Ensure indices stay within the bounds of the list
            if color_index < 0:
                color_index = 0
            elif color_index >= color_range:
                color_index = color_range - 1

            # Add a bit more yellow to the color transition
            remainder *= 1.2

            # Limit remainder to prevent unexpected behavior
            remainder = min(remainder, 1.0)

            # Interpolate between colors
            r = int((1 - remainder) * colors[color_index][0] + remainder * colors[color_index + 1][0])
            g = int((1 - remainder) * colors[color_index][1] + remainder * colors[color_index + 1][1])
            b = int((1 - remainder) * colors[color_index][2] + remainder * colors[color_index + 1][2])

            # Calculate the coordinates of the current rectangle
            x1 = i
            x2 = i + 1
            y1, y2 = 0, 40

            # Draw the rectangle with the current color
            current_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
            canvas.create_rectangle(x1, y1, x2, y2, fill=current_color, outline="")

    def auto_switch_to_page_01(self):
        # Switch to PAGE_01 after 10 seconds
        self.master.switch_frame(PAGE_01)
class PAGE_01(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_01")
        btnx = 500
        btnw = 400
        btnh = 40

        # Create buttons
        system_disarm_btn = tk.Button(self, text="SYSTEM DISARM", command=self.system_disarm)
        system_disarm_btn.place(x=btnx, y=350, width=btnw, height=btnh)

        system_arm_btn = tk.Button(self, text="SYSTEM ARM", command=self.confirm_system_arm)
        system_arm_btn.place(x=btnx, y=400, width=btnw, height=btnh)

        system_override_btn = tk.Button(self, text="SYSTEM OVERRIDE", command=self.switch_to_page_02)
        system_override_btn.place(x=btnx, y=450, width=btnw, height=btnh)

        system_disable_btn = tk.Button(self, text="SYSTEM DISABLE", command=lambda: None)
        system_disable_btn.place(x=btnx, y=500, width=btnw, height=btnh)

        file_preview_btn = tk.Button(self, text="FILE PREVIEW", command=lambda: None)
        file_preview_btn.place(x=btnx, y=550, width=btnw, height=btnh)

    def switch_to_page_02(self):
        # Switch to PAGE_03 when "SYSTEM OVERRIDE" button is clicked
        self.master.switch_frame(PAGE_02)
        
    def system_disarm(self):
        # Additional logic for SYSTEM DISARM button
        print("SYSTEM DISARM button clicked")
        # Close the application
        self.master.destroy()

    def confirm_system_arm(self):
        # Create a custom dialog
        dialog = tk.Toplevel(self)
        dialog.title("Confirmation")

        # Message label
        message_label = tk.Label(dialog, text="Are you sure?")
        message_label.pack(padx=20, pady=10)

        # Yes button
        yes_button = tk.Button(dialog, text="Yes", command=lambda: self.confirm_and_switch(dialog))
        yes_button.pack(side=tk.LEFT, padx=10)

        # No button
        no_button = tk.Button(dialog, text="No", command=dialog.destroy)
        no_button.pack(side=tk.LEFT, padx=10)

        # Calculate the center coordinates of the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - dialog.winfo_reqwidth()) // 2
        y_position = (screen_height - dialog.winfo_reqheight()) // 2

        # Set the dialog to be a transient window (attached to the parent)
        dialog.transient(self)

        # Set the dialog to be a modal window (waits for the user's response)
        dialog.grab_set()

        # Position the dialog in the center of the screen
        dialog.geometry("+{}+{}".format(x_position, y_position))

        # Wait for the user's response before continuing
        self.wait_window(dialog)

    def confirm_and_switch(self, dialog):
        # Close the dialog and switch to PAGE_06
        dialog.destroy()
        self.master.switch_frame(PAGE_06)
class PAGE_02(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_02")
        # Additional drawing or logic for PAGE_02  
class PAGE_03(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_03")
        # Additional drawing or logic for PAGE_03
class PAGE_04(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_04")
        # Additional drawing or logic for PAGE_04
class PAGE_05(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_05")
        # Additional drawing or logic for PAGE_05
class PAGE_06(BasePage):
    def __init__(self, master, timer_label):
        BasePage.__init__(self, master, timer_label, "PAGE_06")

        # Stop the main timer
        master.after_cancel(master.update_timer)

        # Run the DELETING function
        self.DELETING()

        # Start a new timer with 5 seconds
        self.new_timer_label = tk.Label(self, text="New Timer: 5", font=("Helvetica", 18))
        self.new_timer_label.place(x=1500, y=70)
        self.remaining_new_timer = 5
        self.update_new_timer()

    def DELETING(self):
        # Perform any desired actions in the DELETING function
        print("DELETING")

    def update_new_timer(self):
        if self.remaining_new_timer > 0:
            self.new_timer_label.config(text="New Timer: {}".format(self.remaining_new_timer))
            self.remaining_new_timer -= 1
            self.after(1000, self.update_new_timer)
        else:
            # After 5 seconds, close the program
            self.master.destroy()

if __name__ == "__main__":
    app = MainApplication()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)  # Bind the closing event
    app.mainloop()
