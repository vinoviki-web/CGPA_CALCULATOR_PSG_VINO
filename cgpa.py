import streamlit as st 

st.title("CGPA Calculator for PSG TECH")
st.write("Enter your GPA and credits for each semester to calculate your CGPA.")

num_semesters = st.number_input("How many semesters?", min_value=1, step=1)
gpa_list = []
credit_list = []

for i in range(int(num_semesters)):
    st.write(f"### Semester {i + 1}")
    gpa = st.number_input(f"Enter GPA for Semester {i + 1}:", min_value=0.0, max_value=10.0, step=0.01)
    credits = st.number_input(f"Enter total Credits for Semester {i + 1}:", min_value=1, step=1)
    gpa_list.append(gpa)
    credit_list.append(credits)

if st.button("Calculate CGPA"):
    total_credits = sum(credit_list)
    weighted_sum = sum(gpa * credits for gpa, credits in zip(gpa_list, credit_list))
    overall_cgpa = weighted_sum / total_credits if total_credits > 0 else 0
    st.success(f"Your Overall CGPA is: {overall_cgpa:.2f}")
