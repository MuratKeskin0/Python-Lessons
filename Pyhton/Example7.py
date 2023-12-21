# Sample dataset: List of dictionaries
sales_data = [
    {"sale_id": 1, "amount": 150},
    {"sale_id": 2, "amount": 200},
    {"sale_id": 3, "amount": 78},
    {"sale_id": 4, "amount": 400},
    {"sale_id": 5, "amount": 130}
]

# Function to calculate statistics
def calculate_statistics(data):
    if not data:
        return None

    total_sales = sum(item['amount'] for item in data)
    average_sales = total_sales / len(data)
    min_sales = min(item['amount'] for item in data)
    max_sales = max(item['amount'] for item in data)

    return {
        "average_sales": average_sales,
        "min_sales": min_sales,
        "max_sales": max_sales,
        "total_sales": total_sales
    }

# Calculate and print the statistics
statistics = calculate_statistics(sales_data)
if statistics:
    print("Sales Report:")
    print(f"Average Sales: ${statistics['average_sales']}")
    print(f"Minimum Sales: ${statistics['min_sales']}")
    print(f"Maximum Sales: ${statistics['max_sales']}")
    print(f"Total Sales: ${statistics['total_sales']}")
else:
    print("No data available.")
