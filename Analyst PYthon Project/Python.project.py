import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

st.set_page_config(page_title="ITR Filing Dashboard", layout="wide")

st.title("📈 ITR Filing Analytics Platform")

uploaded_file = st.file_uploader("📂 Upload your ITR user CSV file", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, parse_dates=["user_create_date", "payment_date", "first_filing_date", "last_filing_date"])
    except Exception as e:
        st.error(f"Failed to read CSV file: {e}")
    else:
        st.success("File uploaded successfully")

        # Clean & prepare
        df['filed'] = df['first_filing_date'].notna().astype(int)
        df['gender'] = df['gender'].astype(str)
        df['Age_bucket'] = df['Age_bucket'].astype(str)
        if 'Plan_selected' in df.columns:
            df['Plan_selected'] = df['Plan_selected'].map({'Yes': 1, 'No': 0})
        if 'journey_started_after_login' in df.columns:
            df['journey_started_after_login'] = df['journey_started_after_login'].map({'Yes': 1, 'No': 0})
        if 'payment_status' in df.columns:
            df['payment_status'] = df['payment_status'].map({'Success': 1, 'Failed': 0, 'Fail': 0})

        # Encode categorical (only existing columns)
        cat_cols = ["gender", "Age_bucket", "plan", "state", "partner", "filing_mode", "user_type", "income_band"]
        cat_cols = [col for col in cat_cols if col in df.columns]
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)

        st.subheader("🎯 AI-Based Filing Forecast")
        target = "filed"
        drop_cols = ["user_id", "FY_Year", "first_filing_date", "last_filing_date", "user_create_date", "payment_date", "filed"]
        features = df.drop(columns=[col for col in drop_cols if col in df.columns])

        # Ensure numeric only
        features = features.select_dtypes(include=['number'])
        labels = df[target]

        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test)[:, 1]
        full_proba = model.predict_proba(features)[:, 1]

        estimated_filers = int(full_proba.sum())

        st.markdown(f"🔮 **Estimated users likely to file in future:** `{estimated_filers}` out of `{len(df)}`")

        st.text("\n📋 Classification Report")
        st.text(classification_report(y_test, y_pred))

        # Feature importances
        st.subheader("📊 Feature Importance")
        importance_df = pd.DataFrame({
            "Feature": X_train.columns,
            "Importance": model.feature_importances_
        }).sort_values("Importance", ascending=False).head(15)

        st.bar_chart(importance_df.set_index("Feature"))

        st.success("AI prediction completed using all available data. Key drivers are visualized above.")
else:
    st.info("Please upload a CSV file to start the analysis.")
