import streamlit as st
import streamlit.components.v1 as components

# Data for the swipe page
items = [
    {"name": "Bike", "price": "$200", "description": "A mountain bike perfect for trails.", "details": "Prefers cash payment. Offers shipping. Seller: Alex, Location: NY"},
    {"name": "Laptop", "price": "$500", "description": "A gaming laptop with RTX 3060.", "details": "Accepts PayPal. Seller: Jordan, Location: LA"},
    {"name": "Table", "price": "$100", "description": "A solid wooden dining table.", "details": "Prefers local pickup. Seller: Chris, Location: SF"},
    {"name": "Chair", "price": "$50", "description": "Ergonomic office chair.", "details": "Prefers cash payment. Seller: Taylor, Location: TX"},
    {"name": "Phone", "price": "$300", "description": "iPhone 12 in great condition.", "details": "Accepts Venmo. Offers shipping. Seller: Morgan, Location: Chicago"},
    {"name": "TV", "price": "$400", "description": "55-inch 4K Ultra HD TV.", "details": "Accepts credit cards. Seller: Casey, Location: Miami"},
    {"name": "Watch", "price": "$150", "description": "Stylish smartwatch.", "details": "Prefers cash payment. Seller: Riley, Location: Seattle"},
    {"name": "Camera", "price": "$250", "description": "DSLR camera with lens kit.", "details": "Offers shipping. Seller: Jamie, Location: Denver"},
    {"name": "Sofa", "price": "$350", "description": "Comfortable 3-seater sofa.", "details": "Local pickup only. Seller: Dana, Location: Portland"},
    {"name": "Headphones", "price": "$75", "description": "Noise-canceling headphones.", "details": "Prefers cash payment. Seller: Taylor, Location: Boston"},
]

# Swipe Page with Custom HTML and JavaScript
def swipe_page():
    st.title("Swipe Items")
    st.write("Swipe right (green) if you like the item or left (red) to skip. Click on an item to see more details.")

    # Custom HTML/JS for Swiping
    html_code = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Swiper/9.0.1/swiper-bundle.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Swiper/9.0.1/swiper-bundle.min.js"></script>
    <style>
        body { font-family: Arial, sans-serif; }
        .swiper-container {
            width: 100%;
            height: 500px;
            overflow: hidden;
        }
        .swiper-slide {
            position: relative;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
        }
        .swiper-slide img {
            max-width: 100%;
            max-height: 60%;
            border-radius: 10px;
        }
        .details-btn {
            position: absolute;
            bottom: 20px;
            padding: 10px 20px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .details-btn:hover {
            background-color: #0056b3;
        }
        .overlay-right {
            background: rgba(0, 255, 0, 0.2);
            z-index: 1000;
        }
        .overlay-left {
            background: rgba(255, 0, 0, 0.2);
            z-index: 1000;
        }
    </style>
    <div class="swiper-container">
        <div class="swiper-wrapper">
    """

    for item in items:
        html_code += f"""
        <div class="swiper-slide">
            <img src="https://picsum.photos/300/200?random={items.index(item)}" alt="{item['name']}">
            <h3>{item['name']}</h3>
            <p>{item['description']}</p>
            <p><b>{item['price']}</b></p>
            <button class="details-btn" onclick="alert('{item['details']}')">View Details</button>
        </div>
        """

    html_code += """
        </div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
    </div>
    <script>
        const swiper = new Swiper('.swiper-container', {
            loop: true,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            on: {
                slideChangeTransitionStart: function () {
                    document.querySelector('.swiper-slide-active').classList.add('overlay-right');
                },
                slideChangeTransitionEnd: function () {
                    document.querySelector('.swiper-slide-active').classList.remove('overlay-right', 'overlay-left');
                }
            }
        });
    </script>
    """

    # Render the HTML in Streamlit
    components.html(html_code, height=600)

# Run the Swipe Page
swipe_page()