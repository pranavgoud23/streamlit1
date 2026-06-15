import streamlit as st

# ==================================================
# PAGE CONFIGURATION
# ==================================================
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ==================================================
# SESSION STATE
# ==================================================
if "cart" not in st.session_state:
    st.session_state.cart = []

# ==================================================
# CUSTOM CSS
# ==================================================
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

.hero {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.hero h1{
    font-size:55px;
}

.hero p{
    font-size:20px;
}

.product-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 15px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.product-title{
    font-size:24px;
    font-weight:bold;
}

.price{
    color:#16a34a;
    font-size:22px;
    font-weight:bold;
}

.rating{
    color:#f59e0b;
    font-size:18px;
}

.section-title{
    font-size:35px;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# PRODUCT DATABASE
# ==================================================
products = [
    {
        "name":"Wireless Headphones",
        "price":2499,
        "category":"Electronics",
        "rating":"⭐ 4.8",
        "image":"https://images.unsplash.com/photo-1505740420928-5e560c06d30e",
        "description":"Premium noise-cancelling headphones with 30-hour battery life."
    },

    {
        "name":"Smart Watch",
        "price":3999,
        "category":"Electronics",
        "rating":"⭐ 4.7",
        "image":"https://images.unsplash.com/photo-1523275335684-37898b6baf30",
        "description":"Track fitness, heart rate and notifications."
    },

    {
        "name":"Gaming Mouse",
        "price":1499,
        "category":"Accessories",
        "rating":"⭐ 4.6",
        "image":"https://images.unsplash.com/photo-1527814050087-3793815479db",
        "description":"RGB gaming mouse with customizable DPI."
    },

    {
        "name":"Leather Backpack",
        "price":2999,
        "category":"Fashion",
        "rating":"⭐ 4.5",
        "image":"https://images.unsplash.com/photo-1548036328-c9fa89d128fa",
        "description":"Elegant backpack perfect for travel and work."
    },

    {
        "name":"Running Shoes",
        "price":3499,
        "category":"Fashion",
        "rating":"⭐ 4.9",
        "image":"https://images.unsplash.com/photo-1542291026-7eec264c27ff",
        "description":"Lightweight sports shoes for maximum comfort."
    },

    {
        "name":"Bluetooth Speaker",
        "price":1999,
        "category":"Electronics",
        "rating":"⭐ 4.4",
        "image":"https://images.unsplash.com/photo-1589003077984-894e133dabab",
        "description":"Portable speaker with deep bass and waterproof design."
    }
]

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("🛒 MiniStore")

# Search
search = st.sidebar.text_input("🔍 Search Products")

# Categories
categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.selectbox(
    "📂 Categories",
    categories
)

# Price Slider
price_range = st.sidebar.slider(
    "💰 Price Range",
    min_value=0,
    max_value=5000,
    value=(0,5000)
)

# ==================================================
# SHOPPING CART
# ==================================================
st.sidebar.markdown("---")
st.sidebar.subheader("🛍️ Shopping Cart")

cart_count = len(st.session_state.cart)
cart_total = sum(item["price"] for item in st.session_state.cart)

st.sidebar.metric("Items", cart_count)
st.sidebar.metric("Total", f"₹{cart_total:,}")

if st.session_state.cart:

    st.sidebar.markdown("### Cart Items")

    for i,item in enumerate(st.session_state.cart):

        c1,c2 = st.sidebar.columns([4,1])

        with c1:
            st.write(item["name"])
            st.caption(f"₹{item['price']}")

        with c2:
            if st.button("❌", key=f"remove{i}"):
                st.session_state.cart.pop(i)
                st.rerun()

    if st.sidebar.button("🗑️ Clear Cart"):
        st.session_state.cart = []
        st.rerun()

else:
    st.sidebar.info("Cart is empty")

# ==================================================
# HERO SECTION
# ==================================================
st.markdown("""
<div class='hero'>
<h1>🛍️ MiniStore</h1>
<p>Your One Stop Online Shopping Destination</p>
<p>Premium Products • Great Prices • Fast Shopping</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(90deg,#1e3a8a,#2563eb);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
margin-top:20px;
margin-bottom:20px;
">
<h2>🔥 Summer Sale 2026</h2>
<h4>Up to 50% OFF on Electronics, Fashion & Accessories</h4>
<p>Limited Time Offers Available Now</p>
</div>
""", unsafe_allow_html=True)

# ==================================================
# WELCOME SECTION
# ==================================================
st.markdown(
    "<div class='section-title'>Welcome to MiniStore</div>",
    unsafe_allow_html=True
)

st.write("""
Browse our premium collection of electronics,
fashion accessories and lifestyle products.
""")

# ==================================================
# FILTER PRODUCTS
# ==================================================
filtered_products = []

for product in products:

    if selected_category != "All":
        if product["category"] != selected_category:
            continue

    if not (
        price_range[0]
        <= product["price"]
        <= price_range[1]
    ):
        continue

    if search:
        if search.lower() not in product["name"].lower():
            continue

    filtered_products.append(product)

# ==================================================
# FEATURED PRODUCTS
# ==================================================
st.markdown(
    "<div class='section-title'>Featured Products</div>",
    unsafe_allow_html=True
)

# ==================================================
# PRODUCT GRID
# ==================================================
cols = st.columns(3)

for idx, product in enumerate(filtered_products):

    with cols[idx % 3]:

        st.image(
            product["image"],
            use_container_width=True
        )

        st.markdown(
            f"""
            <div class='product-card'>
            <div class='product-title'>
            {product['name']}
            </div>

            <p>{product['category']}</p>

            <div class='rating'>
            {product['rating']}
            </div>

            <p>{product['description']}</p>

            <div class='price'>
            ₹{product['price']}
            </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🛒 Add To Cart",
            key=f"add{idx}"
        ):
            st.session_state.cart.append(product)
            st.success(
                f"{product['name']} added to cart!"
            )
            st.rerun()

# ==================================================
# FOOTER
# ==================================================
st.markdown("---")

st.markdown("""
<div class='footer'>
<h4>MiniStore</h4>
<p>Demo E-Commerce Website Built With Streamlit</p>
</div>
""", unsafe_allow_html=True)