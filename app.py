import streamlit as st
import pandas as pd

# כותרת האפליקציה
st.title("?? מחשבון הוצאות לחברים")

# יצירת מקום לשמירת הנתונים (בזיכרון הזמני של הסשן)
if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# אזור להזנת נתונים חדשים
st.header("הוסף הוצאה חדשה")
with st.form("my_form"):
    name = st.text_input("שם החבר")
    amount = st.number_input("סכום (בשקלים)", min_value=0.0, step=0.1)
    description = st.text_input("תיאור (למשל: פיצה)")
    
    # כפתור שליחה
    submitted = st.form_submit_button("שמור הוצאה")
    
    if submitted:
        if name and amount > 0:
            # הוספה לרשימה
            st.session_state.expenses.append({
                "שם": name,
                "סכום": amount,
                "תיאור": description
            })
            st.success(f"ההוצאה של {name} נשמרה!")
        else:
            st.error("נא למלא שם וסכום תקין.")

# הצגת הטבלה
st.header("רשימת ההוצאות עד כה")
if st.session_state.expenses:
    # המרת הרשימה לטבלה יפה
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)
    
    # חישוב סך הכל
    total = df["סכום"].sum()
    st.metric(label="סה״כ הוצאות הקבוצה", value=f"{total:.2f} ₪")
else:
    st.info("עדיין לא הוזנו הוצאות.")