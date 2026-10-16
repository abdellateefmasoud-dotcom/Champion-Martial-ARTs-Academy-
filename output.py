import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser


# =========================================================
# COLORS - MODERN FITNESS UI
# =========================================================

BG = "#F3F5F7"
WHITE = "#FFFFFF"
NAVY = "#172B4D"
NAVY_LIGHT = "#243B5A"
RED = "#E63946"
RED_DARK = "#C92F3B"
GOLD = "#F4B942"
BLUE = "#2F80ED"
GREEN = "#27AE60"
PURPLE = "#8E5CF6"
TEXT = "#263238"
MUTED = "#6B7785"
BORDER = "#DDE3E8"
LIGHT_BLUE = "#EAF3FF"
LIGHT_RED = "#FFF0F1"
LIGHT_GREEN = "#EAF8F0"
LIGHT_GOLD = "#FFF7E3"


# =========================================================
# COST CONSTANTS
# =========================================================

TRAINING_FEES = {
    "Beginner": 250.00,
    "Intermediate": 300.00,
    "Elite": 350.00
}

PRIVATE_COACHING_RATE = 100.00
COMPETITION_FEE = 220.00
WEEKS_PER_MONTH = 4
MAX_PRIVATE_HOURS = 5.0


# =========================================================
# WEIGHT CATEGORY LIMITS
# =========================================================

WEIGHT_LIMITS = {
    "Flyweight": 66,
    "Lightweight": 73,
    "Light-Middleweight": 81,
    "Middleweight": 90,
    "Light-Heavyweight": 100,
    "Heavyweight": None
}


# =========================================================
# TRAINING LINKS
# =========================================================

TRAINING_LINKS = {
    "Boxing Training":
        "https://www.youtube.com/results?search_query=boxing+training+for+beginners",
    "Leg Workout":
        "https://www.youtube.com/results?search_query=leg+workout+for+athletes",
    "Strength Training":
        "https://www.youtube.com/results?search_query=strength+training+for+martial+artists",
    "Flexibility":
        "https://www.youtube.com/results?search_query=flexibility+training+for+martial+artists",
    "Cardio":
        "https://www.youtube.com/results?search_query=cardio+training+for+athletes",
    "Martial Arts Training":
        "https://www.youtube.com/results?search_query=martial+arts+training+for+beginners"
}


# =========================================================
# OOP: This class stores the details of each athlete.
# The constructor sets the athlete's information.
# ATHLETE CLASS
# =========================================================

class Athlete:
    def __init__(
        self,
        name,
        training_plan,
        weight,
        weight_category,
        private_hours,
        competitions
    ):
        self.name = name
        self.training_plan = training_plan
        self.weight = weight
        # This is the athlete's selected competition category.
        self.weight_category = weight_category
        self.private_hours = private_hours
        self.competitions = competitions


# =========================================================
# ASSIGN CURRENT WEIGHT CATEGORY
# Procedural: This function returns the current weight category.
# =========================================================

def assign_weight_category(weight):
    """Return the current weight category based on the athlete's weight."""
    if weight <= 66:
        return "Flyweight"
    elif weight <= 73:
        return "Lightweight"
    elif weight <= 81:
        return "Light-Middleweight"
    elif weight <= 90:
        return "Middleweight"
    elif weight <= 100:
        return "Light-Heavyweight"
    return "Heavyweight"


# =========================================================
# Procedureal: This function calculates the monthly costs
# CALCULATE COSTS
# =========================================================

def calculate_costs(athlete):
    """Calculate monthly costs. A month is treated as four weeks."""
    training_cost = TRAINING_FEES[athlete.training_plan] * WEEKS_PER_MONTH
    private_cost = (
        athlete.private_hours * PRIVATE_COACHING_RATE * WEEKS_PER_MONTH
    )
    competition_cost = athlete.competitions * COMPETITION_FEE
    total_cost = training_cost + private_cost + competition_cost

    return training_cost, private_cost, competition_cost, total_cost


# =========================================================
# WEIGHT COMPARISON
# Procedural: This function compares the athlete's weight 
# with the selected co,mpetition category.
# =========================================================

