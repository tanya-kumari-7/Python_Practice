
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import uuid
import io
import base64
import os

# Function to generate a sample dataset
def generate_sample_dataset(n_samples=1000):
    np.random.seed(42)
    data = {
        'user_id': [str(uuid.uuid4()) for _ in range(n_samples)],
        'age': np.random.randint(18, 80, n_samples),
        'income': np.random.randint(20000, 200000, n_samples),
        'filing_status': np.random.choice(['Single', 'Married', 'Head of Household'], n_samples),
        'dependents': np.random.randint(0, 5, n_samples),
        'tax_credits': np.random.randint(0, 5000, n_samples),
        'filing_frequency': np.random.choice(['Annually', 'Quarterly'], n_samples),
        'last_filed': [datetime(2024, np.random.randint(1, 13), np.random.randint(1, 29)).strftime('%Y-%m-%d') for _ in range(n_samples)],
        'platform_usage': np.random.randint(1, 100, n_samples),
        'converted': np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    }
    df = pd.DataFrame(data)
    df.to_csv('tax_filing_data.csv', index=False)
    return df

# Function to load and preprocess dataset
def load_and_preprocess_data(file_path=None, uploaded_file=None):
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_csv(file_path)
    df['last_filed'] = pd.to_datetime(df['last_filed'])
    df['months_since_last_filed'] = (datetime.now() - df['last_filed']).dt.days / 30
    df['income_per_dependent'] = df['income'] / (df['dependents'] + 1)
    df = pd.get_dummies(df, columns=['filing_status', 'filing_frequency'], drop_first=True)
    return df

# Function for user behavior analysis
def user_behavior_analysis(df):
    st.subheader("User Behavior Analysis")
    
    # Average platform usage by filing status
    usage_by_status = df.groupby(['filing_status_Married', 'filing_status_Single'])['platform_usage'].mean().reset_index()
    st.write("**Average Platform Usage by Filing Status:**")
    st.dataframe(usage_by_status)
    
    # Correlation matrix
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    corr_matrix = df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    plt.title('Correlation Matrix of Numeric Features')
    st.pyplot(fig)
    
    # Platform usage distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(df['platform_usage'], bins=20, kde=True, ax=ax)
    plt.title('Distribution of Platform Usage Scores')
    plt.xlabel('Usage Score')
    plt.ylabel('Frequency')
    st.pyplot(fig)

# Function for user filing prediction
def user_filing_prediction(df):
    st.subheader("User Filing Prediction")
    features = [col for col in df.columns if col not in ['user_id', 'last_filed', 'converted']]
    X = df[features]
    y = df['converted']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    st.write("**Classification Report:**")
    st.dataframe(pd.DataFrame(report).transpose())
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    st.write("**Feature Importance:**")
    st.dataframe(feature_importance)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=feature_importance, ax=ax)
    plt.title('Feature Importance for Conversion Prediction')
    st.pyplot(fig)
    
    return model

# Function to identify target audience for conversion
def target_audience_analysis(df):
    st.subheader("Target Audience for Conversion")
    
    # Characteristics of converted users
    high_conversion = df[df['converted'] == 1]
    st.write("**Characteristics of Converted Users:**")
    st.dataframe(high_conversion[['age', 'income', 'dependents', 'tax_credits', 'platform_usage']].describe())
    
    # Potential target audience
    potential_targets = df[(df['platform_usage'] > df['platform_usage'].quantile(0.75)) & (df['converted'] == 0)]
    st.write("**Potential Target Audience (High Usage, Non-Converted):**")
    st.dataframe(potential_targets[['user_id', 'age', 'income', 'platform_usage']].head())
    
    # Downloadable CSV
    csv = potential_targets.to_csv(index=False)
    st.download_button(
        label="Download Potential Targets CSV",
        data=csv,
        file_name="potential_targets.csv",
        mime="text/csv"
    )

# Function for idea suggestions and observations
def generate_ideas_and_observations(df):
    st.subheader("Ideas and Observations")
    observations = []
    ideas = []
    
    usage_corr = df['platform_usage'].corr(df['converted'])
    observations.append(f"Platform usage has a correlation of {usage_corr:.2f} with conversion, indicating that more engaged users are more likely to convert.")
    high_income_converted = df[df['income'] > df['income'].quantile(0.75)]['converted'].mean()
    observations.append(f"Users with income above the 75th percentile have a conversion rate of {high_income_converted:.2%}.")
    
    ideas.append("Launch targeted email campaigns for users with high platform usage (>75th percentile) but who haven't converted, offering personalized tax filing guidance.")
    if df[df['filing_frequency_Quarterly'] == 1]['converted'].mean() > df['converted'].mean():
        ideas.append("Offer discounts or premium features to quarterly filers, as they show higher conversion rates.")
    
    st.write("**Observations:**")
    for obs in observations:
        st.write(f"- {obs}")
    
    st.write("**Ideas for Improvement:**")
    for idea in ideas:
        st.write(f"- {idea}")
    
    # Generate and offer downloadable report
    report = "# Tax Filing Analysis Report\n\n"
    report += "## Observations\n" + "\n".join([f"- {obs}" for obs in observations]) + "\n\n"
    report += "## Ideas for Improvement\n" + "\n".join([f"- {idea}" for idea in ideas])
    
    st.download_button(
        label="Download Analysis Report",
        data=report,
        file_name="analysis_report.md",
        mime="text/markdown"
    )

# Streamlit UI
def main():
    st.title("Tax Filing Analysis Platform")
    st.write("Upload a dataset or use the sample dataset to analyze user behavior, predict filings, identify target audiences, and get insights.")
    
    # File upload
    uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])
    use_sample = st.checkbox("Use sample dataset", value=True)
    
    if use_sample and not uploaded_file:
        if not os.path.exists('tax_filing_data.csv'):
            df = generate_sample_dataset()
        else:
            df = load_and_preprocess_data('tax_filing_data.csv')
    elif uploaded_file:
        df = load_and_preprocess_data(uploaded_file=uploaded_file)
    else:
        st.warning("Please upload a dataset or select the sample dataset.")
        return
    
    st.success("Dataset loaded successfully!")
    st.write("**Dataset Preview:**")
    st.dataframe(df.head())
    
    # Run analyses
    user_behavior_analysis(df)
    model = user_filing_prediction(df)
    target_audience_analysis(df)
    generate_ideas_and_observations(df)

if __name__ == "__main__":
    main()
```