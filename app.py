import streamlit as st
import streamlit as st

products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 2499,
        "category": "Electronics",
        "rating": 4.8,
        "image": "https://images.pexels.com/photos/3394650/pexels-photo-3394650.jpeg",
        "description": "Premium noise-cancelling headphones."
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 3999,
        "category": "Electronics",
        "rating": 4.7,
        "image": "https://images.pexels.com/photos/437037/pexels-photo-437037.jpeg",
        "description": "Track fitness and notifications."
    },
    {
        "id": 3,
        "name": "Gaming Mouse",
        "price": 1499,
        "category": "Accessories",
        "rating": 4.6,
        "image": "https://images.pexels.com/photos/2115256/pexels-photo-2115256.jpeg",
        "description": "RGB gaming mouse."
    },
    {
        "id": 4,
        "name": "Leather Backpack",
        "price": 2999,
        "category": "Fashion",
        "rating": 4.5,
        "image": "https://images.pexels.com/photos/2905238/pexels-photo-2905238.jpeg",
        "description": "Stylish leather backpack."
    },
    {
        "id": 5,
        "name": "Running Shoes",
        "price": 3499,
        "category": "Fashion",
        "rating": 4.9,
        "image": "https://images.pexels.com/photos/2529148/pexels-photo-2529148.jpeg",
        "description": "Comfortable running shoes."
    },
    {
        "id": 6,
        "name": "Bluetooth Speaker",
        "price": 1999,
        "category": "Electronics",
        "rating": 4.4,
        "image": "https://images.pexels.com/photos/1649771/pexels-photo-1649771.jpeg",
        "description": "Portable speaker with deep bass."
    }
]

st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

if "cart" not in st.session_state:
    st.session_state.cart = []

st.title("🛍️ MiniStore")
st.caption("Premium Online Shopping Experience")

# Sidebar
st.sidebar.title("🛒 Shopping Cart")

categories = ["All"] + list(
    sorted(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "Category",
    categories
)

price_range = st.sidebar.slider(
    "Price Range",
    0,
    5000,
    (0, 5000)
)

# Search
search = st.text_input(
    "🔍 Search Products"
)

# Filter
filtered_products = []

for product in products:

    if selected_category != "All":
        if product["category"] != selected_category:
            continue

    if product["price"] < price_range[0]:
        continue

    if product["price"] > price_range[1]:
        continue

    if search:
        if search.lower() not in product["name"].lower():
            continue

    filtered_products.append(product)

st.subheader("Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):

    with cols[index % 3]:

        st.image(
            product["image"],
            use_container_width=True
        )

        st.markdown(
            f"### {product['name']}"
        )

        st.write(product["description"])

        st.write(
            f"⭐ {product['rating']}"
        )

        st.success(
            f"₹{product['price']}"
        )

        if st.button(
            "Add to Cart",
            key=f"add_{product['id']}"
        ):
            st.session_state.cart.append(product)
            st.rerun()

# Cart Summary
st.sidebar.markdown("---")

total = sum(
    item["price"]
    for item in st.session_state.cart
)

st.sidebar.metric(
    "Items",
    len(st.session_state.cart)
)

st.sidebar.metric(
    "Total",
    f"₹{total}"
)

if st.session_state.cart:

    st.sidebar.subheader("Cart Items")

    for i, item in enumerate(st.session_state.cart):

        col1, col2 = st.sidebar.columns([4,1])

        with col1:
            st.write(item["name"])

        with col2:
            if st.button(
                "❌",
                key=f"remove_{i}"
            ):
                st.session_state.cart.pop(i)
                st.rerun()

    if st.sidebar.button("Clear Cart"):
        st.session_state.cart = []
        st.rerun()

else:
    st.sidebar.info("Cart is empty")

st.info(
    "💬 Open the Support Chatbot page from the left navigation menu."
)