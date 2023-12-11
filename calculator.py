import streamlit as st
st.title("Calculator")

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def Multiplication(a,b):
    return a*b

def Division(a,b):
    if b==0:
        return "division by zero not possible"
    else:
        return a/b
    
operation=st.sidebar.selectbox("Select Operation",("addition",'subtraction','multiplication','division'))
num1=st.number_input("Enter the first number",value=0)
num2=st.number_input("Enter teh second number",value=0)
def calculator():
    if st.button('Calculate'):
        result=0

        if operation=='addition':
            result=add(num1,num2)
        elif operation=='subtraction':
            result=subtract(num1,num2)
        elif operation=='multiplication':
            result=Multiplication(num1,num2)
        elif operation=='division':
            result=Division(num1,num2)

        st.success(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    calculator()