def weight_comparison(athlete):
    """Compare the athlete's current weight with the selected competition category."""
    category = athlete.weight_category
    upper_limit = WEIGHT_LIMITS[category]

    if upper_limit is None:
        return "Heavyweight has no upper weight limit."

    difference = upper_limit - athlete.weight

    if difference > 0:
        return (
            f"Within the {category} limit. "
            f"{difference:.2f} kg below the upper limit."
        )
    elif difference == 0:
        return f"At the upper limit of {category}."
    else:
        return (
            f"{abs(difference):.2f} kg above the "
            f"{category} upper limit."
        )


# =========================================================
# MAIN APPLICATION
# OOP: This class manager the application window and its features.
# =========================================================

class MartialArtsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Champion Martial Arts Academy")
        self.root.geometry("1050x800")
        self.root.minsize(900, 700)
        self.root.configure(bg=BG)

        self.athletes = []
        self.setup_styles()
        self.create_gui()

    # =====================================================
    # STYLE
    # =====================================================

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
             "Modern.TCombobox",
            fieldbackground=WHITE,
            background=WHITE,
            foreground=TEXT,
            bordercolor=BORDER,
            lightcolor=WHITE,
            darkcolor=WHITE,
            arrowcolor=NAVY,
            padding=8
        )
        style.map(
            "Modern.TCombobox",
            fieldbackground=[("readonly", WHITE)],
            foreground=[("readonly", TEXT)]
        )

    # =====================================================
    # LOGO
    # =====================================================

    def create_logo(self, parent, size=90):
        canvas = tk.Canvas(
            parent,
            width=size,
            height=size,
            bg=parent.cget("bg"),
            highlightthickness=0
        )
        center = size // 2

        canvas.create_oval(
            8, 8, size - 8, size - 8,
            fill=WHITE, outline=RED, width=4
        )
        canvas.create_oval(
            18, 18, size - 18, size - 18,
            outline=NAVY, width=2
        )
        canvas.create_oval(
            center - 5, center - 25, center + 5, center - 15,
            fill=RED, outline=RED
        )
        canvas.create_line(
            center, center - 15, center - 5, center + 5,
            fill=NAVY, width=5
        )
        canvas.create_line(
            center - 4, center - 5, center - 20, center + 5,
            fill=NAVY, width=4
        )
        canvas.create_line(
            center - 4, center - 5, center + 17, center - 13,
            fill=NAVY, width=4
        )
        canvas.create_line(
            center - 5, center + 5, center - 20, center + 23,
            fill=RED, width=5
        )
        canvas.create_line(
            center - 5, center + 5, center + 17, center + 17,
            fill=RED, width=5
        )
        return canvas

    # =====================================================
    # MAIN GUI
    # =====================================================

    def create_gui(self):
        header = tk.Frame(self.root, bg=NAVY, height=115)
        header.pack(fill="x")
        header.pack_propagate(False)

        self.create_logo(header, 82).pack(
            side="left", padx=(28, 12), pady=15
        )

        title_frame = tk.Frame(header, bg=NAVY)
        title_frame.pack(side="left")

        tk.Label(
            title_frame, text="CHAMPION", bg=NAVY, fg=WHITE,
            font=("Arial", 27, "bold")
        ).pack(anchor="w")
        tk.Label(
            title_frame, text="MARTIAL ARTS ACADEMY", bg=NAVY, fg=RED,
            font=("Arial", 13, "bold")
        ).pack(anchor="w")
        tk.Label(
            title_frame, text="Discipline  •  Strength  •  Progress",
            bg=NAVY, fg="#B8C4D2", font=("Arial", 9)
        ).pack(anchor="w", pady=(3, 0))

        display_frame = tk.Frame(header, bg=NAVY)
        display_frame.pack(side="right", padx=30)
        tk.Label(
            display_frame, text="ATHLETE", bg=NAVY, fg=WHITE,
            font=("Arial", 16, "bold")
        ).pack()
        tk.Label(
            display_frame, text="DISPLAY", bg=NAVY, fg=RED,
            font=("Arial", 11, "bold")
        ).pack()

        main = tk.Frame(self.root, bg=BG)
        main.pack(fill="both", expand=True, padx=25, pady=20)

        # Athlete details card
        details = tk.Frame(
            main, bg=WHITE,
            highlightbackground=BORDER, highlightthickness=1
        )
        details.pack(fill="x", pady=(0, 15))

        section_title = tk.Frame(details, bg=WHITE)
        section_title.pack(fill="x", padx=20, pady=(15, 5))
        tk.Label(
            section_title, text="Athlete Details", bg=WHITE, fg=NAVY,
            font=("Arial", 15, "bold")
        ).pack(side="left")
        tk.Label(
            section_title, text="Enter athlete information below",
            bg=WHITE, fg=MUTED, font=("Arial", 9)
        ).pack(side="right")

        input_frame = tk.Frame(details, bg=WHITE)
        input_frame.pack(fill="x", padx=20, pady=5)
        input_frame.columnconfigure(1, weight=1)
        input_frame.columnconfigure(3, weight=1)

        # Row 0: Name and training plan
        self.create_field_label(input_frame, "Athlete Name", 0, 0)
        self.name_entry = self.create_entry(input_frame, 0, 1)

        self.create_field_label(input_frame, "Training Plan", 0, 2)
        self.plan_combo = ttk.Combobox(
            input_frame,
            values=list(TRAINING_FEES.keys()),
            state="readonly",
            style="Modern.TCombobox",
            font=("Arial", 10)
        )
        self.plan_combo.current(0)
        self.plan_combo.grid(
            row=0, column=3, sticky="ew",
            padx=(10, 15), pady=6
        )
    #==================================================
    # Event-driven: update the competition message when the user 
    # selects a different traning plan.
    #==================================================
        self.plan_combo.bind(
            "<<ComboboxSelected>>", self.update_competition_rule
        )

        # Row 1: Current weight and automatically assigned category
        self.create_field_label(input_frame, "Current Weight (kg)", 1, 0)
        self.weight_entry = self.create_entry(input_frame, 1, 1)
        self.weight_entry.bind("<KeyRelease>", self.update_category)
        self.weight_entry.bind("<FocusOut>", self.update_category)

        self.create_field_label(input_frame, "Current Weight Category", 1, 2)
        self.category_label = tk.Label(
            input_frame,
            text="Enter weight",
            bg="#F7F9FA",
            fg=MUTED,
            font=("Arial", 10, "bold"),
            anchor="w",
            padx=12,
            pady=9
        )
        self.category_label.grid(
            row=1, column=3, sticky="ew",
            padx=(10, 15), pady=6
        )
    #================================================
    # Row 2: Competition category and competitions
    #================================================
        self.create_field_label(input_frame, "Competition Weight Category", 2, 0)
        self.competition_category_combo = ttk.Combobox(
            input_frame,
            values=list(WEIGHT_LIMITS.keys()),
            state="readonly",
            style="Modern.TCombobox",
            font=("Arial", 10)
        )
        self.competition_category_combo.grid(
            row=2, column=1, sticky="ew",
            padx=(10, 15), pady=6
        )
        self.competition_category_combo.set("")

        self.create_field_label(input_frame, "Competitions This Month", 2, 2)
        self.competitions_entry = self.create_entry(input_frame, 2, 3)

        # Row 3: Private coaching hours
        self.create_field_label(
            input_frame, "Private Coaching (hours/week)", 3, 0
        )
        self.private_hours_entry = self.create_entry(input_frame, 3, 1)

        self.competition_rule_label = tk.Label(
            input_frame,
            text="Beginner athletes cannot enter competitions.",
            bg=WHITE, fg=MUTED, font=("Arial", 9)
        )
        self.competition_rule_label.grid(
            row=3, column=2, columnspan=2,
            sticky="w", padx=(10, 15), pady=6
        )
    #================================================
    # Buttons
    # Event-driven: Each button calls a function when the user clicks it.
    # These buttons register athletes, calculate costs, clear fields,
    # and open traning resources.
    #================================================
        buttons = tk.Frame(details, bg=WHITE)
        buttons.pack(pady=(10, 18))

        self.create_button(
            buttons, "REGISTER ATHLETE", RED, self.register_athlete
        ).pack(side="left", padx=5)
        self.create_button(
            buttons, "CALCULATE COST", GOLD, self.calculate_selected, dark=True
        ).pack(side="left", padx=5)
        self.create_button(
            buttons, "CLEAR", "#687684", self.clear_fields
        ).pack(side="left", padx=5)
        self.create_button(
            buttons, "EXERCISE & TRAINING", BLUE, self.open_training_resources
        ).pack(side="left", padx=5)

        # Registered athletes
        athletes_card = tk.Frame(
            main, bg=WHITE,
            highlightbackground=BORDER, highlightthickness=1
        )
        athletes_card.pack(fill="both", expand=True)

        title = tk.Frame(athletes_card, bg=WHITE)
        title.pack(fill="x", padx=20, pady=(15, 8))
        tk.Label(
            title, text="Registered Athletes", bg=WHITE, fg=NAVY,
            font=("Arial", 15, "bold")
        ).pack(side="left")
        tk.Label(
            title, text="Select an athlete to view details",
            bg=WHITE, fg=MUTED, font=("Arial", 9)
        ).pack(side="right")

        list_container = tk.Frame(athletes_card, bg=WHITE)
        list_container.pack(fill="both", expand=True, padx=18, pady=5)

        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side="right", fill="y")

        self.athlete_list = tk.Listbox(
            list_container,
            bg="#F8FAFB",
            fg=TEXT,
            selectbackground=NAVY,
            selectforeground=WHITE,
            font=("Arial", 10),
            activestyle="none",
            bd=0,
            highlightbackground=BORDER,
            highlightthickness=1,
            yscrollcommand=scrollbar.set
        )
        self.athlete_list.pack(fill="both", expand=True)
        scrollbar.config(command=self.athlete_list.yview)
    #=======================================================
    # Event-driven: Load athlete details when the user selects an athlete.
    #=======================================================
        self.athlete_list.bind("<<ListboxSelect>>", self.load_athlete)

        tk.Label(
            self.root,
            text="Champion Martial Arts Academy  •  Athlete Management System",
            bg=BG, fg=MUTED, font=("Arial", 8)
        ).pack(pady=(0, 10))

    # =====================================================
    # FIELD HELPERS
    # =====================================================

    def create_field_label(self, parent, text, row, column):
        tk.Label(
            parent, text=text, bg=WHITE, fg=TEXT,
            font=("Arial", 9, "bold"), anchor="w"
        ).grid(
            row=row, column=column, sticky="w",
            padx=(5, 5), pady=6
        )

    def create_entry(self, parent, row, column):
        entry = tk.Entry(
            parent,
            bg="#F8FAFB",
            fg=TEXT,
            insertbackground=NAVY,
            font=("Arial", 10),
            relief="solid",
            bd=1
        )
        entry.grid(
            row=row, column=column, sticky="ew",
            padx=(10, 15), pady=6, ipady=7
        )
        return entry

    def create_button(self, parent, text, color, command, dark=False):
        return tk.Button(
            parent,
            text=text,
            bg=color,
            fg="#222222" if dark else WHITE,
            activebackground=color,
            activeforeground="#222222" if dark else WHITE,
            font=("Arial", 9, "bold"),
            relief="flat",
            bd=0,
            padx=18,
            pady=10,
            cursor="hand2",
            command=command
        )

    # =====================================================
    # UPDATE CURRENT CATEGORY
    # =====================================================

    def update_category(self, event=None):
        try:
            weight = float(self.weight_entry.get())
            if weight <= 0:
                raise ValueError

            category = assign_weight_category(weight)
            self.category_label.config(text=category, fg=NAVY)
        except ValueError:
            self.category_label.config(text="Enter valid weight", fg=MUTED)

    # =====================================================
    # UPDATE COMPETITION RULE MESSAGE
    # =====================================================

    def update_competition_rule(self, event=None):
        if self.plan_combo.get() == "Beginner":
            self.competition_rule_label.config(
                text="Beginner athletes cannot enter competitions.",
                fg=RED_DARK
            )
        else:
            self.competition_rule_label.config(
                text="Intermediate and Elite athletes can compete.",
                fg=GREEN
            )

    # =====================================================
    # REGISTER ATHLETE
    # =====================================================

    def register_athlete(self):
        name = self.name_entry.get().strip()
        training_plan = self.plan_combo.get()
        weight_text = self.weight_entry.get().strip()
        competition_category = self.competition_category_combo.get().strip()
        private_hours_text = self.private_hours_entry.get().strip()
        competitions_text = self.competitions_entry.get().strip()
    #======================================================
    # Validation: Check the athlete's information before registration.
    # Stop registration when the user enters invalid information.
    #======================================================
        if not name:
            messagebox.showerror("Invalid Data", "Please enter athlete name.")
            return
    #======================================================
    # Business rule: Beginner athletes cannt enter competitions.
    #======================================================
        if not training_plan:
            messagebox.showerror("Invalid Data", "Please select a training plan.")
            return

        try:
            weight = float(weight_text)
        except ValueError:
            messagebox.showerror("Invalid Data", "Please enter a valid weight.")
            return

        if weight <= 0:
            messagebox.showerror(
                "Invalid Data", "Weight must be greater than 0."
            )
            return

        if not competition_category:
            messagebox.showerror(
                "Invalid Data",
                "Please select a competition weight category."
            )
            return

        try:
            private_hours = float(private_hours_text)
        except ValueError:
            messagebox.showerror(
                "Invalid Data",
                "Please enter valid private coaching hours per week."
            )
            return

        if private_hours < 0:
            messagebox.showerror(
                "Invalid Data",
                "Private coaching hours cannot be negative."
            )
            return

        if private_hours > MAX_PRIVATE_HOURS:
            messagebox.showerror(
                "Invalid Data",
                f"Maximum private coaching is {MAX_PRIVATE_HOURS:.0f} hours per week."
            )
            return

        try:
            competitions = int(competitions_text)
        except ValueError:
            messagebox.showerror(
                "Invalid Data",
                "Enter the number of competitions as a whole number (for example, 0)."
            )
            return

        if competitions < 0:
            messagebox.showerror(
                "Invalid Data", "Competitions cannot be negative."
            )
            return

        # Only Intermediate and Elite athletes can enter competitions.
        if training_plan == "Beginner" and competitions > 0:
            messagebox.showerror(
                "Competition Not Allowed",
                "Beginner athletes cannot enter competitions. "
                "Please select Intermediate or Elite, or enter 0 competitions."
            )
            return

        athlete = Athlete(
            name,
            training_plan,
            weight,
            competition_category,
            private_hours,
            competitions
        )

        self.athletes.append(athlete)
        current_category = assign_weight_category(weight)

        self.athlete_list.insert(
            tk.END,
            f"{athlete.name} | {athlete.training_plan} | "
            f"{athlete.weight:.2f} kg | Current: {current_category} | "
            f"Competition: {athlete.weight_category} | "
            f"Competitions: {athlete.competitions}"
        )

        new_index = len(self.athletes) - 1
        self.athlete_list.selection_clear(0, tk.END)
        self.athlete_list.selection_set(new_index)
        self.athlete_list.activate(new_index)
        self.athlete_list.see(new_index)

        messagebox.showinfo(
            "Registration Complete",
            "Athlete registered successfully!"
        )

    # =====================================================
    # LOAD SELECTED ATHLETE INTO FIELDS
    # =====================================================

    def load_athlete(self, event=None):
        selected = self.athlete_list.curselection()
        if not selected:
            return

        athlete = self.athletes[selected[0]]

        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.private_hours_entry.delete(0, tk.END)
        self.competitions_entry.delete(0, tk.END)

        self.name_entry.insert(0, athlete.name)
        self.plan_combo.set(athlete.training_plan)
        self.weight_entry.insert(0, str(athlete.weight))
        self.private_hours_entry.insert(0, str(athlete.private_hours))
        self.competitions_entry.insert(0, str(athlete.competitions))
        self.competition_category_combo.set(athlete.weight_category)

        current_category = assign_weight_category(athlete.weight)
        self.category_label.config(text=current_category, fg=NAVY)
        self.update_competition_rule()

    # =====================================================
    # CALCULATE SELECTED ATHLETE
    # =====================================================

    def calculate_selected(self):
        selection = self.athlete_list.curselection()
        if not selection:
            messagebox.showwarning(
                "Select Athlete",
                "Please select an athlete from the list first."
            )
            return

        athlete = self.athletes[selection[0]]
        training_cost, private_cost, competition_cost, total_cost = (
            calculate_costs(athlete)
        )
        comparison = weight_comparison(athlete)

        self.open_cost_window(
            athlete,
            training_cost,
            private_cost,
            competition_cost,
            total_cost,
            comparison
        )

    # =====================================================
    # MONTHLY COST WINDOW
    # =====================================================

    def open_cost_window(
        self,
        athlete,
        training_cost,
        private_cost,
        competition_cost,
        total_cost,
        comparison
    ):
        window = tk.Toplevel(self.root)
        window.title("Monthly Cost Summary")
        window.geometry("720x650")
        window.minsize(650, 600)
        window.configure(bg=BG)

        header = tk.Frame(window, bg=NAVY, height=95)
        header.pack(fill="x")
        header.pack_propagate(False)

        self.create_logo(header, 65).pack(
            side="left", padx=(25, 12), pady=15
        )

        title_box = tk.Frame(header, bg=NAVY)
        title_box.pack(side="left")

        tk.Label(
            title_box, text="MONTHLY COST SUMMARY", bg=NAVY, fg=WHITE,
            font=("Arial", 18, "bold")
        ).pack(anchor="w")
        tk.Label(
            title_box, text=athlete.name, bg=NAVY, fg=GOLD,
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        card = tk.Frame(
            window, bg=WHITE,
            highlightbackground=BORDER, highlightthickness=1
        )
        card.pack(fill="both", expand=True, padx=25, pady=20)

        self.summary_row(card, "Training Plan", athlete.training_plan)
        self.summary_row(card, "Current Weight", f"{athlete.weight:.2f} kg")
        self.summary_row(
            card, "Current Weight Category",
            assign_weight_category(athlete.weight)
        )
        self.summary_row(
            card, "Competition Weight Category", athlete.weight_category
        )

        tk.Frame(card, bg=BORDER, height=1).pack(
            fill="x", padx=25, pady=10
        )

        self.summary_row(card, "Training Fee", f"{training_cost:.2f} AED")
        self.summary_row(card, "Competition Fee", f"{competition_cost:.2f} AED")
        self.summary_row(card, "Private Coaching", f"{private_cost:.2f} AED")

        total_card = tk.Frame(
            card, bg=LIGHT_GOLD,
            highlightbackground=GOLD, highlightthickness=1
        )
        total_card.pack(fill="x", padx=25, pady=15)

        tk.Label(
            total_card, text="TOTAL MONTHLY COST", bg=LIGHT_GOLD, fg=NAVY,
            font=("Arial", 10, "bold")
        ).pack(pady=(10, 2))
        tk.Label(
            total_card, text=f"{total_cost:.2f} AED", bg=LIGHT_GOLD, fg=NAVY,
            font=("Arial", 23, "bold")
        ).pack(pady=(0, 10))

        weight_card = tk.Frame(
            card, bg=LIGHT_GREEN,
            highlightbackground=GREEN, highlightthickness=1
        )
        weight_card.pack(fill="x", padx=25, pady=(0, 15))

        tk.Label(
            weight_card, text="WEIGHT COMPARISON", bg=LIGHT_GREEN, fg=NAVY,
            font=("Arial", 10, "bold")
        ).pack(anchor="w", padx=15, pady=(10, 3))
        tk.Label(
            weight_card, text=comparison, bg=LIGHT_GREEN, fg=GREEN,
            font=("Arial", 9), justify="left", wraplength=600
        ).pack(anchor="w", padx=15, pady=(0, 10))

        tk.Button(
            window, text="Close", bg=NAVY, fg=WHITE,
            activebackground=NAVY_LIGHT, activeforeground=WHITE,
            font=("Arial", 10, "bold"), relief="flat", bd=0,
            padx=35, pady=9, cursor="hand2", command=window.destroy
        ).pack(pady=(0, 20))

    # =====================================================
    # SUMMARY ROW
    # =====================================================

    def summary_row(self, parent, label, value):
        row = tk.Frame(parent, bg=WHITE)
        row.pack(fill="x", padx=25, pady=5)

        tk.Label(
            row, text=label, bg=WHITE, fg=MUTED,
            font=("Arial", 9)
        ).pack(side="left")
        tk.Label(
            row, text=value, bg=WHITE, fg=TEXT,
            font=("Arial", 10, "bold")
        ).pack(side="right")

    # =====================================================
    # TRAINING RESOURCES
    # =====================================================

    def open_training_resources(self):
        window = tk.Toplevel(self.root)
        window.title("Training Resources")
        window.geometry("850x650")
        window.minsize(750, 580)
        window.configure(bg=BG)

        header = tk.Frame(
            window, bg=WHITE, height=105,
            highlightbackground=BORDER, highlightthickness=1
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        self.create_logo(header, 72).pack(
            side="left", padx=(25, 15), pady=15
        )

        title_box = tk.Frame(header, bg=WHITE)
        title_box.pack(side="left")

        tk.Label(
            title_box, text="Training Resources", bg=WHITE, fg=NAVY,
            font=("Arial", 20, "bold")
        ).pack(anchor="w")
        tk.Label(
            title_box, text="Exercise and training resources",
            bg=WHITE, fg=MUTED, font=("Arial", 10)
        ).pack(anchor="w")

        container = tk.Frame(window, bg=BG)
        container.pack(fill="both", expand=True, padx=25, pady=20)
        # Additional feature: Provide training resources for athletes.
        # Users can choose a topic and open related YouTube search results.
        resources = [
            (
                "Boxing Training",
                "Improve punching, footwork and boxing technique.",
                RED, LIGHT_RED
            ),
            (
                "Leg Workout",
                "Build stronger legs and improve lower-body power.",
                GREEN, LIGHT_GREEN
            ),
            (
                "Strength Training",
                "Develop strength and physical performance.",
                BLUE, LIGHT_BLUE
            ),
            (
                "Flexibility",
                "Improve mobility, stretching and range of motion.",
                PURPLE, "#F3EDFF"
            ),
            (
                "Cardio",
                "Improve endurance and cardiovascular fitness.",
                "#168AAD", "#E8F8FC"
            ),
            (
                "Martial Arts Training",
                "Explore martial arts techniques and training sessions.",
                GOLD, LIGHT_GOLD
            )
        ]

        for column in range(3):
            container.columnconfigure(column, weight=1)
        for row in range(2):
            container.rowconfigure(row, weight=1)

        for index, (name, description, color, light_color) in enumerate(resources):
            row = index // 3
            column = index % 3

            card = tk.Frame(
                container, bg=WHITE,
                highlightbackground=BORDER, highlightthickness=1
            )
            card.grid(
                row=row, column=column,
                padx=8, pady=8, sticky="nsew"
            )

            tk.Frame(card, bg=color, height=5).pack(fill="x")
            tk.Label(
                card, text="●", bg=light_color, fg=color,
                font=("Arial", 25, "bold"), width=3, height=1
            ).pack(pady=(18, 8))
            tk.Label(
                card, text=name, bg=WHITE, fg=NAVY,
                font=("Arial", 11, "bold")
            ).pack(pady=3)
            tk.Label(
                card, text=description, bg=WHITE, fg=MUTED,
                font=("Arial", 8), wraplength=210, justify="center"
            ).pack(padx=15, pady=7)

            tk.Button(
                card,
                text="VIEW EXERCISES →",
                bg=color,
                fg="#603434" if color == GOLD else WHITE,
                activebackground=color,
                activeforeground="#643B3B" if color == GOLD else WHITE,
                font=("Arial", 8, "bold"),
                relief="flat", bd=0, padx=15, pady=8,
                cursor="hand2",
                command=lambda n=name: self.open_training_link(n)
            ).pack(pady=(8, 18))

        tk.Button(
            window, text="Close", bg=NAVY, fg=WHITE,
            activebackground=NAVY_LIGHT, activeforeground=WHITE,
            font=("Arial", 9, "bold"), relief="flat", bd=0,
            padx=30, pady=8, cursor="hand2", command=window.destroy
        ).pack(pady=(0, 18))

    # =====================================================
    # OPEN TRAINING LINK
    # open the selected training resource in a web browser.
    # =====================================================

    def open_training_link(self, name):
        url = TRAINING_LINKS.get(name)
        if not url:
            messagebox.showerror("Error", "Training link not found.")
            return

        try:
            opened = webbrowser.open_new_tab(url)
            if not opened:
                messagebox.showinfo(
                    "Training Resource",
                    "Please open your web browser to view the exercises."
                )
        except Exception as error:
            messagebox.showerror(
                "Browser Error",
                f"Could not open the training link.\n\n{error}"
            )

    # =====================================================
    # CLEAR FIELDS
    # =====================================================

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.weight_entry.delete(0, tk.END)
        self.private_hours_entry.delete(0, tk.END)
        self.competitions_entry.delete(0, tk.END)

        self.plan_combo.current(0)
        self.competition_category_combo.set("")
        self.category_label.config(text="Enter weight", fg=MUTED)
        self.athlete_list.selection_clear(0, tk.END)
        self.update_competition_rule()


# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = MartialArtsApp(root)
    root.mainloop()