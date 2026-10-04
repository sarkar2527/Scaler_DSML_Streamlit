import streamlit as st

#write a title and a description for the app
st.title("My First Streamlit App")
st.write("This is a simple Streamlit app.")

#header
st.header("This is the header")

#subheader
st.subheader("This is the subheader")

#Checkbox
if st.checkbox("Show/Hide"):
    st.write("Checkbox is checked!")

#radio button
select_option =st.radio("Select an gender", ["Male", "Female", "Other"])

if select_option == "Male":
    st.write("You selected Male")
elif select_option == "Female":
    st.write("You selected Female")
else:
    st.write("You selected Other")

#Create a button
if st.button("Click Me"):
    st.write("Button clicked!")

#Get a number input from the user and square it
def square_number(num):
    return num ** 2

number = st.number_input("Enter a number")

if st.button("Square the number"):
    result = square_number(number)
    st.write(f"The square of {number} is {result}")
