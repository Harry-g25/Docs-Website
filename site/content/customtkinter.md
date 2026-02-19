# CustomTkinter - Complete Documentation & Reference Guide

**Version:** 5.2.2 (Latest)  
**Last Updated:** February 2026  
**Official Website:** <https://customtkinter.tomschimansky.com/>

---

## Table of Contents

<details open>
<summary><strong>Table of Contents — click to expand/collapse</strong></summary>

<nav aria-label="Table of contents">
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li>
            <a href="#installation--setup">Installation &amp; Setup</a>
            <ul>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#upgrade-to-latest-version">Upgrade to Latest Version</a></li>
                <li><a href="#verify-installation">Verify Installation</a></li>
                <li><a href="#basic-import">Basic Import</a></li>
            </ul>
        </li>
        <li>
            <a href="#core-concepts">Core Concepts</a>
            <ul>
                <li><a href="#ctk-vs-tk">CTk vs Tk</a></li>
                <li><a href="#string-variables-for-dynamic-updates">String Variables for Dynamic Updates</a></li>
                <li><a href="#widget-hierarchy">Widget Hierarchy</a></li>
            </ul>
        </li>
        <li>
            <a href="#main-window--application-setup">Main Window &amp; Application Setup</a>
            <ul>
                <li><a href="#basic-window-setup">Basic Window Setup</a></li>
                <li><a href="#ctk-arguments">CTk Arguments</a></li>
                <li><a href="#complete-initialization-example">Complete Initialization Example</a></li>
                <li><a href="#ctktoplevel---secondary-windows">CTkToplevel — Secondary Windows</a></li>
            </ul>
        </li>
        <li>
            <a href="#appearance--theming">Appearance &amp; Theming</a>
            <ul>
                <li><a href="#appearance-modes">Appearance Modes</a></li>
                <li><a href="#available-themes">Available Themes</a></li>
                <li><a href="#color-system">Color System</a></li>
                <li><a href="#custom-theme-file-json">Custom Theme File (JSON)</a></li>
                <li><a href="#ctkfont---custom-fonts">CTkFont — Custom Fonts</a></li>
                <li><a href="#scaling">Scaling</a></li>
            </ul>
        </li>
        <li>
            <a href="#layout-management">Layout Management</a>
            <ul>
                <li><a href="#grid-layout-recommended">Grid Layout (Recommended)</a></li>
                <li><a href="#pack-layout">Pack Layout</a></li>
                <li><a href="#place-layout-absolute-positioning">Place Layout (Absolute Positioning)</a></li>
                <li><a href="#responsive-design-with-grid">Responsive Design with Grid</a></li>
            </ul>
        </li>
        <li>
            <a href="#widget-reference">Widget Reference</a>
            <ul>
                <li><a href="#ctkbutton">CTkButton</a></li>
                <li><a href="#ctklabel">CTkLabel</a></li>
                <li><a href="#ctkentry">CTkEntry</a></li>
                <li><a href="#ctktextbox">CTkTextbox</a></li>
                <li><a href="#ctkframe">CTkFrame</a></li>
                <li><a href="#ctkscrollableframe">CTkScrollableFrame</a></li>
                <li><a href="#ctkslider">CTkSlider</a></li>
                <li><a href="#ctkprogressbar">CTkProgressBar</a></li>
                <li><a href="#ctkcheckbox">CTkCheckBox</a></li>
                <li><a href="#ctkswitch">CTkSwitch</a></li>
                <li><a href="#ctkradiobutton">CTkRadioButton</a></li>
                <li><a href="#ctkcombobox">CTkComboBox</a></li>
                <li><a href="#ctkoptionmenu">CTkOptionMenu</a></li>
                <li><a href="#ctksegmentedbutton">CTkSegmentedButton</a></li>
                <li><a href="#ctktabview">CTkTabview</a></li>
                <li><a href="#ctkscrollbar">CTkScrollbar</a></li>
                <li><a href="#ctkimage">CTkImage</a></li>
            </ul>
        </li>
        <li>
            <a href="#event-handling--callbacks">Event Handling &amp; Callbacks</a>
            <ul>
                <li><a href="#button-commands">Button Commands</a></li>
                <li><a href="#entry-commands">Entry Commands</a></li>
                <li><a href="#slider-commands">Slider Commands</a></li>
                <li><a href="#checkbox-and-switch-commands">CheckBox and Switch Commands</a></li>
                <li><a href="#combobox-commands">ComboBox Commands</a></li>
                <li><a href="#event-binding-with-bind">Event Binding with bind()</a></li>
            </ul>
        </li>
        <li>
            <a href="#best-practices">Best Practices</a>
            <ul>
                <li><a href="#use-classes-for-complex-applications">Use Classes for Complex Applications</a></li>
                <li><a href="#responsive-layout-with-grid">Responsive Layout with Grid</a></li>
                <li><a href="#data-validation">Data Validation</a></li>
                <li><a href="#state-management">State Management</a></li>
                <li><a href="#error-handling">Error Handling</a></li>
            </ul>
        </li>
        <li>
            <a href="#common-patterns">Common Patterns</a>
            <ul>
                <li><a href="#modal-dialog">Modal Dialog</a></li>
                <li><a href="#loading-indicator">Loading Indicator</a></li>
                <li><a href="#form-validation">Form Validation</a></li>
            </ul>
        </li>
        <li>
            <a href="#custom-widget-creation">Custom Widget Creation</a>
            <ul>
                <li><a href="#creating-reusable-components">Creating Reusable Components</a></li>
                <li><a href="#how-it-works">How It Works</a></li>
            </ul>
        </li>
        <li>
            <a href="#configuration--preferences">Configuration &amp; Preferences</a>
            <ul>
                <li><a href="#saving-and-loading-settings">Saving and Loading Settings</a></li>
            </ul>
        </li>
        <li>
            <a href="#threading--long-operations">Threading &amp; Long Operations</a>
            <ul>
                <li><a href="#running-background-tasks">Running Background Tasks</a></li>
            </ul>
        </li>
        <li>
            <a href="#common-gotchas--solutions">Common Gotchas &amp; Solutions</a>
            <ul>
                <li><a href="#lambda-closure-in-loops">Lambda Closure in Loops</a></li>
                <li><a href="#image-garbage-collection">Image Garbage Collection</a></li>
                <li><a href="#theme-aware-colors">Theme-Aware Colors</a></li>
                <li><a href="#grid-layout-not-expanding">Grid Layout Not Expanding</a></li>
                <li><a href="#entry-widget-focus-issues">Entry Widget Focus Issues</a></li>
            </ul>
        </li>
        <li><a href="#summary">Summary</a></li>
    </ul>
</nav>

</details>

---

## Introduction

CustomTkinter is a modern, fully customizable Python desktop UI library built on top of Tkinter. It provides modern-looking widgets with support for light/dark modes and consistent styling across Windows, macOS, and Linux.

**Key Features:**

| Name | Description |
| --- | --- |
| Modern, customizable widgets |  |
| Light and dark mode support (system or manual) |  |
| HighDPI scaling on Windows and macOS |  |
| Consistent appearance across all platforms |  |
| Full backward compatibility with Tkinter |  |
| Lightweight with minimal dependencies |  |

---

## Installation & Setup

### Installation

Install CustomTkinter via pip:

```bash
pip install customtkinter
```

### Upgrade to Latest Version

```bash
pip install customtkinter --upgrade
```

### Verify Installation

```python
import customtkinter
print(customtkinter.__version__)
```

### Basic Import

```python
import customtkinter
```

---

## Core Concepts

### CTk vs Tk

CustomTkinter's `CTk` class replaces standard Tkinter's `Tk` class. It's a drop-in replacement:

```python
import customtkinter

# Instead of tkinter.Tk(), use:
app = customtkinter.CTk()
app.mainloop()
```

### String Variables for Dynamic Updates

Like Tkinter, CustomTkinter supports StringVar for keeping text widgets in sync:

```python
import customtkinter
from tkinter import StringVar

app = customtkinter.CTk()
app.geometry("300x150")

# Create a StringVar to hold text
text_var = StringVar(value="Initial text")

label = customtkinter.CTkLabel(app, textvariable=text_var)
label.pack(pady=10)

button = customtkinter.CTkButton(
    app, 
    text="Update Label",
    command=lambda: text_var.set("Updated text!")
)
button.pack(pady=10)

app.mainloop()
```

### Widget Hierarchy

All CustomTkinter widgets inherit from tkinter.Widget and follow standard widget hierarchy:

```
CTk (Main Window)
├── CTkFrame
│   ├── CTkLabel
│   ├── CTkButton
│   └── CTkEntry
└── CTkScrollableFrame
    ├── CTkSlider
    └── CTkCheckBox
```

---

## Main Window & Application Setup

### Basic Window Setup

```python
import customtkinter

# Create main window
app = customtkinter.CTk()

# Set window properties
app.title("My Application")
app.geometry("800x600")
app.minsize(400, 300)
app.resizable(True, True)

# Configure window appearance
app.configure(fg_color="#ffffff")

app.mainloop()
```

### CTk Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `fg_color` | str/tuple | "white"/"gray20" | Window background color (light, dark) |
| `appearance_mode` | str | "System" | "System", "Light", or "Dark" |

### Complete Initialization Example

```python
import customtkinter

class MyApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # Window configuration
        self.title("Professional App")
        self.geometry("1000x600")
        self.minsize(600, 400)
        
        # Appearance
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        
        # Configure appearance
        self.configure(fg_color="#f0f0f0")
        
        # Create widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Add your widgets here
        
    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### CTkToplevel - Secondary Windows

```python
import customtkinter

