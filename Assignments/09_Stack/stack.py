class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        
        to_return = self.top.data
        self.top = self.top.next
        return to_return

    def peek(self):
        return None if self.top is None else self.top.data

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None


"""########## Assignment Methods ##########"""

def operators_precedence(op1, op2):
    if op2 == '(':
        return 1
    
    if (op2 == '*' or op2 == '/') and (op1 == '+' or op1 == '-'):
        return 1
    
    if (op2 == '*' or op2 == '/') and (op1 == '*' or op1 == '/'):
        return 0
    
    if (op2 == '+' or op2 == '-') and (op1 == '+' or op1 == '-'):
        return 0
    
    return 0


def infix_to_postfix(expr):
    stack = LinkedStack()
    output = ""
    i = 0

    while i < len(expr):
        # Skip white space
        if expr[i] == " ":
            i += 1
            continue
        
        # Check if the current character is a digit
        if str.isdigit(expr[i]):
            while i < len(expr) and (str.isdigit(expr[i]) or expr[i] == '.'):
                output += expr[i]
                i += 1
            
            output += " "  
            continue
        
        # Check and deal with the different operators according to precedence
        elif expr[i] == '(' or expr[i] == '*' or expr[i] == '/' or expr[i] == '+' or expr[i] == '-':
            if stack.is_empty() or stack.peek() == '(':
                stack.push(expr[i])
            
            else:
                if operators_precedence(stack.peek(), expr[i]) == 1:
                    stack.push(expr[i])
                
                else:
                    while not stack.is_empty() and stack.peek() != '(' and operators_precedence(stack.peek(), expr[i]) != 1:
                        output += stack.pop() + " "
                    
                    stack.push(expr[i])

        # Deal with the case when the character in a right parenthesis.
        elif expr[i] == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output += stack.pop() + " "
            
            if not stack.is_empty():
                stack.pop()

            else:
                return "Invalid expression (no left parenthesis found), :("
            
        else:
            return f"Invalid character '{expr[i]}' :("
        

        i += 1

    # Pop everything still inside stack after we finish dealing with expression characters    
    while not stack.is_empty():
        if stack.peek() == '(':
            return "Invalid expression, :("
        
        output += stack.pop() + " "
    
    return output.strip()


expr = input("Please enter an exprission: ") # example: 5 + ( 6 - 2 ) * 9

print(infix_to_postfix(expr))
