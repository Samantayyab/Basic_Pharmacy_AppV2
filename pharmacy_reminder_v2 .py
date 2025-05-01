reminders = []
  

medicines = ["Aspirin", "Ibuprofen"]
dosage_times = ["morning", "evening"]

for i in range(2):
    reminders.append(f"Reminder: Take {medicines[i]} in the {dosage_times[i]} .")


print("\nYour Medicine Reminders:")
for reminder in reminders:
  print(reminder)