def open_new_window():
    top = customtkinter.CTkToplevel(app)
    top.title("Secondary Window")
    top.geometry("400x300")
    
    label = customtkinter.CTkLabel(
        top, 
        text="This is a secondary window"
    )
    label.pack(pady=20)

app = customtkinter.CTk()
app.geometry("500x300")

button = customtkinter.CTkButton(
    app,
    text="Open New Window",
    command=open_new_window
)
button.pack(pady=20)

app.mainloop()
```

---

## Appearance & Theming

### Appearance Modes

CustomTkinter supports three appearance modes:

```python
import customtkinter

# Set global appearance mode
customtkinter.set_appearance_mode("System")  # Modes: "System", "Light", "Dark"
customtkinter.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

app = customtkinter.CTk()
app.geometry("400x300")

def toggle_appearance():
    current = customtkinter.get_appearance_mode()
    new_mode = "Dark" if current == "Light" else "Light"
    customtkinter.set_appearance_mode(new_mode)

button = customtkinter.CTkButton(
    app,
    text="Toggle Dark/Light Mode",
    command=toggle_appearance
)
button.pack(pady=20)

app.mainloop()
```

### Available Themes

CustomTkinter comes with built-in themes:

- `"blue"` (default)
- `"dark-blue"`
- `"green"`

```python
import customtkinter

customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("400x300")
app.mainloop()
```

### Color System

Colors in CustomTkinter support multiple formats:

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Single color (used in all modes)
label1 = customtkinter.CTkLabel(app, text="Single Color", fg_color="red")
label1.pack(pady=10)

# Tuple: (light_mode_color, dark_mode_color)
label2 = customtkinter.CTkLabel(
    app, 
    text="Mode-Specific Colors",
    fg_color=("white", "gray20")
)
label2.pack(pady=10)

# Transparent (inherits from parent)
label3 = customtkinter.CTkLabel(
    app,
    text="Transparent",
    fg_color="transparent"
)
label3.pack(pady=10)

# Supported color formats:
# - Named colors: "red", "blue", "green", etc.
# - Hex colors: "#FF5733"
# - RGB (0-255): Not directly, use hex conversion
# - HSL: Not directly, use hex conversion

app.mainloop()
```

### Custom Theme File (JSON)

Create a `custom_theme.json`:

```json
{
  "CTk": {
    "fg_color": ["#ececec", "#212121"]
  },
  "CTkButton": {
    "fg_color": ["#0066cc", "#0052a3"],
    "hover_color": ["#0052a3", "#003d7a"],
    "text_color": ["white", "white"],
    "border_color": ["#cccccc", "#404040"]
  },
  "CTkEntry": {
    "fg_color": ["#f0f0f0", "#212121"],
    "border_color": ["#cccccc", "#404040"],
    "text_color": ["black", "white"]
  },
  "CTkLabel": {
    "text_color": ["black", "white"]
  }
}
```

Load custom theme:

```python
import customtkinter

customtkinter.set_default_color_theme("custom_theme.json")

app = customtkinter.CTk()
app.geometry("400x300")
app.mainloop()
```

### CTkFont - Custom Fonts

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Create custom fonts
header_font = customtkinter.CTkFont(family="Helvetica", size=24, weight="bold")
normal_font = customtkinter.CTkFont(family="Arial", size=12)
mono_font = customtkinter.CTkFont(family="Courier", size=10)

# Use fonts in widgets
label1 = customtkinter.CTkLabel(
    app,
    text="Header Text",
    font=header_font
)
label1.pack(pady=10)

label2 = customtkinter.CTkLabel(
    app,
    text="Normal Text",
    font=normal_font
)
label2.pack(pady=10)

label3 = customtkinter.CTkLabel(
    app,
    text="Monospace Text",
    font=mono_font
)
label3.pack(pady=10)

# Font properties
label4 = customtkinter.CTkLabel(
    app,
    text="Italic Text",
    font=customtkinter.CTkFont(family="Arial", size=12, slant="italic")
)
label4.pack(pady=10)

app.mainloop()
```

### Scaling

CustomTkinter supports window and widget scaling:

```python
import customtkinter

# Set global scaling (affects all new widgets)
customtkinter.set_widget_scaling(1.5)  # 150% scaling
customtkinter.set_window_scaling(1.2)  # Window scaling

app = customtkinter.CTk()
app.geometry("400x300")

label = customtkinter.CTkLabel(app, text="Scaled Text")
label.pack(pady=20)

app.mainloop()
```

---

## Layout Management

CustomTkinter supports three layout managers: `grid()`, `pack()`, and `place()`.

### Grid Layout (Recommended)

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Configure grid weights for responsive design
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)

# Header frame
header = customtkinter.CTkLabel(
    app,
    text="My Application",
    font=("Arial", 24, "bold")
)
header.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Content frame
content = customtkinter.CTkFrame(app)
content.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
content.grid_rowconfigure(0, weight=1)
content.grid_columnconfigure(0, weight=1)

# Widgets in content
label = customtkinter.CTkLabel(content, text="Content Area")
label.grid(row=0, column=0, sticky="nsew")

app.mainloop()
```

### Pack Layout

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

# Pack from top to bottom
label1 = customtkinter.CTkLabel(app, text="Top Widget")
label1.pack(side="top", fill="x", padx=10, pady=10)

label2 = customtkinter.CTkLabel(app, text="Middle Widget")
label2.pack(side="top", fill="x", padx=10, pady=10)

label3 = customtkinter.CTkLabel(app, text="Bottom Widget")
label3.pack(side="bottom", fill="x", padx=10, pady=10)

app.mainloop()
```

### Place Layout (Absolute Positioning)

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

# Absolute positioning
button1 = customtkinter.CTkButton(app, text="Button 1")
button1.place(x=50, y=50, width=100, height=50)

button2 = customtkinter.CTkButton(app, text="Button 2")
button2.place(relx=0.5, rely=0.5, anchor="center", width=100, height=50)

app.mainloop()
```

### Responsive Design with Grid

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("800x600")

# Configure responsive grid
for i in range(3):
    app.grid_rowconfigure(i, weight=1)
    app.grid_columnconfigure(i, weight=1)

# Create responsive layout
for row in range(3):
    for col in range(3):
        button = customtkinter.CTkButton(
            app,
            text=f"Button {row},{col}"
        )
        button.grid(
            row=row, 
            column=col, 
            sticky="nsew", 
            padx=5, 
            pady=5
        )

