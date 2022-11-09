import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(initial_sidebar_state="expanded")



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def show_home():
    st.header("Welcome to ShopIt Car Sale App")
    st.subheader("Buy your dream car here") 
    st.image("back.jpg",use_column_width= True)

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.button("Buy")
    with col2:
        st.button("Sell")
    with col3:
        st.button("Rent")

    col1,col2,col3,col4 = st.columns([1,1,1,1])
    with col1:
        st.image("car1.webp",use_column_width=True)
    with col2:
        st.image("car2.jpeg",use_column_width=True)
    with col3:
        st.image("car3.webp",use_column_width=True)
    with col4:
        st.image("car4.webp",use_column_width=True)
    col1,col2,col3,col4 = st.columns([1,1,1,1])
    with col1:
        st.image("car5.jpg",use_column_width=True)
    with col2:
        st.image("car6.webp",use_column_width=True)
    with col3:
        st.image("car7.webp",use_column_width=True)
    with col4:
        st.image("car8.jpg",use_column_width=True)



def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data
def main():
    st.title("SHopIt Car Sale App")
    menu = ["Home","Login","SignUp","Contact Us"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        show_home()
    elif choice == "Login":
        st.subheader("Login Section")
        username = st.text_input("User Name")
        password = st.text_input("Password",type='password')
        if st.button("Login"):
            create_usertable()
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
            if result:
                st.success("Logged In as {}".format(username))
                show_home()
            else:
                st.warning("Incorrect Username/Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        new_password = st.text_input("Password",type='password')
        if st.button("Signup"):
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
    elif choice == "Contact Us":
        st.subheader("Contact Us")
        st.text("Email: example@gmail.com")
        st.text("Phone: 1234567890")
        st.text("Address: 123, ABC Street, XYZ City, 123456")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
    

if __name__ == '__main__':
    main()

