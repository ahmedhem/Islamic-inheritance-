import tkinter as tk
from tkinter import ttk

def calculate_fixed_inheritance(heirs, estate_value):
    fixed_inheritance = {}
    fixed_inheritance['husband'] = estate_value * 0.5
    fixed_inheritance['wife'] = estate_value * 0.5
    fixed_inheritance['children'] = estate_value * 0.2 / len(heirs['children'])
    fixed_inheritance['parents'] = estate_value * 0.1 / len(heirs['parents'])
    fixed_inheritance['siblings'] = estate_value * 0.05 / len(heirs['siblings'])
    return fixed_inheritance

def calculate_residuary_inheritance(heirs, estate_value):
    fixed_inheritance = calculate_fixed_inheritance(heirs, estate_value)
    residuary_inheritance = estate_value - sum(fixed_inheritance.values())
    return residuary_inheritance

def calculate():
    heirs = {
        'husband': husband_entry.get(),
        'wife': wife_entry.get(),
        'children': children_entry.get().split(','),
        'parents': parents_entry.get().split(','),
        'siblings': siblings_entry.get().split(','),
        'nieces_and_nephews': nieces_and_nephews_entry.get().split(',')
    }
    estate_value_str = estate_value_entry.get()


    heirs = {k: v for k, v in heirs.items() if v}  # remove empty values
    estate_value = int(estate_value_str)

    fixed_inheritance = calculate_fixed_inheritance(heirs, estate_value)
    residuary_inheritance = calculate_residuary_inheritance(heirs, estate_value)

    treeview.delete(*treeview.get_children())

    for heir, amount in fixed_inheritance.items():
        treeview.insert('', 'end', text=heir, values=(amount))

    treeview.insert('', 'end', text='Residuary Inheritance', values=(residuary_inheritance))

    main_screen.pack_forget()
    results_screen.pack()

def go_back():
    results_screen.pack_forget()
    main_screen.pack()

backgroundColor = "#00b8d4"

window = tk.Tk()
window.title("Inheritance Calculator")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg=backgroundColor)

main_screen = tk.Frame(window, bg=backgroundColor)
main_screen.pack(padx=20, pady=20)

estate_value_label = tk.Label(main_screen, text="Estate Value:", bg=backgroundColor)
estate_value_label.grid(row=0, column=0, sticky="E", pady=5)
estate_value_entry = tk.Entry(main_screen)
estate_value_entry.grid(row=0, column=1)



style = ttk.Style(main_screen)
style.configure('lefttab.TNotebook', tabposition='ws')
heirs_notebook = ttk.Notebook(main_screen, style='lefttab.TNotebook')
heirs_tab1 = ttk.Frame(heirs_notebook)
heirs_tab2 = ttk.Frame(heirs_notebook)
heirs_tab3 = ttk.Frame(heirs_notebook)
heirs_tab4 = ttk.Frame(heirs_notebook)
heirs_tab5 = ttk.Frame(heirs_notebook)
heirs_tab6 = ttk.Frame(heirs_notebook)
heirs_notebook.add(heirs_tab1, text='Husband')
heirs_notebook.add(heirs_tab2, text='Wife')
heirs_notebook.add(heirs_tab3, text='Children')
heirs_notebook.add(heirs_tab4, text='Parents')
heirs_notebook.add(heirs_tab5, text='Siblings')
heirs_notebook.add(heirs_tab6, text='Nieces and Nephews')
heirs_notebook.grid(row=1, column=0, columnspan=2, pady=5)

husband_label = tk.Label(heirs_tab1, text="Name:", bg=backgroundColor)
husband_label.pack(padx=10, pady=10)
husband_entry = tk.Entry(heirs_tab1)
husband_entry.pack(padx=10, pady=10)

wife_label = tk.Label(heirs_tab2, text="Name:", bg=backgroundColor)
wife_label.pack(padx=10, pady=10)
wife_entry = tk.Entry(heirs_tab2)
wife_entry.pack(padx=10, pady=10)


children_label = tk.Label(heirs_tab3, text="Names (comma-separated):", bg=backgroundColor)
children_label.pack(padx=10, pady=10)
children_entry = tk.Entry(heirs_tab3)
children_entry.pack(padx=10, pady=10)

parents_label = tk.Label(heirs_tab4, text="Names (comma-separated):", bg=backgroundColor)
parents_label.pack(padx=10, pady=10)
parents_entry = tk.Entry(heirs_tab4)
parents_entry.pack(padx=10, pady=10)

siblings_label = tk.Label(heirs_tab5, text="Names (comma-separated):", bg=backgroundColor)
siblings_label.pack(padx=10, pady=10)
siblings_entry = tk.Entry(heirs_tab5)
siblings_entry.pack(padx=10, pady=10)

nieces_and_nephews_label = tk.Label(heirs_tab6, text="Names (comma-separated):", bg=backgroundColor)
nieces_and_nephews_label.pack(padx=10, pady=10)
nieces_and_nephews_entry = tk.Entry(heirs_tab6)
nieces_and_nephews_entry.pack(padx=10, pady=10)

calculate_button = tk.Button(main_screen, text="Calculate", command=calculate, bg=backgroundColor, fg='white')
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)



results_screen = tk.Frame(window, bg=backgroundColor)

treeview = ttk.Treeview(results_screen, columns=("Amount"))
treeview.heading("#0", text="Heir")
treeview.heading("Amount", text="Amount")
results_screen.columnconfigure(0, weight=1)
treeview.column("Amount", minwidth=0, width=120)
treeview.grid(row=3, column=0, columnspan=6, pady=10)

back_button = tk.Button(results_screen, text="<< Back", command=go_back, bg=backgroundColor, fg='white')
back_button.grid(row=0, column=0, columnspan=2, pady=10)

main_screen.pack()

window.mainloop()