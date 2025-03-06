import streamlit as st

def convert_units(value,unit_from,unit_to):
    conversions = {
        "meter_kilometer":0.001,
        "kilometer_meter":1000,
        "gram_kilogram":0.001,
        "kilogram_gram":1000
    }
    
    key =f"{unit_from}_{unit_to}"   #generate key based on the input units
    
    if key in conversions:
        conversion= conversions[key]
        return value * conversion
    else:
         return "Conversion not available"

st.title("👩‍💻 Unit Converter")

value = st.number_input("Enter the value to convert : ", min_value=1.0,step=1.0)

unit_from = st.selectbox("Convert From: ",["meter","kilometer","gram","kilogram"])

unit_to = st.selectbox("Convert To: ",["meter","kilometer","gram","kilogram"])

if st.button("🤹 Convert your value"):
    result = convert_units(value,unit_from,unit_to)
    st.write(f"Converted your value: ✨  {result}")

st.write("-------------------------------------------")
st.write("Build with ❤️ by  [Rabia Rehman](https://github.com/studentRabia)")