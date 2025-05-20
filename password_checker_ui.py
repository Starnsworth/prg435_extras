#    Try out TKinter to add a user interface to the password checker

import tkinter
from passwordHash import gen_md5
from passDupeCheck import check_for_duplicates
from passSeqCheck import checkPassSeq
from passLenRules import beginComparison as check_len_rules

root_window = tkinter.Tk()
root_window.title("Password Checker")

# Welcome message
welcome_message = tkinter.Label(root_window, text="Welcome to Password Checker")
welcome_message.grid(row=0, column=0, columnspan=2, pady=(10, 10))

# Checkbox list
select_dupe_check = tkinter.Checkbutton(root_window, text="Duplicate character check", onvalue=1, offvalue=0)
select_dupe_check.grid(row=1, column=0, sticky="w", padx=10, pady=2)

select_length_check = tkinter.Checkbutton(root_window, text="Length check", onvalue=1, offvalue=0)
select_length_check.grid(row=2, column=0, sticky="w", padx=10, pady=2)

select_sequence_check = tkinter.Checkbutton(root_window, text="Check sequential characters", onvalue=1, offvalue=0)
select_sequence_check.grid(row=3, column=0, sticky="w", padx=10, pady=2)

# Outcome areas
dupe_check_outcome = tkinter.Label(root_window, text="")
dupe_check_outcome.grid(row=1, column=1, sticky="w", padx=10)

length_check_outcome = tkinter.Label(root_window, text="")
length_check_outcome.grid(row=2, column=1, sticky="w", padx=10)

sequence_check_outcome = tkinter.Label(root_window, text="")
sequence_check_outcome.grid(row=3, column=1, sticky="w", padx=10)

# Hash area
hash_label = tkinter.Label(root_window, text="Password MD5 Hash: ")
hash_label.grid(row=4, column=0, sticky="w", padx=10, pady=(10, 2))

hash_label_outcome = tkinter.Label(root_window, text="")
hash_label_outcome.grid(row=4, column=1, sticky="w", padx=10, pady=(10, 2))

# Password entry and button
password_entry_field = tkinter.Entry(root_window, width=30)
password_entry_field.grid(row=5, column=0, sticky="w", padx=10, pady=(10, 10))

def on_pass_field_button_click():
    if password_entry_field.get() != "":
        if select_length_check.config()
        update_label(dupe_check_outcome, check_for_duplicates(password_entry_field.get()))

        update_label(length_check_outcome, check_len_rules(password_entry_field.get()))

        update_label(sequence_check_outcome, checkPassSeq(password_entry_field.get()))


        update_label(hash_label_outcome, gen_md5(password_entry_field.get()))
        password_entry_field.delete(0, "end")
    else:
        update_label(hash_label_outcome, "Enter A Password")

password_field_confirm = tkinter.Button(root_window, text="Check Password", command = on_pass_field_button_click)
password_field_confirm.grid(row=5, column=1, sticky="w", padx=10, pady=(10, 10))

# Optional: make columns stretch properly
root_window.grid_columnconfigure(0, weight=1)
root_window.grid_columnconfigure(1, weight=1)



def update_label(label_to_update, new_label_value :str):
    label_to_update.config(text=new_label_value)





root_window.mainloop()