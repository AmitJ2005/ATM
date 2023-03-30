import tkinter as tk

class ATM:
    def __init__(self, master):
        self.master = master
        self.pin = "1234"
        self.balance = 0
        self.create_widgets()

    def create_widgets(self):
        self.pin_label = tk.Label(self.master, text="Enter PIN:")
        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_button = tk.Button(self.master, text="Enter", command=self.check_pin)

        self.amount_label = tk.Label(self.master, text="Enter amount:")
        self.amount_entry = tk.Entry(self.master)
        self.amount_button = tk.Button(self.master, text="Enter", command=self.perform_operation, state="disabled")

        self.message_label = tk.Label(self.master, text="")
        self.menu_frame = tk.Frame(self.master)

        self.deposit_button = tk.Button(self.menu_frame, text="Deposit", command=lambda: self.set_operation("deposit"))
        self.withdraw_button = tk.Button(self.menu_frame, text="Withdraw", command=lambda: self.set_operation("withdraw"))
        self.balance_button = tk.Button(self.menu_frame, text="Check Balance", command=self.check_balance)

        self.pin_label.pack()
        self.pin_entry.pack()
        self.pin_button.pack()

        self.amount_label.pack()
        self.amount_entry.pack()
        self.amount_button.pack()

        self.message_label.pack()
        self.menu_frame.pack()

        self.deposit_button.pack(side="left")
        self.withdraw_button.pack(side="left")
        self.balance_button.pack(side="left")

    def check_pin(self):
        if self.pin_entry.get() == self.pin:
            self.message_label.config(text="PIN correct")
            self.amount_button.config(state="normal")
            return True
        else:
            self.message_label.config(text="Invalid PIN")
            return False

    def set_operation(self, operation):
        self.operation = operation
        self.message_label.config(text="")
        self.amount_button.config(state="normal")

    def perform_operation(self):
        if not self.check_pin():
            return

        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            self.message_label.config(text="Invalid amount")
            return

        if amount <= 0:
            self.message_label.config(text="Amount must be positive")
            return

        if self.operation == "deposit":
            self.balance += amount
            self.message_label.config(text="Deposit successful")
        elif self.operation == "withdraw":
            if amount > self.balance:
                self.message_label.config(text="Insufficient balance")
            else:
                self.balance -= amount
                self.message_label.config(text="Withdrawal successful")

        self.amount_entry.delete(0, tk.END)
        self.amount_button.config(state="disabled")

    def check_balance(self):
        if self.check_pin():
            self.message_label.config(text=f"Balance: {self.balance:.2f}")

root = tk.Tk()
my_atm = ATM(root)
root.mainloop()
