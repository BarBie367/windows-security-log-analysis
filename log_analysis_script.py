import matplotlib.pyplot as plt


event_names = {
    "4625": "Failed Login",
    "4624": "Successful Login",
    "4634": "Logoff",
    "4688": "Process Creation",
    "4798": "Group Enumeration"  
}


results = {name: 0 for name in event_names.values()}


with open("security_logs.csv", "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
  
        if line.startswith("Audit Success") or line.startswith("Audit Failure"):
            parts = line.split(",")
            if len(parts) >= 4:
          
                event_id = parts[3].strip()
                
            
                if event_id in event_names:
                    display_name = event_names[event_id]
                    results[display_name] += 1


print("=== Security Event Analysis ===")
for name, count in results.items():
    print(f"{name}: {count}")


if results["Failed Login"] > 5:
    print("\n[ALERT] Possible brute-force attack detected!")


plt.figure(figsize=(10, 5))
plt.bar(results.keys(), results.values(), color=['red', 'green', 'blue', 'orange', 'purple'])
plt.title("Windows Security Events")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.xticks(rotation=15)
plt.tight_layout()

plt.show()

input("\nNaciśnij Enter, aby zakończyć...")
