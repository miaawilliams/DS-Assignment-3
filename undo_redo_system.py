# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:

    def __init__(self):
        self.top = None
    

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if not self.top:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value
            

    def clear(self):
        self.top = None


    def peek(self):
        if self.top:
            return self.top.value
        else:
            return None
        

    def print_stack(self):
        current = self.top
        if not current:
            print("Stack is empty.")
            return
        while current:
            print(f"-{current.value}")
            current = current.next
    
        
def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()



    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            # Push the action onto the undo stack and clear the redo stack
            undo_stack.push(action)
            redo_stack.clear()
            print(f"Action performed: {action}")

        elif choice == "2":
            # Pop an action from the undo stack and push it onto the redo stack
            action = undo_stack.pop()  
            if action:
                redo_stack.push(action)          
                print(f"Action undone: {action}")
            else:
                print("Nothing to undo")    

        elif choice == "3":
            action = redo_stack.pop()
            # Pop an action from the redo stack and push it onto the undo stack
            if action:
                undo_stack.push(action)
            else:
                print("Nothing to redo")


        elif choice == "4":
            # Print the undo stack
            undo_stack.print_stack()
            print("\nUndo Stack:")
            if undo_stack.top is None:
                print("Undo stack is empty")
            
            
        elif choice == "5":
            # Print the redo stack
            redo_stack.print_stack()
            print("\nRedo Stack:")
            
            
            
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()



# A stack is the better choice for an undo/ redo system because it follows the last in first out (LIFO) method. The most recent 
# action is the first to be undone/ redone. A stack helps to keep everything organized and easy to access so the program can easily pull
# information and actions from the top of the stack. A queue is better for a help desk scenario because it follows a first in first out
# (FIFO) method. This means that the first customer or ticket that comes into the queue is the first one to be helped, like a line of people.
# This is efficient for a help desk system because it helps make sure every customer is helped in a fair order. The stack and queue differ 
# from lists because lists are not accessed in a specific order. It is simple to access a certain element from a list regardless of 
# where or when it was added. Because order doesn't matter in a list, they would not be good for a help desk or undo/ redo system, as those
# programs relt on FIFO and LIFO methods. Stacks are useful most in scenarios like keeping track of browser history, or undo/ redo
# systems. Queues are helpful in situations like a song queue, or a line of people online (tickets, customer service, etc.). Lists, stacks,
# and queues are all useful and important ways or storing data, but they all serve different purposes and have their strenghths and weaknesses.