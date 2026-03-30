import logging

def calculate_totals(data):
    """Apply a 15% increase to each item in data."""
    return [item * 1.15 for item in data]

def log_totals(totals, filename="log.txt"):
    """Append totals to a log file."""
    with open(filename, "a") as f:
        f.write(str(totals) + "\n")

def display_totals(totals):
    """Display each total formatted to two decimal places."""
    for total in totals:
        print(f"Total: {total:.2f}")

def process_data(data):
    """Process data by calculating, displaying, and logging totals."""
    totals = calculate_totals(data)
    display_totals(totals)
    log_totals(totals)
    return totals