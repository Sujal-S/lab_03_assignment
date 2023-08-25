class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority

    def __str__(self):
        return f"P_ID: {self.p_id}\tName: {self.name}\tStart Time (ms): {self.start_time}\tPriority: {self.priority}"

def sort_and_print(processes, sort_option):
    if sort_option == 1:
        processes.sort(key=lambda x: x.p_id)
    elif sort_option == 2:
        processes.sort(key=lambda x: x.start_time)
    elif sort_option == 3:
        processes.sort(key=lambda x: x.priority, reverse=True)

    for process in processes:
        print(process)

# Sample process table
processes = [
    Process("P1", "VSCode", 100, "MID"),
    Process("P23", "Eclipse", 234, "MID"),
    Process("P93", "Chrome", 189, "High"),
    Process("P42", "JDK 9", 9, "High"),
    Process("P9", "CMD", 7, "High"),
    Process("P87", "NotePad", 23, "Low")
]

while True:
    print("\nMenu:")
    print("1. Sort by Process ID")
    print("2. Sort by Start Time (ms)")
    print("3. Sort by Priority")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        break

    if choice in [1, 2, 3]:
        sort_and_print(processes, choice)
    else:
        print("Invalid choice. Please select a valid option (1-4).")

