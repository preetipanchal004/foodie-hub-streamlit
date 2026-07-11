import streamlit as st
import pandas as pd
st.sidebar.title("Foodie hub")
page = st.sidebar.radio("menu",
["Home", "Menu", "Offers", "Contact"])
st.title("Foodie hub")
st.header("Fresh, Delicious & Delivered to your Door")
st.subheader("Explore Your Favourite Meals Anytime, Anywhere")

st.image("foodie hub.jpg", width = 300)

st.markdown("""
            ## Today's Special
            
            Welcome to **Foodie Hub**!
            
            Enjoy fresh and delicious food made with love.
            """)
st.write("###  Our Menu")

st.write("Pizza")
st.write("Burger")
st.write("Pasta")
st.write("Sandwich")
st.write("Momos")
st.write("Cold Coffee")

category = st.selectbox("Select Category",
["Fast Food", "Indian", "chinese", "Italian", "desserts"])

st.subheader("Price List")

st.table({
    "Food": ["Pizza", "Burger", "Pasta", "Sandwich", "Momos", "Cold Coffee"],
    "Price": ["250", "180", "220", "120", "80", "150"]
})

st.info("Get 20% OFF on your First Order!")

food = st.selectbox(
    "Choose Your Favourite Food",
    ["Pizza","Burger","Pasta","Sandwich","Momos"]
)
st.write("You Selected:", food)

with st.form("food_form"):

    name = st.text_input("Enter Your Name")
    
    feedback = st.text_area("Give Your Feedback")

    rating = st.slider("Rate Our Food",1, 5)
    
    submit = st.form_submit_button("Order Now")
    
    if submit:
        st.success("Thank You! Your Order has been Placed Successfully")
        
        st.write("Name:", name)
        st.write("Feedback:", feedback)
        st.write("Rating:", rating)
        
        st.subheader("Contact Us")
        st.write("Email: foodiehub@gmail.com")
        st.write("Phone: +91-9876543210")
    
    st.markdown("---")
    st.write("2026 Foodie Hub | Thank You for Visiting")