app.mainloop()
```

---

## Widget Reference

### CTkButton

**Purpose:** Clickable button with command callback

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

def button_callback():
    print("Button clicked!")

# Basic button
button1 = customtkinter.CTkButton(
    app,
    text="Click Me",
    command=button_callback
)
button1.pack(pady=10)

# Styled button with all parameters
button2 = customtkinter.CTkButton(
    app,
    master=app,                          # Parent widget
    text="Styled Button",
    command=button_callback,
    width=150,                           # Width in pixels
    height=40,                           # Height in pixels
    corner_radius=8,                     # Corner rounding
    border_width=2,                      # Border thickness
    border_spacing=4,                    # Space between border and content
    fg_color=("blue", "#003d7a"),        # (light, dark) colors
    hover_color=("darkblue", "#002855"), # Hover state color
    border_color=("black", "white"),     # Border color
    text_color=("white", "white"),       # Text color
    text_color_disabled="gray",          # Disabled text color
    font=("Arial", 14),                  # Font (family, size)
    state="normal",                      # "normal" or "disabled"
    hover=True,                          # Enable hover effect
    compound="left",                     # Position of image vs text
    anchor="center"                      # Text alignment
)
button2.pack(pady=10)

# Disabled button
button3 = customtkinter.CTkButton(
    app,
    text="Disabled Button",
    state="disabled"
)
button3.pack(pady=10)

# Button methods
def toggle_button():
    if button2.cget("state") == "normal":
        button2.configure(state="disabled", text="Now Disabled")
    else:
        button2.configure(state="normal", text="Now Enabled")

toggle_btn = customtkinter.CTkButton(
    app,
    text="Toggle Button State",
    command=toggle_button
)
toggle_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| text | str | The label text to display on the button |
| command | function | The callback function to execute when button is clicked |
| width/height | int | Explicit size in pixels (if not set, button auto-sizes to content) |
| corner_radius | int | Amount of rounding for button corners (0 for square, higher values for more rounded) |
| fg_color | str/tuple | Background color of the button (use tuple for light/dark mode: (light, dark)) |
| hover_color | str/tuple | Background color when mouse hovers over button |
| text_color | str/tuple | Color of the button text |
| state | str | Button state - "normal" (clickable), "disabled" (grayed out), or "hover" (shows hover color) |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .configure() |  | - Update widget properties |
| .cget() |  | - Get property value |
| .invoke() |  | - Trigger button click |

---

### CTkLabel

**Purpose:** Display static text or images

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic label
label1 = customtkinter.CTkLabel(
    app,
    text="Simple Label"
)
label1.pack(pady=10)

# Label with full customization
label2 = customtkinter.CTkLabel(
    app,
    text="Styled Label",
    width=200,                           # Width in pixels
    height=50,                           # Height in pixels
    corner_radius=8,                     # Corner rounding
    fg_color=("lightblue", "darkblue"),  # Background color
    text_color=("black", "white"),       # Text color
    font=("Arial", 16, "bold"),          # Font specification
    anchor="center",                     # Text position
    justify="center",                    # Multi-line justify
    wraplength=150                       # Text wrapping width
)
label2.pack(pady=10)

# Multi-line label
label3 = customtkinter.CTkLabel(
    app,
    text="This is a label with\nmultiple lines of text",
    justify="left",
    wraplength=300
)
label3.pack(pady=10)

# Label with transparency
label4 = customtkinter.CTkLabel(
    app,
    text="Transparent Label",
    fg_color="transparent",
    text_color="darkblue"
)
label4.pack(pady=10)

# Dynamic label update
from tkinter import StringVar

text_var = StringVar(value="Initial Text")
label5 = customtkinter.CTkLabel(app, textvariable=text_var)
label5.pack(pady=10)

def update_label():
    text_var.set("Updated Text!")

update_btn = customtkinter.CTkButton(
    app,
    text="Update Label",
    command=update_label
)
update_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| text | str | The text content displayed in the label |
| textvariable | StringVar | A StringVar object for dynamic text updates without recreating the label |
| width/height | int | Explicit size in pixels (labels usually auto-size to fit text) |
| fg_color | str/tuple | Background color of the label area (use tuple for light/dark: (light, dark)) |
| text_color | str/tuple | Color of the text content |
| font | tuple | Font specification as (family, size) like ("Arial", 14) or (family, size, weight) |
| anchor | str | Text alignment within label - "nw" (top-left), "center", "se" (bottom-right), etc. |
| justify | str | How to justify multi-line text - "left", "center", or "right" |

---

### CTkEntry

**Purpose:** Single-line text input

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic entry
entry1 = customtkinter.CTkEntry(app)
entry1.pack(pady=10, padx=20, fill="x")

# Entry with placeholder
entry2 = customtkinter.CTkEntry(
    app,
    placeholder_text="Enter your name"
)
entry2.pack(pady=10, padx=20, fill="x")

# Fully customized entry
entry3 = customtkinter.CTkEntry(
    app,
    placeholder_text="Email address",
    width=300,                           # Width in pixels
    height=40,                           # Height in pixels
    corner_radius=8,                     # Corner rounding
    border_width=2,                      # Border thickness
    fg_color=("white", "#212121"),       # Background color
    border_color=("gray", "darkgray"),   # Border color
    text_color=("black", "white"),       # Text color
    placeholder_text_color="gray",       # Placeholder color
    font=("Arial", 14),                  # Text font
    state="normal"                       # "normal", "disabled", or "readonly"
)
entry3.pack(pady=10, padx=20, fill="x")

# Password entry
entry4 = customtkinter.CTkEntry(
    app,
    placeholder_text="Password",
    show="*"                             # Hide characters
)
entry4.pack(pady=10, padx=20, fill="x")

# Get entry value
def get_value():
    value = entry3.get()
    print(f"Entry value: {value}")

button = customtkinter.CTkButton(
    app,
    text="Get Value",
    command=get_value
)
button.pack(pady=10)

# Set entry value
def set_value():
    entry3.delete(0, "end")
    entry3.insert(0, "New value")

set_btn = customtkinter.CTkButton(
    app,
    text="Set Value",
    command=set_value
)
set_btn.pack(pady=10)

# Clear entry
def clear_entry():
    entry3.delete(0, "end")

clear_btn = customtkinter.CTkButton(
    app,
    text="Clear",
    command=clear_entry
)
clear_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| placeholder_text | str | Hint text shown when entry is empty (disappears when user starts typing) |
| width/height | int | Size of the entry field in pixels |
| corner_radius | int | Amount of corner rounding for the entry box |
| border_width | int | Thickness of the border around the entry field |
| fg_color | str/tuple | Background color of the entry field (light/dark tuple for theming) |
| text_color | str/tuple | Color of the text user types |
| font | tuple | Font for user input text, e.g., ("Arial", 12) |
| show | str | Character to show instead of actual input (use "*" for password fields) |
| state | str | "normal" (editable), "disabled" (grayed and read-only), or "readonly" (read-only but not grayed) |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get() |  | - Get entry value |
| .insert(index, text) |  | - Insert text |
| .delete(start, end) |  | - Delete text |
| .select_range(start, end) |  | - Select text range |
| .select_clear() |  | - Clear selection |
| .focus() |  | - Focus entry |

---

### CTkTextbox

**Purpose:** Multi-line text input and display

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic textbox
textbox1 = customtkinter.CTkTextbox(
    app,
    width=400,
    height=150
)
textbox1.pack(pady=10, padx=20)

# Textbox with customization
textbox2 = customtkinter.CTkTextbox(
    app,
    width=400,
    height=150,
    corner_radius=8,
    border_width=2,
    fg_color=("white", "#212121"),
    border_color=("gray", "darkgray"),
    text_color=("black", "white"),
    font=("Arial", 12),
    state="normal",
    wrap="word"                          # "word", "char", or "none"
)
textbox2.pack(pady=10, padx=20)

# Insert initial text
textbox2.insert("0.0", "Enter text here...")

# Get textbox value
def get_textbox_value():
    value = textbox2.get("1.0", "end")
    print(f"Textbox value:\n{value}")

button = customtkinter.CTkButton(
    app,
    text="Get Text",
    command=get_textbox_value
)
button.pack(pady=10)

# Clear textbox
def clear_textbox():
    textbox2.delete("1.0", "end")

clear_btn = customtkinter.CTkButton(
    app,
    text="Clear",
    command=clear_textbox
)
clear_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| width/height | int | Size of the textbox in pixels |
| corner_radius | int | Corner rounding amount for the textbox container |
| fg_color | str/tuple | Background color of the textbox editing area |
| text_color | str/tuple | Color of the text content |
| font | tuple | Font for the textbox text, e.g., ("Courier", 11) for monospace |
| wrap | str | How to wrap text - "word" (wrap at word boundaries), "char" (wrap at any character), or "none" (no wrapping) |
| state | str | "normal" (fully editable), "disabled" (read-only and grayed), or "readonly" (read-only but not grayed) |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get(start, end) |  | - Get text (use "1.0" for start, "end" for end) |
| .insert(index, text) |  | - Insert text |
| .delete(start, end) |  | - Delete text |
| .focus() |  | - Focus textbox |

---

### CTkFrame

**Purpose:** Container for grouping widgets

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x500")

# Basic frame
frame1 = customtkinter.CTkFrame(app)
frame1.pack(pady=10, padx=10, fill="both", expand=True)

label1 = customtkinter.CTkLabel(frame1, text="Frame 1 Content")
label1.pack(pady=10)

# Styled frame
frame2 = customtkinter.CTkFrame(
    app,
    width=300,                           # Width in pixels
    height=200,                          # Height in pixels
    corner_radius=10,                    # Corner rounding
    border_width=2,                      # Border thickness
    border_color=("gray", "darkgray"),   # Border color
    fg_color=("lightgray", "#212121")    # Background color
)
frame2.pack(pady=10, padx=10)

# Add widgets to frame
label2 = customtkinter.CTkLabel(frame2, text="Styled Frame")
label2.pack(pady=10)

button = customtkinter.CTkButton(frame2, text="Button in Frame")
button.pack(pady=10)

# Nested frames for layout
outer_frame = customtkinter.CTkFrame(app)
outer_frame.pack(pady=10, padx=10, fill="both", expand=True)

inner_frame1 = customtkinter.CTkFrame(outer_frame)
inner_frame1.pack(side="left", fill="both", expand=True, padx=5)

inner_label1 = customtkinter.CTkLabel(inner_frame1, text="Left Section")
inner_label1.pack()

inner_frame2 = customtkinter.CTkFrame(outer_frame)
inner_frame2.pack(side="right", fill="both", expand=True, padx=5)

inner_label2 = customtkinter.CTkLabel(inner_frame2, text="Right Section")
inner_label2.pack()

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| width/height | int | Size in pixels |
| corner_radius | int | Rounded corners |
| border_width | int | Border thickness |
| border_color | str/tuple | Border color |
| fg_color | str/tuple | Background color |

---

### CTkScrollableFrame

**Purpose:** Frame with automatic scrollbar for overflow content

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Create scrollable frame
scrollable_frame = customtkinter.CTkScrollableFrame(
    app,
    width=400,
    height=300,
    corner_radius=10,
    label_text="Scrollable Content"
)
scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Add many widgets to demonstrate scrolling
for i in range(20):
    label = customtkinter.CTkLabel(
        scrollable_frame,
        text=f"Item {i+1}",
        font=("Arial", 14)
    )
    label.pack(pady=5)
    
    button = customtkinter.CTkButton(
        scrollable_frame,
        text=f"Button {i+1}",
        command=lambda i=i: print(f"Button {i+1} clicked")
    )
    button.pack(pady=5)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| width/height | int | Size of the scrollable frame in pixels |
| corner_radius | int | Amount of corner rounding for the frame |
| label_text | str | Optional text displayed at the top of the scrollable frame |
| label_fg_color | str/tuple | Background color of the label area |
| label_text_color | str/tuple | Color of the label text |
| label_font | tuple | Font specification for the label |

---

### CTkSlider

**Purpose:** Numeric input with slider control

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic slider
slider1 = customtkinter.CTkSlider(
    app,
    from_=0,                            # Minimum value
    to=100,                             # Maximum value
    command=lambda v: print(f"Slider: {v}")
)
slider1.pack(pady=10, padx=20, fill="x")

# Slider with customization
slider2 = customtkinter.CTkSlider(
    app,
    from_=0,
    to=100,
    width=300,                          # Width in pixels
    height=20,                          # Height in pixels
    border_width=2,                     # Border thickness
    corner_radius=8,                    # Corner rounding
    fg_color=("gray", "darkgray"),      # Background color
    progress_color=("blue", "#0052a3"), # Progress color
    button_color=("white", "white"),    # Button color
    button_hover_color=("lightgray", "gray"),
    state="normal",                     # "normal" or "disabled"
    number_of_steps=10,                 # Discrete steps
    orientation="horizontal"             # "horizontal" or "vertical"
)
slider2.pack(pady=10, padx=20, fill="x")

# Get slider value
def get_slider_value():
    value = slider2.get()
    print(f"Slider value: {value}")

button = customtkinter.CTkButton(
    app,
    text="Get Value",
    command=get_slider_value
)
button.pack(pady=10)

# Set slider value
def set_slider_value():
    slider2.set(50)

set_btn = customtkinter.CTkButton(
    app,
    text="Set to 50",
    command=set_slider_value
)
set_btn.pack(pady=10)

# Real-time display
value_label = customtkinter.CTkLabel(app, text="Value: 0")
value_label.pack(pady=10)

def update_label(value):
    value_label.configure(text=f"Value: {value:.1f}")
    slider2.configure(command=update_label)

slider2.set(0)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| from_/to | int/float | Minimum and maximum values the slider can be set to |
| width/height | int | Dimensions of the slider in pixels |
| corner_radius | int | Amount of corner rounding |
| border_width | int | Thickness of the slider border |
| fg_color | str/tuple | Background color of the slider track |
| progress_color | str/tuple | Color of the filled/active portion of the slider |
| button_color | str/tuple | Color of the slider drag button/thumb |
| number_of_steps | int | Number of discrete stopping points (0 for continuous) |
| orientation | str | "horizontal" for left-right or "vertical" for up-down |
| command | function | Callback function called when slider value changes |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get() |  | - Get current value |
| .set(value) |  | - Set value |

---

### CTkProgressBar

**Purpose:** Display progress indication

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic progress bar
progress1 = customtkinter.CTkProgressBar(app)
progress1.pack(pady=10, padx=20, fill="x")

# Set progress
progress1.set(0.5)  # 50%

# Customized progress bar
progress2 = customtkinter.CTkProgressBar(
    app,
    width=300,                          # Width in pixels
    height=20,                          # Height in pixels
    corner_radius=8,                    # Corner rounding
    border_width=2,                     # Border thickness
    fg_color=("gray", "darkgray"),      # Background color
    progress_color=("green", "#00aa00"),# Progress color
    border_color=("black", "white")     # Border color
)
progress2.pack(pady=10, padx=20, fill="x")

progress2.set(0.75)  # 75%

# Animated progress
import time

def animate_progress():
    for i in range(101):
        progress1.set(i / 100)
        app.update()
        time.sleep(0.01)

button = customtkinter.CTkButton(
    app,
    text="Animate Progress",
    command=animate_progress
)
button.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| width/height | int | Size in pixels |
| corner_radius | int | Rounded corners |
| border_width | int | Border thickness |
| fg_color | str/tuple | Background color |
| progress_color | str/tuple | Progress bar color |
| border_color | str/tuple | Border color |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get() |  | - Get current progress (0.0 to 1.0) |
| .set(value) |  | - Set progress (0.0 to 1.0) |

---

### CTkCheckBox

**Purpose:** Boolean toggle with label

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x400")

# Basic checkbox
checkbox1 = customtkinter.CTkCheckBox(
    app,
    text="Enable Feature",
    command=lambda: print(f"Checkbox: {checkbox1.get()}")
)
checkbox1.pack(pady=10)

# Customized checkbox
checkbox2 = customtkinter.CTkCheckBox(
    app,
    text="Accept Terms",
    width=20,                           # Checkbox width in pixels
    height=20,                          # Checkbox height in pixels
    corner_radius=4,                    # Corner rounding
    border_width=2,                     # Border thickness
    border_color=("gray", "darkgray"),  # Border color
    fg_color=("blue", "#0052a3"),       # Checked color
    hover_color=("darkblue", "#003d7a"),# Hover color
    checkmark_color=("white", "white"), # Checkmark color
    text_color=("black", "white"),      # Text color
    font=("Arial", 12),                 # Font
    state="normal",                     # "normal" or "disabled"
    onvalue=True,                       # Value when checked
    offvalue=False                      # Value when unchecked
)
checkbox2.pack(pady=10, padx=20)

# Get checkbox state
def get_checkbox_state():
    state = checkbox2.get()
    print(f"Checkbox state: {state}")

button = customtkinter.CTkButton(
    app,
    text="Get State",
    command=get_checkbox_state
)
button.pack(pady=10)

# Set checkbox state
def set_checkbox_state():
    checkbox2.select()  # Check
    # checkbox2.deselect()  # Uncheck
    # checkbox2.toggle()  # Toggle

set_btn = customtkinter.CTkButton(
    app,
    text="Check",
    command=set_checkbox_state
)
set_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| text | str | Label text displayed next to the checkbox |
| width/height | int | Size of the checkbox widget in pixels |
| corner_radius | int | Amount of rounding for the checkbox corners |
| border_width | int | Thickness of the checkbox border |
| border_color | str/tuple | Color of the checkbox border line |
| fg_color | str/tuple | Background color when the checkbox is checked |
| hover_color | str/tuple | Color that appears when mouse hovers over the checkbox |
| checkmark_color | str/tuple | Color of the checkmark symbol inside |
| text_color | str/tuple | Color of the label text |
| font | tuple | Font specification for the label text |
| command | function | Callback function when checkbox is clicked |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get() |  | - Get state (True/False) |
| .select() |  | - Check |
| .deselect() |  | - Uncheck |
| .toggle() |  | - Toggle state |

---

### CTkSwitch

**Purpose:** Toggle switch for boolean values

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x400")

# Basic switch
switch1 = customtkinter.CTkSwitch(
    app,
    text="Dark Mode",
    command=lambda: print(f"Switch: {switch1.get()}")
)
switch1.pack(pady=10)

# Customized switch
switch2 = customtkinter.CTkSwitch(
    app,
    text="Notifications",
    width=50,                           # Switch width in pixels
    height=28,                          # Switch height in pixels
    corner_radius=14,                   # Corner rounding
    border_width=2,                     # Border thickness
    fg_color=("gray", "gray"),          # Off color
    progress_color=("green", "#00aa00"),# On color
    button_color=("white", "white"),    # Button color
    button_hover_color=("lightgray", "gray"),
    text_color=("black", "white"),      # Text color
    font=("Arial", 12),                 # Font
    state="normal",                     # "normal" or "disabled"
    command=lambda: print(f"Switch2: {switch2.get()}")
)
switch2.pack(pady=10, padx=20)

# Get switch state
def get_switch_state():
    state = switch2.get()
    print(f"Switch state: {state}")

button = customtkinter.CTkButton(
    app,
    text="Get State",
    command=get_switch_state
)
button.pack(pady=10)

# Set switch state
def set_switch_state():
    switch2.select()  # Turn on
    # switch2.deselect()  # Turn off
    # switch2.toggle()  # Toggle

set_btn = customtkinter.CTkButton(
    app,
    text="Turn On",
    command=set_switch_state
)
set_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| text | str | Label text displayed next to the switch |
| width/height | int | Dimensions of the switch widget in pixels |
| corner_radius | int | Amount of rounding for the switch edges |
| border_width | int | Thickness of the switch border |
| fg_color | str/tuple | Background color when switch is OFF/disabled |
| progress_color | str/tuple | Background color when switch is ON/enabled |
| button_color | str/tuple | Color of the sliding button/thumb |
| button_hover_color | str/tuple | Color of the button when mouse hovers over it |
| text_color | str/tuple | Color of the label text |
| font | tuple | Font specification for the label |
| command | function | Callback function called when switch is toggled |
| state | str | "normal" (fully functional) or "disabled" (grayed out and non-functional) |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .get() |  | - Get state (True/False) |
| .select() |  | - Turn on |
| .deselect() |  | - Turn off |
| .toggle() |  | - Toggle state |

---

### CTkRadioButton

**Purpose:** Mutually exclusive selection option

```python
import customtkinter
from tkinter import IntVar

