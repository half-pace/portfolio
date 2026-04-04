def mean(numbers: float) -> float:
    """Calculate the mean of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0

def median(numbers: float) -> float:
    """Calculate the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]
    
def mode(numbers: float) -> float:
    """Calculate the mode of a list of numbers."""
    from collections import Counter
    count = Counter(numbers)
    mode_data = count.most_common(1)
    return mode_data[0][0] if mode_data else None

def variance(numbers: float) -> float:
    """Calculate the variance of a list of numbers."""
    mean_value = mean(numbers)
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def std_dev(numbers: float) -> float:
    """Calculate the standard deviation of a list of numbers."""
    return variance(numbers) ** 0.5

def percentile(numbers: float, percentile: float) -> float:
    """Return pth percentile using the variance function above"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    k = (n - 1) * (percentile / 100)
    f = int(k)
    c = k - f
    if f + 1 < n:
        return sorted_numbers[f] + c * (sorted_numbers[f + 1] - sorted_numbers[f])
    else:
        return sorted_numbers[f]
    
def main():
    # users enter series of numbers (comma separated), riun all 6 and display a formatted statistics report - including edge cases - what if the list is empty? what if there are multiple modes?
    numbers_input = input("Enter a series of numbers (comma separated): ")
    try:
        numbers = [float(num.strip()) for num in numbers_input.split(",") if num.strip()]
        if not numbers:
            print("No numbers entered. Please enter at least one number.")
            return
        
        print(f"Mean: {mean(numbers)}")
        print(f"Median: {median(numbers)}")
        print(f"Mode: {mode(numbers)}")
        print(f"Variance: {variance(numbers)}")
        print(f"Standard Deviation: {std_dev(numbers)}")
        
        percentile_input = float(input("Enter the percentile to calculate (0-100): "))
        if 0 <= percentile_input <= 100:
            print(f"{percentile_input}th Percentile: {percentile(numbers, percentile_input)}")
        else:
            print("Invalid percentile. Please enter a value between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        
if __name__ == "__main__":    main()