# keert
This a clothing store.
def create_clothing_brand_page(brand_name, clothing_items):
    st.title(f"{brand_name} Clothing")
    st.write("Welcome to our online store!")
    st.write("Check out our latest collection:")

    for item in clothing_items:
        st.write(item)

    st.write("Thank you for visiting our website. Happy shopping!")

# Example usage:
brand_name = "Fashion World"
clothing_items = ["T-shirt", "Jeans", "Dress", "Jacket", "Shoes"]

create_clothing_brand_page(brand_name, clothing_items)

df = pd.read_csv('women_clothing_ecommerce_sales.csv')
df

st.dataframe(df)