app = customtkinter.CTk()
app.geometry("400x400")

# Create variable to store radio button value
radio_var = IntVar(value=0)

# Radio button group
radio1 = customtkinter.CTkRadioButton(
    app,
    text="Option 1",
    variable=radio_var,
    value=1,
    command=lambda: print(f"Selected: {radio_var.get()}")
)
radio1.pack(pady=10)

radio2 = customtkinter.CTkRadioButton(
    app,
    text="Option 2",
    variable=radio_var,
    value=2
)
radio2.pack(pady=10)

radio3 = customtkinter.CTkRadioButton(
    app,
    text="Option 3",
    variable=radio_var,
    value=3
)
radio3.pack(pady=10)

# Customized radio buttons
radio_var2 = IntVar(value=0)

radio4 = customtkinter.CTkRadioButton(
    app,
    text="Customized Option 1",
    variable=radio_var2,
    value=1,
    width=20,                           # Button width in pixels
    height=20,                          # Button height in pixels
    corner_radius=10,                   # Corner rounding
    border_width=2,                     # Border thickness
    border_color=("gray", "darkgray"),  # Border color
    fg_color=("blue", "#0052a3"),       # Selected color
    hover_color=("darkblue", "#003d7a"),# Hover color
    text_color=("black", "white"),      # Text color
    font=("Arial", 12)                  # Font
)
radio4.pack(pady=10, padx=20)

radio5 = customtkinter.CTkRadioButton(
    app,
    text="Customized Option 2",
    variable=radio_var2,
    value=2,
    width=20,
    height=20,
    corner_radius=10,
    border_width=2,
    border_color=("gray", "darkgray"),
    fg_color=("blue", "#0052a3"),
    hover_color=("darkblue", "#003d7a"),
    text_color=("black", "white"),
    font=("Arial", 12)
)
radio5.pack(pady=10, padx=20)

# Get selected radio button
def get_radio_selection():
    selected = radio_var.get()
    print(f"Selected: Option {selected}")

