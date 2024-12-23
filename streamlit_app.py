import streamlit as st
import random
import time

# HTML and CSS for the swiper page
st.markdown("""
    <style>
        .swiper-container {
            width: 100%;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .swiper-slide {
            width: 80%;
            height: 80%;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 20px;
            overflow: hidden;
        }
        .swiper-slide img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .swiper-button-next, .swiper-button-prev {
            color: white;
        }
        .swiper-button-next:hover, .swiper-button-prev:hover {
            background-color: rgba(0, 0, 0, 0.5);
        }
        .swiper-button-next {
            right: 20px;
        }
        .swiper-button-prev {
            left: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Create a list of items with names, descriptions, and images
items = [
    {"title": "Vintage Lamp", "price": "$15", "image": "https://via.placeholder.com/600x400?text=Vintage+Lamp", "description": "A quirky vintage lamp for your cozy home!", "seller": "John Doe", "location": "New York", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Gaming Chair", "price": "$120", "image": "https://via.placeholder.com/600x400?text=Gaming+Chair", "description": "Comfy gaming chair, perfect for long sessions.", "seller": "Jane Smith", "location": "California", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Smart Watch", "price": "$80", "image": "https://via.placeholder.com/600x400?text=Smart+Watch", "description": "Track your health with this sleek smartwatch.", "seller": "Mark Lee", "location": "Texas", "shipping": "No", "payment": "Cash Only"},
    {"title": "Mountain Bike", "price": "$250", "image": "https://via.placeholder.com/600x400?text=Mountain+Bike", "description": "Ready for any terrain, take it for an adventure.", "seller": "Alice Cooper", "location": "Colorado", "shipping": "No", "payment": "Cash Only"},
    {"title": "Bluetooth Speaker", "price": "$40", "image": "https://via.placeholder.com/600x400?text=Bluetooth+Speaker", "description": "Portable speaker with great sound.", "seller": "Eve Adams", "location": "Florida", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Coffee Maker", "price": "$60", "image": "https://via.placeholder.com/600x400?text=Coffee+Maker", "description": "Start your morning right with this reliable coffee maker.", "seller": "George Harris", "location": "Georgia", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Electric Guitar", "price": "$150", "image": "https://via.placeholder.com/600x400?text=Electric+Guitar", "description": "Rock on with this stylish electric guitar.", "seller": "Tom Baker", "location": "Chicago", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Camera Lens", "price": "$300", "image": "https://via.placeholder.com/600x400?text=Camera+Lens", "description": "Capture your moments with this high-quality lens.", "seller": "Sarah Miller", "location": "New York", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Drone", "price": "$400", "image": "https://via.placeholder.com/600x400?text=Drone", "description": "Fly high with this top-notch drone.", "seller": "David Wilson", "location": "California", "shipping": "Yes", "payment": "Cash Only"},
    {"title": "Leather Jacket", "price": "$100", "image": "https://via.placeholder.com/600x400?text=Leather+Jacket", "description": "Stylish leather jacket for all seasons.", "seller": "Clara Scott", "location": "Texas", "shipping": "Yes", "payment": "Cash Only"},
]

# Shuffle items to randomize the order
random.shuffle(items)

# Create the swiper section using the Swiper.js framework
swiper_html = """
    <div class="swiper-container">
        <div class="swiper-wrapper">
"""

# Add each item as a slide
for item in items:
    swiper_html += f"""
        <div class="swiper-slide">
            <div style="text-align:center; padding: 20px; background-color: white; border-radius: 20px;">
                <img src="{item['image']}" alt="{item['title']}">
                <h3>{item['title']}</h3>
                <p>{item['description']}</p>
                <p><strong>Price:</strong> {item['price']}</p>
                <button onclick="showDetails('{item['title']}', '{item['seller']}', '{item['location']}', '{item['shipping']}', '{item['payment']}')">More Details</button>
            </div>
        </div>
    """

swiper_html += """
        </div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>
"""

# Add JavaScript for functionality
swiper_js = """
    <script>
        var swiper = new Swiper('.swiper-container', {
            spaceBetween: 10,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            loop: true,
            on: {
                slideChange: function () {
                    if (this.activeIndex === this.slides.length - 1) {
                        // Reset if we reached the last item
                        setTimeout(function () {
                            swiper.slideTo(0);
                        }, 1000);
                    }
                }
            }
        });

        function showDetails(title, seller, location, shipping, payment) {
            alert(`Title: ${title}\nSeller: ${seller}\nLocation: ${location}\nShipping: ${shipping}\nPayment: ${payment}`);
        }
    </script>
"""

# Display the HTML in Streamlit
st.markdown(swiper_html, unsafe_allow_html=True)
st.markdown(swiper_js, unsafe_allow_html=True)