import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="ITR Filing Dashboard", layout="wide")

st.title("📈 ITR Filing Analytics Platform")

uploaded_file = st.file_uploader("📂 Upload your ITR user CSV file", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, parse_dates=["user_create_date", "payment_date", "first_filing_date", "last_filing_date"])
    except Exception as e:
        st.error(f"Failed to read CSV file: {e}")
    else:
        required_columns = [
            "user_id", "FY_Year", "journey_started_after_login", "Plan_selected",
            "payment_status", "first_filing_date", "last_filing_date",
            "gender", "Age_bucket"
        ]

        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            st.error(f"The following required columns are missing in your file: {', '.join(missing_cols)}")
        else:
            st.sidebar.header("🔍 Filters")
            fy_filter = st.sidebar.selectbox("Filter by FY Year", options=["All"] + sorted(df["FY_Year"].dropna().unique().tolist()))
            if fy_filter != "All":
                df = df[df["FY_Year"] == fy_filter]

            st.subheader("1️⃣ User Overview")
            total_users = df["user_id"].nunique()
            repeat_users = df[df["user_id"].duplicated(keep=False)]
            new_users = df.drop_duplicates("user_id", keep="first")

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Unique Users", total_users)
            col2.metric("Repeat Users", repeat_users["user_id"].nunique())
            col3.metric("New Users", new_users["user_id"].nunique())

            fig = px.pie(names=["Repeat", "New"], values=[repeat_users["user_id"].nunique(), new_users["user_id"].nunique()], title="User Types")
            st.plotly_chart(fig)

            st.subheader("1️⃣.a Gender & Age Distribution")
            gender_counts = df['gender'].value_counts()
            age_counts = df['Age_bucket'].value_counts()
            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(px.pie(names=gender_counts.index, values=gender_counts.values, title="Gender Distribution"))
            with col2:
                st.plotly_chart(px.pie(names=age_counts.index, values=age_counts.values, title="Age Bucket Distribution"))

            st.subheader("2️⃣ Funnel Analysis")
            funnel = {
                "Journey Started": df[df["journey_started_after_login"] == "Yes"].shape[0],
                "Plan Selected": df[df["Plan_selected"] == "Yes"].shape[0],
                "Payment Success": df[df["payment_status"] == "Success"].shape[0],
                "Filed": df[df["first_filing_date"].notna()].shape[0],
            }
            funnel_df = pd.DataFrame(list(funnel.items()), columns=["Stage", "Count"])
            st.bar_chart(funnel_df.set_index("Stage"))

            st.subheader("3️⃣ Drop-Off Analysis")
            total = len(df)
            journey_no = df[df["journey_started_after_login"] != "Yes"].shape[0]
            plan_no = df[(df["journey_started_after_login"] == "Yes") & (df["Plan_selected"] != "Yes")].shape[0]
            pay_no = df[(df["Plan_selected"] == "Yes") & (df["payment_status"] != "Success")].shape[0]
            filed_no = df[(df["payment_status"] == "Success") & (df["first_filing_date"].isna())].shape[0]

            drop_data = pd.DataFrame({
                "Stage": ["No Journey", "No Plan Selected", "Payment Failed", "Did Not File"],
                "Users": [journey_no, plan_no, pay_no, filed_no]
            })
            st.bar_chart(drop_data.set_index("Stage"))

            st.subheader("4️⃣ Filing Forecast (Simple Avg)")
            df['last_filing_year'] = pd.to_datetime(df['last_filing_date'], errors='coerce').dt.year
            filing_trend = df.groupby('last_filing_year')["user_id"].nunique()
            if not filing_trend.empty:
                forecast = int(filing_trend.mean())
                st.write(f"📌 Projected filings (based on average): **{forecast}**")
                st.line_chart(filing_trend)
            else:
                st.info("No filing data available to forecast.")

            st.subheader("5️⃣ Actionable Users")
            actionable = df[(df["payment_status"] == "Success") & (df["first_filing_date"].isna())]
            st.write("🎯 Users who paid but haven't filed:")
            st.dataframe(actionable[["user_id", "payment_date", "plan", "plan_price", "partner", "state"]].drop_duplicates("user_id").head(20))
            csv = actionable.to_csv(index=False)
            st.download_button("📥 Download Actionable Users", csv, "actionable_users.csv", "text/csv")
else:
    st.info("Please upload a CSV file to start the analysis.")
