"""1) За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? 
При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
**Input:**

n = 700

m = 750

**Output:**"""
def calculate_days_to_ride(N, M):
    days = (M + N - 1) // N  # Add N-1 to M and perform integer division by N
    return days

# Example usage:
N = 700  # kilometers per day
M = 1890  # total kilometers to ride
days_needed = calculate_days_to_ride(N, M)
print("The car will need to ride for", days_needed, "days to cover", M, "kilometers.")