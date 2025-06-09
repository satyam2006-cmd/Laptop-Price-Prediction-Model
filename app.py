import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('laptop_price_prediction_model.pkl')

# ------------------ Page Config ------------------
st.set_page_config(page_title="Laptop Price Predictor", layout="centered")

# ------------------ Theme Toggle ------------------
theme = st.selectbox("🌓 Choose Theme", ["Dark", "Light"], index=0)

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: #FAFAFA;
            font-family: 'Segoe UI', sans-serif;
        }
        .title { color: #4db8ff; font-size: 2.4rem; font-weight: bold; }
        .card {
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .stApp {
            background-color: #ffffff;
            color: #000000;
            font-family: 'Segoe UI', sans-serif;
        }
        .title { color: #3366cc; font-size: 2.4rem; font-weight: bold; }
        .card {
            background-color: #e8f0fe;
            padding: 20px;
            border-radius: 12px;
            margin-top: 20px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

# ------------------ App Title ------------------
st.markdown("<div class='title'>💻 Laptop Price Predictor</div>", unsafe_allow_html=True)
st.markdown("Estimate the market price of your laptop based on specs.")
st.image("https://user-images.githubusercontent.com/113234633/208248053-de8898ea-5f32-4bad-956e-2c0a91d3039b.png", width=250)

# ------------------ Input Fields ------------------
col1, col2 = st.columns(2)

with col1:
    company = st.selectbox("🏷️ Brand", ['HP', 'Dell', 'Lenovo', 'Apple', 'Asus', 'Acer', 'MSI', 'Microsoft'])
    typename = st.selectbox("💼 Laptop Type", ['Notebook', 'Gaming', 'Ultrabook', 'Workstation'])
    cpu_input = st.selectbox("🧠 CPU Brand", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen'])
    memory = st.selectbox("💾 Storage", ['128GB SSD', '256GB SSD', '512GB SSD', '1TB HDD', '1TB SSD'])

with col2:
    gpu_input = st.selectbox("🎮 GPU", ['Intel', 'Nvidia', 'AMD'])
    os_input = st.selectbox("🖥️ Operating System", ['Windows 10', 'Windows 11', 'Mac OS', 'Linux'])
    weight = st.number_input("⚖️ Weight (kg)", step=0.1, min_value=0.5, max_value=5.0, value=1.5)
    touch = st.selectbox("🖱️ Touchscreen", ['Yes', 'No'])
    ips = st.selectbox("🌈 IPS Display", ['Yes', 'No'])
    pixels = st.selectbox("🔳 Screen Resolution", ['1920x1080', '1366x768', '1600x900', '3840x2160'])

# ------------------ RAM & Screen Size Buttons ------------------
st.subheader("💡 Choose RAM:")
ram_options = [2, 4, 8, 16, 32, 64]
if "ram" not in st.session_state:
    st.session_state.ram = None

cols = st.columns(len(ram_options))
for i, val in enumerate(ram_options):
    if cols[i].button(f"{val} GB"):
        st.session_state.ram = val

st.write(f"✅ Selected RAM: {st.session_state.ram} GB" if st.session_state.ram else "❌ No RAM selected")

st.subheader("📏 Select Screen Size:")
screen_sizes = [13.3, 14.0, 15.6, 17.3]
if "inches" not in st.session_state:
    st.session_state.inches = None

cols = st.columns(len(screen_sizes))
for i, val in enumerate(screen_sizes):
    if cols[i].button(f"{val}\""):
        st.session_state.inches = val

st.write(f"✅ Screen Size: {st.session_state.inches}\"" if st.session_state.inches else "❌ No size selected")

# ------------------ Storage Converter ------------------
def convert_storage(x):
    x = x.replace(' ', '')
    x = x.replace('SSD', '').replace('HDD', '')
    if 'TB' in x:
        return int(float(x.replace('TB', '')) * 1024)
    else:
        return int(x.replace('GB', ''))

# ------------------ Prediction ------------------
if st.button("🔍 Predict Price"):
    if st.session_state.ram is None or st.session_state.inches is None:
        st.error("⚠️ Please select RAM and Screen Size!")
    else:
        try:
            df = pd.DataFrame([{
                'Company': company,
                'TypeName': typename,
                'Cpu_Brand': cpu_input,
                'Ram': st.session_state.ram,
                'Memory': memory,
                'Gpu_Brand': gpu_input,
                'Gpus': gpu_input,
                'OpSys': os_input,
                'Weight': weight,
                'Inches': st.session_state.inches,
                'Touch': 1 if touch == 'Yes' else 0,
                'Ips': 1 if ips == 'Yes' else 0,
                'Pixels': int(pixels.split('x')[0]) * int(pixels.split('x')[1])
            }])

            df['HDD'] = df['Memory'].apply(lambda x: convert_storage(x) if 'HDD' in x else 0)
            df['SSD'] = df['Memory'].apply(lambda x: convert_storage(x) if 'SSD' in x else 0)
            df['Hybrid'] = 0
            df['Flash_Storage'] = 0
            df.drop(columns=['Memory'], inplace=True)

            result = model.predict(df)
            st.markdown(f"""
                <div class="card">
                    <h3>💰 Estimated Price: <span style="color:#2b8a3e">₹{int(result[0]):,}</span></h3>
                    <p>This is the approximate price based on the laptop specifications.</p>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Prediction failed: {e}")
