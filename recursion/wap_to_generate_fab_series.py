"""
@desc: Programm to generate fibonaci series recusively
"""

def feb(n1, n2, rc):

    if rc==0:
        return n1+n2
    else:
        print(f"{n1+n2}| ", end=" ")
        n1, n2 = n2, n1+n2
    
    return feb(n1, n2, rc-1)



if __name__ == "__main__":
    # rc = recursive count 
    rc = int(input("Enter the number of iteration you want .."))
    num1 = int(input("Enter the first digit of series.."))
    num2 = int(input("Enter the second digit of series"))

    if rc < 3:
        print(f"Please enter the value greater than 2")
        print(f"{num1}| {num2}| ")
    else:
        print(f"{num1}| {num2}| ", end=" ")
        print(feb(num1, num2, rc-3))
