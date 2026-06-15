import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="MiniStore - Demo E-Commerce",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------------------------------------
# Custom CSS Styling
# ----------------------------------------------------
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        padding: 40px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    }

    .hero h1 {
        font-size: 3rem;
        margin-bottom: 10px;
    }

    .hero p {
        font-size: 1.2rem;
    }

    /* Product Card */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        height: 320px;
    }

    .product-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #111827;
    }

    .product-category {
        color: #6B7280;
        font-size: 0.9rem;
    }

    .product-price {
        color: #10B981;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 10px;
    }

    .section-title {
        font-size: 2rem;
        font-weight: bold;
        color: #111827;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .sidebar-title {
        font-size: 1.1rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Sample Product Data
# ----------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2499,
        "description": "Premium noise-cancelling headphones with 30-hour battery life.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 3999,
        "description": "Track fitness, heart rate, and notifications on the go.",
        "category": "Electronics"
    },
    {
        "name": "Gaming Mouse",
        "price": 1499,
        "description": "Ergonomic RGB gaming mouse with adjustable DPI settings.",
        "category": "Accessories"
    },
    {
        "name": "Leather Backpack",
        "price": 2999,
        "description": "Stylish and durable backpack perfect for work and travel.",
        "category": "Fashion"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Lightweight running shoes designed for comfort and speed.",
        "category": "Fashion"
    },
    {
        "name": "Portable Bluetooth Speaker",
        "price": 1999,
        "description": "Compact speaker with deep bass and waterproof design.",
        "category": "Electronics"
    }
]

# ----------------------------------------------------
# Session State for Cart
# ----------------------------------------------------
if "cart" not in st.session_state:
    st.session_state.cart = []

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(list(set(p["category"] for p in products)))

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("Cart Summary")

cart_count = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.metric("Items", cart_count)
st.sidebar.metric("Total", f"₹{cart_total:,}")

# ----------------------------------------------------
# Hero Section
# ----------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your One-Stop Demo E-Commerce Experience</p>
    <p>Discover premium products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# Welcome Section
# ----------------------------------------------------
st.markdown(
    '<div class="section-title">Welcome to MiniStore</div>',
    unsafe_allow_html=True
)

st.write("""
Explore our collection of carefully selected products.
This demo store showcases a modern e-commerce interface built entirely using Streamlit.
""")

# ----------------------------------------------------
# Filter Products
# ----------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# ----------------------------------------------------
# Featured Products Section
# ----------------------------------------------------
st.markdown(
    '<div class="section-title">Featured Products</div>',
    unsafe_allow_html=True
)

# ----------------------------------------------------
# Product Cards Layout
# ----------------------------------------------------
cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:

        st.markdown(f"""
        <div class="product-card">
            <div class="product-title">{product['name']}</div>
            <div class="product-category">{product['category']}</div>
            <br>
            <div>{product['description']}</div>
            <div class="product-price">₹{product['price']:,}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            f"Add to Cart",
            key=f"cart_{index}"
        ):
            st.session_state.cart.append(product)
            st.success(f"{product['name']} added to cart!")
# ----------------------------------------------------
# Footer
# ----------------------------------------------------
st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:15px;">
    <h4>MiniStore Demo</h4>
    <p>Built with Streamlit • Modern UI • Sample E-Commerce Website</p>
</div>
""", unsafe_allow_html=True)