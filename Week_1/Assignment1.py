def find_best_city_to_pillage(t, test_cases):
    results = []
    for case in test_cases:
        n, m, s = case
        best_city = -1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                best_city = max(best_city, int(s[i]))
        results.append(best_city)
    return results

# Input handling
t = int(input().strip())
test_cases = []
for _ in range(t):
    n, m = map(int, input().strip().split())
    s = input().strip()
    test_cases.append((n, m, s))

# Process each test case
results = find_best_city_to_pillage(t, test_cases)

# Output results
for result in results:
    print(result)
