import random
import tkinter as tk

# Class data
classes = {
    "Light": {
        "Specializations": ["Evasive Dash", "Grappling Hook", "Cloaking Device"],
        "Weapons": ["93R", "Dagger", "LH1", "M11", "M26 Matter", "Recurve Bow", "SH1900", "SR-84", "Sword", "Throwing Knives", "V9S", "XP-54"],
        "Gadgets": ["Breach Charge", "Flashbang", "Frag Grenade", "Gas Grenade", "Gateway", "Glitch Grenade", "Goo Grenade", "Pyro Grenade", "Smoke Grenade", "Sonar Grenade", "Stun Gun", "Thermal Bore", "Thermal Vision", "Tracking Dart", "Vanishing Bomb"]
    },
    "Medium": {
        "Specializations": ["Dematerializer", "Guardian Turret", "Healing Beam"],
        "Weapons": ["AKM", "CL-40", "Dual Blades", "Famas", "FCAR", "Model 1887", "Pike-556", "R .357", "Riot Shield"],
        "Gadgets": ["APS Turret", "Data Reshaper", "Defibrillator", "Explosive Mine", "Flashbang", "Frag Grenade", "Gas Grenade", "Gas Mine", "Glitch Trap", "Goo Grenade", "Jump Pad", "Pyro Grenade", "Zipline"]
    },
    "Heavy": {
        "Specializations": ["Charge N Slam", "Goo Gun", "Mesh Shield", "Winch Claw"],
        "Weapons": [".50 Akimbo", "Flamethrower", "KS-23", "Lewis Gun", "M60", "MGL32", "SA1216", "Sledgehammer", "Spear"],
        "Gadgets": ["Anti-Gravity Cube", "Barricade", "C4", "Dome Shield", "Explosive Mine", "Flashbang", "Frag Grenade", "Gas Grenade", "Goo Grenade", "Proximity Sensor", "Pyro Grenade", "Pyro Mine", "RPG-7"]
    }
}

# Set up the GUI
root = tk.Tk()
root.title("Random Class Selector")

# Set dark theme colors
root.configure(bg='#2E2E2E')

# Set fixed size for the window
root.geometry("600x400")
root.resizable(False, False)

def randomize_class():
    # Pick a random class
    chosen_class = random.choice(list(classes.keys()))

    # Pick a random specialization and weapon from that class
    Specializations = random.choice(classes[chosen_class]["Specializations"])
    Weapons = random.choice(classes[chosen_class]["Weapons"])

    if chosen_class == "Medium":
        # Always include Defibrillator and select 2 more unique gadgets
        Gadgets = ["Defibrillator"] + random.sample([gadget for gadget in classes[chosen_class]["Gadgets"] if gadget != "Defibrillator"], 2)
    else:
        # Select 3 unique gadgets from the other classes
        Gadgets = random.sample(classes[chosen_class]["Gadgets"], 3)

    # Update the display
    result_label.config(text=f"Class: {chosen_class}\nSpecialization: {Specializations}\nWeapon: {Weapons}\nGadgets: {', '.join(Gadgets)}")

# Title label
title_label = tk.Label(root, text="Random Class Selector", bg='#2E2E2E', fg='white', font=('Arial', 16, 'bold'))
title_label.pack(pady=10)

# Create a label to display the results
result_label = tk.Label(root, text="", bg='#2E2E2E', fg='white', padx=20, pady=20, font=('Arial', 14), wraplength=560)
result_label.pack(pady=(0, 30))

# Create a standard button for reroll, raised and wider
reroll_button = tk.Button(root, text="Reroll", command=randomize_class, bg='#4B4B4B', fg='white', padx=20, pady=8, font=('Arial', 12, 'bold'), width=15)
reroll_button.pack(pady=(20, 0))  # Adjusted padding to move the button higher

# Initial randomization
randomize_class()

# Start the GUI event loop
root.mainloop()