button = customtkinter.CTkButton(
    app,
    text="Get Selection",
    command=get_radio_selection
)
button.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| text | str | Label text displayed next to the radio button |
| variable | IntVar/StringVar | Shared variable that stores which radio button is selected |
| value | int/str | The unique value assigned to this radio button (stored when selected) |
| width/height | int | Dimensions of the radio button widget in pixels |
| corner_radius | int | Amount of rounding for the radio button circle |
| border_width | int | Thickness of the border around the radio button |
| border_color | str/tuple | Color of the radio button border |
| fg_color | str/tuple | Background color when this radio button is selected |
| hover_color | str/tuple | Color that appears when mouse hovers over the button |
| text_color | str/tuple | Color of the label text |
| font | tuple | Font specification for the label |
| command | function | Callback function executed when this radio button is selected |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .select() |  | - Select this option |

---

### CTkComboBox

**Purpose:** Dropdown selection with optional typing

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic combobox
combobox1 = customtkinter.CTkComboBox(
    app,
    values=["Option 1", "Option 2", "Option 3"],
    command=lambda v: print(f"Selected: {v}")
)
combobox1.pack(pady=10, padx=20, fill="x")

# Customized combobox
combobox2 = customtkinter.CTkComboBox(
    app,
    values=["Red", "Green", "Blue", "Yellow", "Orange"],
    width=300,                          # Width in pixels
    height=40,                          # Height in pixels
    corner_radius=8,                    # Corner rounding
    border_width=2,                     # Border thickness
    fg_color=("white", "#212121"),      # Background color
    border_color=("gray", "darkgray"),  # Border color
    text_color=("black", "white"),      # Text color
    dropdown_fg_color=("white", "#212121"),
    dropdown_text_color=("black", "white"),
    button_color=("gray", "darkgray"),  # Dropdown button color
    button_hover_color=("lightgray", "gray"),
    font=("Arial", 12),                 # Font
    state="readonly",                   # "readonly" or "normal"
    command=lambda v: print(f"Color: {v}")
)
combobox2.pack(pady=10, padx=20, fill="x")

# Get combobox value
def get_combobox_value():
    value = combobox2.get()
    print(f"Selected color: {value}")

button = customtkinter.CTkButton(
    app,
    text="Get Value",
    command=get_combobox_value
)
button.pack(pady=10)

# Set combobox value
def set_combobox_value():
    combobox2.set("Blue")

set_btn = customtkinter.CTkButton(
    app,
    text="Set to Blue",
    command=set_combobox_value
)
set_btn.pack(pady=10)

# Dynamic options
combobox3 = customtkinter.CTkComboBox(
    app,
    values=[],
    state="readonly"
)
combobox3.pack(pady=10, padx=20, fill="x")

def update_options():
    combobox3.configure(values=["New 1", "New 2", "New 3"])

update_btn = customtkinter.CTkButton(
    app,
    text="Update Options",
    command=update_options
)
update_btn.pack(pady=10)

app.mainloop()
```

#### CTkComboBox Parameters & Methods

| Parameter | Type | Description & Usage |
|-----------|------|-------------------|
| `values` | list | The list of options that appear in the dropdown menu. Users can select from these options. Example: `["Red", "Green", "Blue"]`. Can be updated at runtime. |
| `width` | int | The width of the combobox field in pixels. Controls how much horizontal space the widget takes up on screen. Default is usually 120 pixels. |
| `height` | int | The height of the combobox field in pixels. Controls the vertical size of the input area. Standard height is around 28-40 pixels. |
| `corner_radius` | int | Controls how rounded the corners of the combobox are. Use 0 for sharp corners, higher values (8-15) for rounded corners. Makes the widget look more modern. |
| `border_width` | int | The thickness of the border line around the combobox in pixels. Use 0 for no border, 1-3 for visible borders. Helps define widget boundaries. |
| `fg_color` | str/tuple | Background color of the input field. Use tuple format `("light_color", "dark_color")` for light/dark theme support. Example: `("white", "#212121")`. |
| `border_color` | str/tuple | Color of the border line around the combobox. Also supports light/dark tuple format for theming. Typically gray or a theme accent color. |
| `text_color` | str/tuple | Color of the text that appears in the combobox (both typed and selected text). Use tuples for theme support. Example: `("black", "white")`. |
| `dropdown_fg_color` | str/tuple | Background color of the dropdown menu list when opened. Should contrast with text color for readability. Supports light/dark tuples. |
| `dropdown_text_color` | str/tuple | Color of the text in the dropdown list options. Should be readable against the dropdown background color. |
| `button_color` | str/tuple | Color of the dropdown arrow button on the right side. Typically matches the theme accent color. |
| `button_hover_color` | str/tuple | Color the arrow button turns when user hovers mouse over it. Provides visual feedback that the button is interactive. |
| `font` | tuple | Font specification for the text in the combobox. Format: `("FontName", size)` or `("FontName", size, "weight")`. Example: `("Arial", 12)`. |
| `state` | str | Controls whether the combobox is editable. `"readonly"` allows only selection from list, `"normal"` allows user typing. Use "readonly" for strict options. |
| `command` | function | Callback function executed when user selects an option. Receives the selected value as parameter. Example: `command=lambda v: print(v)`. |

#### Common Methods for CTkComboBox

| Method | Purpose & Usage |
|--------|-----------------|
| `.get()` | Returns the currently selected value from the combobox. Use this to retrieve user's selection in your code. Example: `selected = combobox.get()` |
| `.set(value)` | Programmatically sets the combobox to a specific value. Useful for pre-selecting an option or updating based on other events. Example: `combobox.set("Blue")` |
| `.configure(values=[...])` | Updates the list of available options at runtime. Allows dynamic changing of dropdown items based on application logic. Example: `combobox.configure(values=["New1", "New2"])` |

---

### CTkOptionMenu

**Purpose:** Popup menu for selection

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x400")

# Basic option menu
options_var = customtkinter.StringVar(value="Option 1")

option_menu1 = customtkinter.CTkOptionMenu(
    app,
    variable=options_var,
    values=["Option 1", "Option 2", "Option 3"],
    command=lambda v: print(f"Selected: {v}")
)
option_menu1.pack(pady=10)

# Customized option menu
size_var = customtkinter.StringVar(value="Medium")

option_menu2 = customtkinter.CTkOptionMenu(
    app,
    variable=size_var,
    values=["Small", "Medium", "Large", "Extra Large"],
    width=200,                          # Width in pixels
    height=40,                          # Height in pixels
    corner_radius=8,                    # Corner rounding
    fg_color=("white", "#212121"),      # Background color
    button_color=("blue", "#0052a3"),   # Button color
    button_hover_color=("darkblue", "#003d7a"),
    text_color=("black", "white"),      # Text color
    dropdown_fg_color=("white", "#212121"),
    dropdown_text_color=("black", "white"),
    font=("Arial", 12),                 # Font
    dropdown_font=("Arial", 12),
    command=lambda v: print(f"Size: {v}")
)
option_menu2.pack(pady=10)

# Get current selection
def get_selection():
    selected = size_var.get()
    print(f"Current selection: {selected}")

button = customtkinter.CTkButton(
    app,
    text="Get Selection",
    command=get_selection
)
button.pack(pady=10)

# Change options dynamically
option_menu3 = customtkinter.CTkOptionMenu(
    app,
    variable=customtkinter.StringVar(value="Option 1"),
    values=["Option 1", "Option 2"],
    command=lambda v: print(f"Selected: {v}")
)
option_menu3.pack(pady=10)

def update_menu_options():
    option_menu3.configure(values=["New 1", "New 2", "New 3"])

update_btn = customtkinter.CTkButton(
    app,
    text="Update Menu",
    command=update_menu_options
)
update_btn.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| variable | StringVar | Variable to store the currently selected option value |
| values | list | List of option strings to display in the dropdown menu |
| width/height | int | Dimensions of the option menu button in pixels |
| corner_radius | int | Amount of rounding for button corners |
| fg_color | str/tuple | Background color of the option menu button |
| button_color | str/tuple | Color of the dropdown arrow/button area |
| button_hover_color | str/tuple | Color of button when mouse hovers over it |
| text_color | str/tuple | Color of the selected option text |
| dropdown_fg_color | str/tuple | Background color of the dropdown list when opened |
| dropdown_text_color | str/tuple | Color of text in the dropdown list |
| font | tuple | Font for the selected text |
| dropdown_font | tuple | Font for the dropdown list options |
| command | function | Callback function called when selection changes |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .configure(values=[...]) |  | - Update options |

---

### CTkSegmentedButton

**Purpose:** Multiple choice button group

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("500x400")

# Basic segmented button
seg_var = customtkinter.StringVar(value="Option 1")

segmented1 = customtkinter.CTkSegmentedButton(
    app,
    values=["Option 1", "Option 2", "Option 3"],
    variable=seg_var,
    command=lambda v: print(f"Selected: {v}")
)
segmented1.pack(pady=10)

# Customized segmented button
theme_var = customtkinter.StringVar(value="Light")

segmented2 = customtkinter.CTkSegmentedButton(
    app,
    values=["Light", "Dark", "Auto"],
    variable=theme_var,
    width=300,                          # Width in pixels
    height=40,                          # Height in pixels
    corner_radius=8,                    # Corner rounding
    border_width=2,                     # Border thickness
    fg_color=("lightgray", "#212121"),  # Background color
    selected_color=("blue", "#0052a3"), # Selected color
    selected_hover_color=("darkblue", "#003d7a"),
    unselected_color=("white", "gray20"),
    unselected_hover_color=("lightgray", "gray30"),
    text_color=("black", "white"),      # Text color
    font=("Arial", 12),                 # Font
    command=lambda v: print(f"Theme: {v}")
)
segmented2.pack(pady=10)

# Get current selection
def get_segmented_value():
    selected = theme_var.get()
    print(f"Theme: {selected}")

button = customtkinter.CTkButton(
    app,
    text="Get Theme",
    command=get_segmented_value
)
button.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| values | list | List of button labels/options to display as segments |
| variable | StringVar | Variable to store which segment is currently selected |
| width/height | int | Total dimensions of the segmented button group in pixels |
| corner_radius | int | Amount of rounding for the button corners |
| border_width | int | Thickness of the border around buttons |
| fg_color | str/tuple | Background color of unselected buttons |
| selected_color | str/tuple | Background color of the currently selected button |
| selected_hover_color | str/tuple | Color when mouse hovers over the selected button |
| unselected_color | str/tuple | Specific color for unselected buttons (if different from fg_color) |
| unselected_hover_color | str/tuple | Color when mouse hovers over unselected buttons |
| text_color | str/tuple | Color of the button text |
| font | tuple | Font specification for the button labels |
| command | function | Callback function called when selection changes |

---

### CTkTabview

**Purpose:** Tabbed interface

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("600x400")

# Create tabview
tabview = customtkinter.CTkTabview(
    app,
    width=500,
    height=300,
    corner_radius=8,
    border_width=2,
    fg_color=("white", "#212121"),
    segmented_button_fg_color=("lightgray", "gray20"),
    segmented_button_selected_color=("blue", "#0052a3"),
    segmented_button_selected_hover_color=("darkblue", "#003d7a"),
    text_color=("black", "white"),
    anchor="nw"                         # Tab anchor position
)
tabview.pack(pady=10, padx=10, fill="both", expand=True)

# Add tabs
tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

# Add widgets to Tab 1
label1 = customtkinter.CTkLabel(
    tabview.tab("Tab 1"),
    text="Content for Tab 1"
)
label1.pack(pady=20)

button1 = customtkinter.CTkButton(
    tabview.tab("Tab 1"),
    text="Button 1"
)
button1.pack(pady=10)

# Add widgets to Tab 2
label2 = customtkinter.CTkLabel(
    tabview.tab("Tab 2"),
    text="Content for Tab 2"
)
label2.pack(pady=20)

entry = customtkinter.CTkEntry(
    tabview.tab("Tab 2"),
    placeholder_text="Enter text"
)
entry.pack(pady=10)

# Add widgets to Tab 3
label3 = customtkinter.CTkLabel(
    tabview.tab("Tab 3"),
    text="Content for Tab 3"
)
label3.pack(pady=20)

slider = customtkinter.CTkSlider(
    tabview.tab("Tab 3"),
    from_=0,
    to=100
)
slider.pack(pady=10, padx=20, fill="x")

# Get current tab
def get_current_tab():
    current = tabview.get()
    print(f"Current tab: {current}")

button = customtkinter.CTkButton(
    app,
    text="Get Current Tab",
    command=get_current_tab
)
button.pack(pady=10)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| width/height | int | Dimensions of the entire tabview widget in pixels |
| corner_radius | int | Amount of rounding for the tabview corners |
| border_width | int | Thickness of the border around the tabview |
| fg_color | str/tuple | Background color of the tab content area |
| segmented_button_fg_color | str/tuple | Background color of the tab button bar |
| segmented_button_selected_color | str/tuple | Color of the active/selected tab button |
| segmented_button_selected_hover_color | str/tuple | Color when hovering over the selected tab |
| segmented_button_unselected_color | str/tuple | Color of unselected tab buttons |
| segmented_button_unselected_hover_color | str/tuple | Color when hovering over unselected tabs |
| text_color | str/tuple | Color of text in tab content |
| anchor | str | Position of tabs - "nw" (top-left), "n" (top-center), etc. |
| command | function | Callback function when tab changes (optional) |

**Common Methods:**

| Method | Signature | Description |
| --- | --- | --- |
| .add(name) |  | - Add tab |
| .tab(name) |  | - Get tab by name |
| .get() |  | - Get current tab name |
| .set(name) |  | - Set current tab |
| .delete(name) |  | - Delete tab |

---

### CTkScrollbar

**Purpose:** Manual scrollbar control

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("600x400")

# Create frame with scrollbar
main_frame = customtkinter.CTkFrame(app)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create scrollable area
canvas = customtkinter.CTkCanvas(
    main_frame,
    bg="#f0f0f0" if customtkinter.get_appearance_mode() == "Light" else "#212121"
)
scrollbar = customtkinter.CTkScrollbar(
    main_frame,
    orientation="vertical",
    command=canvas.yview,
    width=20,                           # Scrollbar width in pixels
    corner_radius=10,                   # Corner rounding
    fg_color=("gray", "darkgray"),      # Background color
    button_color=("blue", "#0052a3"),   # Button color
    button_hover_color=("darkblue", "#003d7a")
)

# Configure canvas with scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create scrollable frame inside canvas
scrollable_frame = customtkinter.CTkFrame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add content to scrollable frame
for i in range(20):
    button = customtkinter.CTkButton(
        scrollable_frame,
        text=f"Item {i+1}"
    )
    button.pack(pady=5, padx=10, fill="x")

# Update scroll region
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

app.mainloop()
```

