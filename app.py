import streamlit as st
import pandas as pd
import joblib

model = joblib.load('laptop_price_prediction_model.pkl')

st.title("💻 Laptop Price Predictor")

# Existing inputs
company = st.selectbox("Company", ['HP', 'Dell', 'Lenovo', 'Apple', 'Asus', 'Acer', 'MSI', 'Microsoft'])
typename = st.selectbox("Laptop Type", ['Notebook', 'Gaming', 'Ultrabook', 'Workstation'])
cpu_input = st.selectbox("CPU Brand", ['Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen'])
memory = st.selectbox("Storage", ['128GB SSD', '256GB SSD', '512GB SSD', '1TB HDD', '1TB SSD'])
gpu_input = st.selectbox("GPU", ['Intel', 'Nvidia', 'AMD'])
os_input = st.selectbox("Operating System", ['Windows 10', 'Windows 11', 'Mac OS', 'Linux'])
weight = st.number_input("Weight (in kg)", step=0.1, min_value=0.5, max_value=5.0, value=1.5)
touch = st.selectbox("Touchscreen", ['Yes', 'No'])
ips = st.selectbox("IPS Display", ['Yes', 'No'])
pixels = st.selectbox("Resolution", ['1920x1080', '1366x768', '1600x900', '3840x2160'])

# RAM buttons
ram_options = [2, 4, 8, 16, 32, 64]
if "ram" not in st.session_state:
    st.session_state.ram = None

st.write("Select RAM (in GB):")
cols = st.columns(len(ram_options))
for i, val in enumerate(ram_options):
    if cols[i].button(str(val)):
        st.session_state.ram = val

if st.session_state.ram is None:
    st.write("No RAM selected yet")
else:
    st.write(f"Selected RAM: {st.session_state.ram} GB")

# Screen Size buttons
screen_sizes = [13.3, 14.0, 15.6, 17.3]
if "inches" not in st.session_state:
    st.session_state.inches = None

st.write("Select Screen Size (in inches):")
cols = st.columns(len(screen_sizes))
for i, val in enumerate(screen_sizes):
    if cols[i].button(str(val)):
        st.session_state.inches = val

if st.session_state.inches is None:
    st.write("No screen size selected yet")
else:
    st.write(f"Selected Screen Size: {st.session_state.inches} inches")

# Convert storage function same as before
def convert_storage(x):
    x = x.replace(' ', '')
    x = x.replace('SSD', '').replace('HDD', '')
    if 'TB' in x:
        return int(float(x.replace('TB', '')) * 1024)
    else:
        return int(x.replace('GB', ''))

# Predict button
if st.button("Predict Price"):
    if st.session_state.ram is None or st.session_state.inches is None:
        st.error("Please select RAM and Screen Size before predicting!")
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
            st.success(f"💰 Estimated Price: ₹{int(result[0])}")

        except Exception as e:
            st.error(f"⚠️ Prediction failed: {e}")
