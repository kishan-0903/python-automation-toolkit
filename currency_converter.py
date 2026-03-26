def convert_to_inr(dollars):
    """
    Converts USD to INR based on the current exchange rate.
    Standardized function for financial automation.
    """
    exchange_rate = 83.50
    return round(dollars * exchange_rate, 2)

payments_usd = []
print("--- International Payment Processor ---")

for i in range(3):
    value = float(input(f"Enter payment amount {i+1} (USD): "))
    payments_usd.append(value)

print("\n--- Conversion Report ---")
for amt in payments_usd:
    inr_value = convert_to_inr(amt)
    print(f"${amt} USD is equivalent to ₹{inr_value} INR")
    
       