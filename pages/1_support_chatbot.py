import streamlit as st
products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "price": 2499,
        "category": "Electronics",
        "rating": 4.8,
        "description": "Premium noise-cancelling headphones."
    },
    {
        "id": 2,
        "name": "Smart Watch",
        "price": 3999,
        "category": "Electronics",
        "rating": 4.7,
        "description": "Track fitness and notifications."
    },
    {
        "id": 3,
        "name": "Gaming Mouse",
        "price": 1499,
        "category": "Accessories",
        "rating": 4.6,
        "description": "RGB gaming mouse."
    },
    {
        "id": 4,
        "name": "Leather Backpack",
        "price": 2999,
        "category": "Fashion",
        "rating": 4.5,
        "description": "Stylish leather backpack."
    },
    {
        "id": 5,
        "name": "Running Shoes",
        "price": 3499,
        "category": "Fashion",
        "rating": 4.9,
        "description": "Comfortable running shoes."
    },
    {
        "id": 6,
        "name": "Bluetooth Speaker",
        "price": 1999,
        "category": "Electronics",
        "rating": 4.4,
        "description": "Portable speaker with deep bass."
    }
]

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬",
    layout="wide"
)

st.title("💬 MiniStore Support")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you?"
        }
    ]

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

def get_response(text):

    text = text.lower()

    if "delivery" in text:
        return "Delivery takes 3-5 business days."

    if "refund" in text:
        return "Refunds are processed within 5-7 business days."

    if "return" in text:
        return "Returns are accepted within 30 days."

    if "payment" in text:
        return "We accept UPI, Debit Card, Credit Card and Net Banking."

    if "order" in text:
        return "Please provide your Order ID."

    for product in products:
        if product["name"].lower() in text:
            return (
                f"{product['name']} costs ₹{product['price']}."
            )

    return (
        "I can help with products, delivery, returns, refunds and payments."
    )

prompt = st.chat_input(
    "Ask a question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = get_response(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    st.rerun()
