# TASK PLANNER

# =====================================================

class Task:
	def __init__(self, task_id, title, due_date, priority, status = "pending"):
		self.task_id = task_id
		self.title = title
		self.due_date = due_date
		self.priority = priority
		self.status = status

	def mark_done(self):
		self.status = "done"

	def display(self):
		print(f" >> [{self.task_id}] {self.title}")
		print(f"	Due: {self.due_date} | Priority: {self.priority} | Status: {self.status}")

# =====================================================

class TaskPlanner:
	def __init__(self):
		self.tasks = []
		self.next_id = 1

	def add_task(self):
		print("\n--- Add New Task ---")
		title = input("Task title: ")
		due_date = input("Due date (DD/MM/YYYY): ")
		priority = input("Priority (high/medium/low): ").lower()

		if priority not in ["high", "medium", "low"]:
			print("Invalid priority! Setting to 'medium'.")
			priority = "medium"

		new_task = Task(self.next_id, title, due_date, priority)
		self.tasks.append(new_task)
		self.next_id += 1
		print(f"\n✅ Task added! ID: {new_task.task_id}")

	def view_all_tasks(self):
		print("\n--- All Tasks ---")
		if len(self.tasks) == 0:
			print(" >> No tasks yet.")
			return
		for task in self.tasks:
			task.display()

	def view_pending(self):
		print("\n--- Pending Tasks ---")
		found = False
		for task in self.tasks:
			if task.status == "pending":
				task.display()
				found = True
		if not found:
			print(" >> No pending tasks!")

	def view_done(self):
		print("\n--- Completed Tasks ---")
		found = False
		for task in self.tasks:
			if task.status == "done":
				task.display()
				found = True
		if not found:
			print(" >> No completed tasks yet.")

	def mark_task_done(self):
		print("\n--- Mark Task as Done ---")
		task_id = int(input("Enter task ID: "))
		task = self.find_task(task_id)
		if task:
			if task.status == "done":
				print(" >> This task is already marked as done.")
			else:
				task.mark_done()
			print(f"✅ '{task.title}' marked as done!")
		else:
			print(" >> Task not found.")

	def delete_task(self):
		print("\n--- Delete Task ---")
		task_id = int(input("Enter task ID to delete: "))
		task = self.find_task(task_id)
		if task:
			confirm = input(f" Delete '{task.title}'? (y/n): ")
			if confirm.lower() == "y":
				self.tasks.remove(task)
				print("✅ Task deleted!")
			else:
				print(" >> Deletion cancelled.")
		else:
			print(" >> Task not found.")

	def search_task(self):
		print("\n--- Search Task ---")
		keywd = input("Enter keyword: ").lower()
		results = []
		for task in self.tasks:
			if keywd in task.title.lower():
				results.append(task)
		if results:
			print(f" >> Found {len(results)} result(s):")
			for task in results:
				task.display()
		else:
			print(" >> No tasks found with that keyword.")

	def show_statistics(self):
		total = len(self.tasks)
		done = sum(1 for t in self.tasks if t.status == "done")
		pending = total - done

		print("\n--- Statistics ---")
		print(f" Total Tasks : {total}")
		print(f" Completed   : {done}")
		print(f" Pending     : {pending}")

		if total > 0:
			rate = (done / total) * 100
			print(f" Completion  : {rate:.1f}%")

		high = sum(1 for t in self.tasks if t.priority == "high" and t.status == "pending")
		medium = sum(1 for t in self.tasks if t.priority == "medium" and t.status == "pending")
		low = sum(1 for t in self.tasks if t.priority == "low" and t.status == "pending")
		print("\n Pending by priority:")
		print(f"	High: {high} | Medium: {medium} | Low: {low}")

	def find_task(self, task_id):
		for task in self.tasks:
			if task.task_id == task_id:
				return task
		return None

# =====================================================

def print_menu():
    print("\n========== TASK PLANNER ==========")
    print(" 1. Add New Task")
    print(" 2. View All Tasks")
    print(" 3. View Pending Tasks")
    print(" 4. View Completed Tasks")
    print(" 5. Mark Task as Done")
    print(" 6. Delete Task")
    print(" 7. Search Task")
    print(" 8. Statistics")
    print(" 0. Exit")
    print("==================================")

# =====================================================

def main():
	p = TaskPlanner()

	print("\n>> Welcome to Task Planner! ")
	print(">> stay organised, stay productive. ")

	while True:
		print_menu()
		ch = input("Enter choice (0-8): ")
		match(ch):
			case '1':
				p.add_task()
			case '2':
				p.view_all_tasks()
			case '3':
				p.view_pending()
			case '4':
				p.view_done()
			case '5':
				p.mark_task_done()
			case '6':
				p.delete_task()
			case '7':
				p.search_task()
			case '8':
				p.show_statistics()
			case '0':
				print("\n >> Thanks for using Task Planner! Goodbye!\n")
				exit()
			case _:
				print("\n >> Invalid choice. Please try again.")

# =====================================================

main()