**Key Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| orientation | str | "vertical" or "horizontal" |
| width | int | Scrollbar width in pixels |
| corner_radius | int | Rounded corners |
| fg_color | str/tuple | Background color |
| button_color | str/tuple | Button color |
| button_hover_color | str/tuple | Hover color |
| command | function | Callback for scroll command |

---

### CTkImage

**Purpose:** Load and display images

```python
import customtkinter
from PIL import Image

app = customtkinter.CTk()
app.geometry("500x400")

# Load image from file
try:
    image = customtkinter.CTkImage(
        light_image=Image.open("path/to/light_image.png"),
        dark_image=Image.open("path/to/dark_image.png"),
        size=(200, 200)                 # Image size in pixels
    )
    
    image_label = customtkinter.CTkLabel(
        app,
        image=image,
        text=""                         # Empty text to show only image
    )
    image_label.pack(pady=20)
except FileNotFoundError:
    # Fallback label if image not found
    label = customtkinter.CTkLabel(
        app,
        text="Image not found"
    )
    label.pack(pady=20)

# Image on button
try:
    button_image = customtkinter.CTkImage(
        light_image=Image.open("path/to/button_icon.png"),
        dark_image=Image.open("path/to/button_icon.png"),
        size=(30, 30)
    )
    
    button = customtkinter.CTkButton(
        app,
        image=button_image,
        text="",                        # Image only
        width=50,
        height=50
    )
    button.pack(pady=10)
except FileNotFoundError:
    pass

# Create a simple test image (requires PIL)
from PIL import Image as PILImage
import os

# Create a temporary test image if it doesn't exist
test_image_path = "test_image.png"
if not os.path.exists(test_image_path):
    test_img = PILImage.new('RGB', (100, 100), color='red')
    test_img.save(test_image_path)

app.mainloop()
```

**Parameters:**

| Parameter | Type | Description |
| --- | --- | --- |
| light_image | PIL.Image | Image for light mode |
| dark_image | PIL.Image | Image for dark mode |
| size | tuple | (width, height) in pixels |

---

## Event Handling & Callbacks

### Button Commands

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

# Simple callback
def on_button_click():
    print("Button clicked!")

button1 = customtkinter.CTkButton(
    app,
    text="Simple Button",
    command=on_button_click
)
button1.pack(pady=10)

# Lambda for parameters
def greet(name):
    print(f"Hello, {name}!")

button2 = customtkinter.CTkButton(
    app,
    text="Lambda Button",
    command=lambda: greet("User")
)
button2.pack(pady=10)

# Multiple widgets with callbacks
counter = 0

def increment():
    global counter
    counter += 1
    label.configure(text=f"Count: {counter}")

def decrement():
    global counter
    counter -= 1
    label.configure(text=f"Count: {counter}")

label = customtkinter.CTkLabel(app, text="Count: 0")
label.pack(pady=10)

button_inc = customtkinter.CTkButton(
    app,
    text="Increment",
    command=increment
)
button_inc.pack(pady=5)

button_dec = customtkinter.CTkButton(
    app,
    text="Decrement",
    command=decrement
)
button_dec.pack(pady=5)

app.mainloop()
```

### Entry Commands

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

entry = customtkinter.CTkEntry(
    app,
    placeholder_text="Type here",
    width=300
)
entry.pack(pady=10)

# Real-time input handling
result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=10)

def on_entry_change(*args):
    value = entry.get()
    result_label.configure(text=f"Input: {value}")

# Note: CustomTkinter Entry doesn't have direct variable binding
# Use a button instead
def on_submit():
    value = entry.get()
    print(f"Submitted: {value}")

submit_btn = customtkinter.CTkButton(
    app,
    text="Submit",
    command=on_submit
)
submit_btn.pack(pady=10)

app.mainloop()
```

### Slider Commands

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

value_label = customtkinter.CTkLabel(app, text="Value: 0")
value_label.pack(pady=10)

def on_slider_change(value):
    value_label.configure(text=f"Value: {value:.1f}")

slider = customtkinter.CTkSlider(
    app,
    from_=0,
    to=100,
    command=on_slider_change
)
slider.pack(pady=10, padx=20, fill="x")

app.mainloop()
```

### CheckBox and Switch Commands

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

def on_checkbox_change():
    state = checkbox.get()
    print(f"Checkbox: {state}")

checkbox = customtkinter.CTkCheckBox(
    app,
    text="Enable Feature",
    command=on_checkbox_change
)
checkbox.pack(pady=10)

def on_switch_change():
    state = switch.get()
    print(f"Switch: {state}")

switch = customtkinter.CTkSwitch(
    app,
    text="Dark Mode",
    command=on_switch_change
)
switch.pack(pady=10)

app.mainloop()
```

