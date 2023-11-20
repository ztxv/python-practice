import tkinter as tk
import time
#11/19/23
def on_button_click():
    start_time = time.time()
    calculation = entry.get()
    try:
        result = eval(calculation)
        result_label.config(text=f"Answer: {result}")

    except Exception as e:
        result_label.config(text=f"Error: {e}")

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    time_label.config(text=f"Execution time: {elapsed_time:.5f} seconds")

def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="Answer: ")
    time_label.config(text="Execution time: ")

# Create the main window
root = tk.Tk()
root.title("Calculator")

root.geometry("400x300")

# Create a label
label_text = tk.Label(root, text="Addition (+), Subtraction (-), Division (/), Multiplication (*)")
label_text.pack(pady=10)

# Create an entry widget for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=on_button_click)
calculate_button.pack(pady=5)

# Create a button to clear the input and result fields
clear_button = tk.Button(root, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

# Create a label to display the result
result_label = tk.Label(root, text="Answer: ")
result_label.pack(pady=10)

# Create a label to display the execution time
time_label = tk.Label(root, text="Execution time: ")
time_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
