def average_ratios(numbers):
    total = 0
    count = 0
    for i, num in enumerate(numbers):
        if num == 0:
            logging.warning(f"Skipped division by zero at index {i}")
            continue
        total += 100 / num
        count += 1
    if count == 0:
        raise ValueError("No valid (non-zero) numbers provided.")
    return total / count

if __name__ == "__main__":
    print(average_ratios([10, 5, 0]))