### ComboBox Commands

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

def on_combobox_select(value):
    print(f"Selected: {value}")

combobox = customtkinter.CTkComboBox(
    app,
    values=["Option 1", "Option 2", "Option 3"],
    command=on_combobox_select
)
combobox.pack(pady=10, padx=20, fill="x")

app.mainloop()
```

### Event Binding with bind()

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("400x300")

label = customtkinter.CTkLabel(app, text="Click or hover on me")
label.pack(pady=20)

# Bind mouse events
def on_click(event):
    label.configure(text="You clicked!")

def on_hover(event):
    label.configure(text="Mouse over!")

def on_leave(event):
    label.configure(text="Click or hover on me")

label.bind("<Button-1>", on_click)          # Left mouse click
label.bind("<Enter>", on_hover)             # Mouse enter
label.bind("<Leave>", on_leave)             # Mouse leave

# Bind keyboard events
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")

app.bind("<KeyPress>", on_key_press)

app.mainloop()
```

### Common Event Types

```
Mouse Events:
- <Button-1>: Left mouse click
- <Button-3>: Right mouse click
- <Double-Button-1>: Double click
- <Enter>: Mouse enters widget
- <Leave>: Mouse leaves widget
- <Motion>: Mouse motion

Keyboard Events:
- <KeyPress>: Any key press
- <Return>: Enter key
- <Escape>: Escape key
- <a>, <b>, etc.: Specific key
- <Shift-a>: Key combinations

Window Events:
- <Configure>: Widget changed
- <Destroy>: Widget destroyed
- <FocusIn>: Widget receives focus
- <FocusOut>: Widget loses focus
```

---

## Best Practices

### 1. Use Classes for Complex Applications

```python
import customtkinter

class MyApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("My Application")
        self.geometry("600x400")
        
        # Configure appearance
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")
        
        # Setup layout
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = customtkinter.CTkLabel(
            self,
            text="Welcome",
            font=("Arial", 24, "bold")
        )
        header.pack(pady=20)
        
        # Content frame
        self.content_frame = customtkinter.CTkFrame(self)
        self.content_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Buttons
        button_frame = customtkinter.CTkFrame(self)
        button_frame.pack(pady=20)
        
        button1 = customtkinter.CTkButton(
            button_frame,
            text="Button 1",
            command=self.on_button1
        )
        button1.pack(side="left", padx=5)
        
        button2 = customtkinter.CTkButton(
            button_frame,
            text="Button 2",
            command=self.on_button2
        )
        button2.pack(side="left", padx=5)
        
    def on_button1(self):
        print("Button 1 clicked")
        
    def on_button2(self):
        print("Button 2 clicked")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
```

### 2. Responsive Layout with Grid

```python
import customtkinter

app = customtkinter.CTk()
app.geometry("800x600")

# Configure responsive grid
app.grid_rowconfigure((0, 1, 2), weight=1)
app.grid_columnconfigure((0, 1), weight=1)

# Header
header = customtkinter.CTkLabel(
    app,
    text="Responsive Layout",
    font=("Arial", 24)
)
header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

# Left panel
left_frame = customtkinter.CTkFrame(app)
left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

label1 = customtkinter.CTkLabel(left_frame, text="Left Panel")
label1.pack(pady=10)

# Right panel
right_frame = customtkinter.CTkFrame(app)
right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

label2 = customtkinter.CTkLabel(right_frame, text="Right Panel")
label2.pack(pady=10)

# Footer
footer = customtkinter.CTkLabel(
    app,
    text="Footer",
    fg_color="gray"
)
footer.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

app.mainloop()
```

### 3. Data Validation

```python
import customtkinter
from tkinter import messagebox

app = customtkinter.CTk()
app.geometry("400x300")

def validate_email(email):
    return "@" in email and "." in email

def on_submit():
    email = entry.get()
    
    if not email:
        messagebox.showerror("Error", "Email is required")
        return
    
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return
    
    messagebox.showinfo("Success", f"Email {email} is valid!")

label = customtkinter.CTkLabel(app, text="Enter email:")
label.pack(pady=10)

entry = customtkinter.CTkEntry(
    app,
    placeholder_text="user@example.com",
    width=300
)
entry.pack(pady=10, padx=20)

button = customtkinter.CTkButton(
    app,
    text="Submit",
    command=on_submit
)
button.pack(pady=10)

app.mainloop()
```

### 4. State Management

```python
import customtkinter

class AppState:
    def __init__(self):
        self.counter = 0
        self.is_running = False
        self.theme = "light"

class StateApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.state = AppState()
        self.title("State Management")
        self.geometry("400x300")
        
        self.setup_ui()
        
    def setup_ui(self):
        self.counter_label = customtkinter.CTkLabel(
            self,
            text=f"Counter: {self.state.counter}"
        )
        self.counter_label.pack(pady=10)
        
        button_inc = customtkinter.CTkButton(
            self,
            text="Increment",
            command=self.increment
        )
        button_inc.pack(pady=5)
        
        button_dec = customtkinter.CTkButton(
            self,
            text="Decrement",
            command=self.decrement
        )
        button_dec.pack(pady=5)
        
    def increment(self):
        self.state.counter += 1
        self.update_display()
        
    def decrement(self):
        self.state.counter -= 1
        self.update_display()
        
    def update_display(self):
        self.counter_label.configure(
            text=f"Counter: {self.state.counter}"
        )

if __name__ == "__main__":
    app = StateApp()
    app.mainloop()
```

### 5. Error Handling

```python
import customtkinter
from tkinter import messagebox

def safe_operation():
    try:
        # Perform operation
        value = int(entry.get())
        result = 100 / value
        result_label.configure(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

app = customtkinter.CTk()
app.geometry("400x300")

entry = customtkinter.CTkEntry(app, placeholder_text="Enter number")
entry.pack(pady=10, padx=20, fill="x")

button = customtkinter.CTkButton(
    app,
    text="Calculate",
    command=safe_operation
)
button.pack(pady=10)

result_label = customtkinter.CTkLabel(app, text="Result: ")
result_label.pack(pady=10)

app.mainloop()
```

---

## Common Patterns

### Modal Dialog

```python
import customtkinter
from tkinter import messagebox

def open_modal():
    dialog = customtkinter.CTkToplevel(app)
    dialog.title("Dialog")
    dialog.geometry("300x200")
    dialog.resizable(False, False)
    
    # Make dialog modal
    dialog.transient(app)
    dialog.grab_set()
    
    label = customtkinter.CTkLabel(
        dialog,
        text="This is a modal dialog"
    )
    label.pack(pady=20)
    
    button = customtkinter.CTkButton(
        dialog,
        text="Close",
        command=dialog.destroy
    )
    button.pack(pady=10)

app = customtkinter.CTk()
app.geometry("400x300")

button = customtkinter.CTkButton(
    app,
    text="Open Dialog",
    command=open_modal
)
button.pack(pady=20)

app.mainloop()
```

### Loading Indicator

```python
import customtkinter

class LoadingApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Loading Indicator")
        
        self.setup_ui()
        
    def setup_ui(self):
        self.label = customtkinter.CTkLabel(
            self,
            text="Click to load",
            font=("Arial", 16)
        )
        self.label.pack(pady=50)
        
        button = customtkinter.CTkButton(
            self,
            text="Start Loading",
            command=self.start_loading
        )
        button.pack(pady=10)
        
        self.progress = customtkinter.CTkProgressBar(self)
        self.progress.pack(pady=20, padx=20, fill="x")
        self.progress.set(0)
        
    def start_loading(self):
        import time
        
        self.label.configure(text="Loading...")
        self.update()
        
        for i in range(101):
            self.progress.set(i / 100)
            self.update()
            time.sleep(0.01)
        
        self.label.configure(text="Done!")

if __name__ == "__main__":
    app = LoadingApp()
    app.mainloop()
```

### Form Validation

```python
import customtkinter
from tkinter import messagebox

class FormApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title("Form Validation")
        
        self.setup_form()
        
    def setup_form(self):
        # Name field
        name_label = customtkinter.CTkLabel(self, text="Name:")
        name_label.pack(pady=5)
        
        self.name_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter name",
            width=300
        )
        self.name_entry.pack(pady=5)
        
        # Email field
        email_label = customtkinter.CTkLabel(self, text="Email:")
        email_label.pack(pady=5)
        
        self.email_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter email",
            width=300
        )
        self.email_entry.pack(pady=5)
        
        # Age field
        age_label = customtkinter.CTkLabel(self, text="Age:")
        age_label.pack(pady=5)
        
        self.age_entry = customtkinter.CTkEntry(
            self,
            placeholder_text="Enter age",
            width=300
        )
        self.age_entry.pack(pady=5)
        
        # Submit button
        submit_btn = customtkinter.CTkButton(
            self,
            text="Submit",
            command=self.validate_form
        )
        submit_btn.pack(pady=20)
        
    def validate_form(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        age = self.age_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        
        if not email or "@" not in email:
            messagebox.showerror("Error", "Valid email is required")
            return
        
        try:
            age_int = int(age)
            if age_int < 0 or age_int > 150:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid number")
            return
        
        messagebox.showinfo("Success", f"Form submitted!\nName: {name}\nEmail: {email}\nAge: {age}")

if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
```

---

---

## Custom Widget Creation

Creating custom widgets allows you to build reusable components that encapsulate both UI and behavior. This is especially useful for forms, dialogs, and repeated patterns in your application. By extending `CTkFrame`, you can combine multiple widgets into a single, easy-to-use component.

