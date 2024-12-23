import streamlit as st
import folium
from streamlit_folium import st_folium

# Define the app's navigation
st.sidebar.title("Marketplace App")
page = st.sidebar.selectbox("Navigate", ["Profile Page", "Swipe Items", "Map View"])

# Sample data with placeholder images
sample_items = [
    {"name": "Bike", "price": "$200", "image_url": "https://picsum.photos/400/300?random=1", "location": [37.7749, -122.4194]},
    {"name": "Laptop", "price": "$500", "image_url": "https://picsum.photos/400/300?random=2", "location": [34.0522, -118.2437]},
    {"name": "Table", "price": "$100", "image_url": "https://picsum.photos/400/300?random=3", "location": [40.7128, -74.0060]},
]

# Page 1: Profile Page
if page == "Profile Page":
    st.title("Upload Your Item")

    # Form for item details
    with st.form("item_form"):
        item_name = st.text_input("Item Name")
        item_price = st.text_input("Price")
        item_image = st.file_uploader("Upload Item Image (optional)", type=["jpg", "png", "jpeg"])
        submit_button = st.form_submit_button("Add Item")

        if submit_button:
            if item_name and item_price:
                st.success(f"{item_name} has been added!")
            else:
                st.error("Please fill in all required fields!")

# Page 2: Swipe Items
elif page == "Swipe Items":
    st.title("Swipe Items")
    st.write("Swipe Right for items you like or Left to skip.")

    # Show items in swipeable format
    for item in sample_items:
        st.image(item["image_url"], caption=item["name"], use_column_width=True)
        st.write(f"Price: {item['price']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"Skip {item['name']}"):
                st.write(f"Skipped {item['name']}")
        with col2:
            if st.button(f"Like {item['name']}"):
                st.success(f"You liked {item['name']}")

# Page 3: Map View
elif page == "Map View":
    st.title("Map View of Listings")
    st.write("View items available in your area.")

    # Create a map
    map_center = [37.7749, -122.4194]
    folium_map = folium.Map(location=map_center, zoom_start=5)

    # Add markers for items
    for item in sample_items:
        folium.Marker(
            location=item["location"],
            popup=f"{item['name']} - {item['price']}",
            tooltip=item["name"],
        ).add_to(folium_map)

    # Display the map in the app
    st_folium(folium_map, width=700, height=500)