### Creating Reusable Components

```python
import customtkinter

class CTkLabeledEntry(customtkinter.CTkFrame):
    """Reusable labeled entry widget that combines a label and entry field"""
    def __init__(self, master, label_text, placeholder_text=""):
        super().__init__(master)
        # Create and pack label above the entry
        label = customtkinter.CTkLabel(self, text=label_text, font=("Arial", 12))
        label.pack(anchor="w", padx=10, pady=(10, 5))
        # Create and pack entry field
        self.entry = customtkinter.CTkEntry(self, placeholder_text=placeholder_text)
        self.entry.pack(padx=10, pady=5, fill="x", expand=True)
    
    def get(self):
        """Retrieve the current value from the entry field"""
        return self.entry.get()


app = customtkinter.CTk()
app.geometry("400x200")

# Using the custom widget
widget = CTkLabeledEntry(app, "Name:", "Enter your name")
widget.pack(pady=20, padx=20, fill="x")

app.mainloop()
```

#### How It Works

This example creates a reusable `CTkLabeledEntry` component that combines a label with an entry field. Instead of repeating this pattern throughout your application, you create it once and can use it anywhere. The component automatically handles layout (label above entry) and provides a simple `get()` method to retrieve the user's input. This reduces code duplication and makes your application easier to maintain.

---

## Configuration & Preferences

Most applications need to remember user preferences and settings between sessions. By persisting configuration to a JSON file, you can reload settings when the application starts. This provides a seamless user experience where their customizations persist across runs.

### Saving and Loading Settings

```python
import customtkinter
import json
import os


class AppConfig:
    """Manages application configuration with JSON persistence"""
    
    def __init__(self, file="config.json"):
        self.file = file
        self.config = self.load()
    
    def load(self):
        """Load configuration from JSON file or use defaults"""
        if os.path.exists(self.file):
            try:
                with open(self.file) as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading config: {e}")
        # Return default configuration if file doesn't exist
        return {
            "theme": "blue",
            "appearance_mode": "System",
            "window_size": "800x600"
        }
    
    def save(self):
        """Save configuration to JSON file"""
        with open(self.file, 'w') as f:
            json.dump(self.config, f, indent=2)


# Usage example
config = AppConfig()
config.config["theme"] = "dark-blue"
config.config["appearance_mode"] = "dark"
config.save()  # Persist to disk

print(config.config)  # Retrieve settings
```

#### How It Works

The `AppConfig` class provides a simple way to manage application settings. On initialization, it tries to load existing configuration from a JSON file. If the file doesn't exist, it uses sensible defaults. You can modify the configuration dictionary at runtime and call `save()` to persist changes to disk. This allows users' preferences to survive application restarts.

---

## Threading & Long Operations

Long-running operations (like file downloads, database queries, or heavy computations) can freeze your UI if they run on the main thread. Threading allows these operations to run in the background while keeping your UI responsive. However, you must update the UI from the main thread, so we use a callback pattern to communicate results.

### Running Background Tasks

```python
import customtkinter
import threading
import time


class BackgroundTask:
    """Helper class for running functions in background threads"""
    
    def __init__(self, callback=None):
        self.callback = callback
    
    def run(self, func, *args):
        """Execute function in daemon thread, call callback when complete"""
        thread = threading.Thread(
            target=lambda: self._worker(func, args),
            daemon=True
        )
        thread.start()
    
    def _worker(self, func, args):
        """Worker method that executes the function and handles results"""
        try:
            result = func(*args)
            if self.callback:
                # Callback runs with the result
                self.callback(result)
        except Exception as e:
            if self.callback:
                # Error passed to callback for handling
                self.callback(f"Error: {str(e)}")


class TaskApp(customtkinter.CTk):
    """Example application with background task support"""
    
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        # Initialize background task handler
        self.task = BackgroundTask(self.on_complete)
        
        # Status label
        self.label = customtkinter.CTkLabel(
            self,
            text="Ready to start",
            font=("Arial", 14)
        )
        self.label.pack(pady=20)
        
        # Start button
        btn = customtkinter.CTkButton(
            self,
            text="Start Long Operation",
            command=self.start
        )
        btn.pack(pady=10)
    
    def start(self):
        """Initiate background task"""
        self.label.configure(text="Processing... please wait")
        # Run long operation in background
        self.task.run(self.long_operation)
    
    def long_operation(self):
        """Simulated long-running operation"""
        time.sleep(3)  # Simulate work
        return "Operation completed successfully!"
    
    def on_complete(self, result):
        """Called when background task finishes"""
        self.label.configure(text=result)


if __name__ == "__main__":
    app = TaskApp()
    app.mainloop()
```

#### How It Works

The `BackgroundTask` class provides a thread-safe way to run long operations without freezing the UI. When you call `run()`, it executes your function in a daemon thread. Once the function completes, it calls the callback function with the result. This callback runs in the main thread, making it safe to update UI elements. The example shows a simple task that takes 3 seconds to complete—during that time, the UI remains responsive.

---

## Common Gotchas & Solutions

These are patterns that commonly catch new CustomTkinter developers. Understanding these will save you hours of debugging.

### 1. Lambda Closure in Loops

**Problem:** When using lambda functions in loops, the variable gets captured by reference, not by value. All lambdas end up using the final value of the variable.

```python
# ❌ WRONG - all buttons will print 4 (the final value)
for i in range(5):
    btn = customtkinter.CTkButton(
        app,
        text=f"Button {i}",
        command=lambda: print(f"Clicked: {i}")
    )

# ✅ CORRECT - use default argument to capture value
for i in range(5):
    btn = customtkinter.CTkButton(
        app,
        text=f"Button {i}",
        command=lambda x=i: print(f"Clicked: {x}")
    )
```

#### Why This Works

The default argument `x=i` captures the current value of `i` when the lambda is created. Without it, the lambda captures `i` by reference and looks up its value when called, which is always the final loop value.

---

### 2. Image Garbage Collection

**Problem:** PhotoImage objects are garbage collected even if they're still being used by a widget. This causes images to disappear from your UI.

```python
# ❌ WRONG - image gets garbage collected
def setup_ui(self):
    image = customtkinter.CTkImage(
        light_image=Image.open("light.png")
    )
    label = customtkinter.CTkLabel(self, image=image)
    label.pack()
    # Image reference is lost here!

# ✅ CORRECT - store reference to prevent garbage collection
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.images = {}  # Keep strong references
    
    def setup_ui(self):
        self.images["logo"] = customtkinter.CTkImage(
            light_image=Image.open("light.png")
        )
        label = customtkinter.CTkLabel(self, image=self.images["logo"])
        label.pack()
```

#### Why This Works

By storing image references in an instance variable (dictionary), you keep the image alive as long as the application is running. Without this reference, Python's garbage collector might clean up the image while it's still being displayed.

---

### 3. Theme-Aware Colors

**Problem:** CustomTkinter supports both light and dark themes. If you specify a single color, it won't adapt when the theme changes.

```python
# ❌ WRONG - ignores theme changes
label = customtkinter.CTkLabel(
    app,
    text="Hello",
    fg_color="white"  # Always white, looks bad in light theme
)

# ✅ CORRECT - tuple for light/dark modes
label = customtkinter.CTkLabel(
    app,
    text="Hello",
    fg_color=("white", "gray20")  # White in light mode, dark gray in dark mode
)
```

#### Why This Works

CustomTkinter color parameters accept tuples where the first value is for light mode and the second is for dark mode. This ensures your colors look good regardless of which theme the user selects.

---

### 4. Grid Layout Not Expanding

**Problem:** Widgets placed with grid don't expand to fill available space, making your layout look cramped.

```python
# ❌ WRONG - widgets don't expand
frame = customtkinter.CTkFrame(app)
frame.grid(row=0, column=0)

# ✅ CORRECT - configure rows/columns to expand
app.grid_rowconfigure(0, weight=1)     # Row 0 expands vertically
app.grid_columnconfigure(0, weight=1)  # Column 0 expands horizontally

frame = customtkinter.CTkFrame(app)
frame.grid(row=0, column=0, sticky="nsew")  # Stretch to all edges
```

#### Why This Works

The `weight` parameter tells grid which rows and columns should expand when extra space is available. The `sticky="nsew"` parameter tells the widget to stretch to the North, South, East, and West edges of its grid cell.

---

### 5. Entry Widget Focus Issues

**Problem:** Sometimes calling `entry.focus()` immediately after creating an entry widget doesn't work because the widget isn't fully initialized yet.

```python
# ❌ WRONG - focus may not work
entry = customtkinter.CTkEntry(app, placeholder_text="Enter text")
entry.pack()
entry.focus()  # Might not work

# ✅ CORRECT - use after() to delay focus
entry = customtkinter.CTkEntry(app, placeholder_text="Enter text")
entry.pack()
app.after(100, entry.focus)  # Wait for widget to initialize
```

#### Why This Works

The `after()` method schedules the focus call for later, giving the widget time to fully initialize. A 100ms delay is usually sufficient, but you can adjust based on your needs.

---

## Summary

CustomTkinter provides a complete toolkit for building modern desktop applications with Python. Key takeaways:

✅ Modern, customizable widgets  
✅ Light/dark mode support  
✅ Consistent cross-platform appearance  
✅ Grid, pack, and place layout options  
✅ Event handling and callbacks  
✅ Full customization via colors, fonts, and parameters  
✅ Responsive design capabilities  
✅ Custom widget composition  
✅ Thread support for long operations  
✅ Configuration persistence  

For more information, visit: <https://customtkinter.tomschimansky.com/documentation/>

---

**Documentation created and expanded: February 16, 2026**
