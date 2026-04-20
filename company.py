import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

DATASET_PATH = "company_dataset.csv"

def analyze_companies(path):
    # Load the dataset
    df = pd.read_csv(path)

    # 1. Pie Chart [companies employees wise]
    plt.figure(figsize=(8, 8))
    # Count occurrences of each employee range
    df['employees'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Employee Distribution Across Companies')
    plt.ylabel('')  # Hides the vertical label for cleaner look
    plt.show()

    # 2. Funnel Chart [companies review wise]
    # We sort by reviews to create the funnel shape
    df_sorted = df.sort_values(by='review_count', ascending=False).head(10)
    fig = px.funnel(df_sorted, x='review_count', y='name', title='Top 10 Companies by Review Count')
    fig.show()

    # 3. Headquarters of 10 companies
    print("\n--- Headquarters of 10 Companies ---")
    print(df[['name', 'hq']].head(10).to_string(index=False))

    # 4. Bar Chart [companies rating wise]
    plt.figure(figsize=(12, 8))
    plt.bar(df['name'].head(15), df['ratings'].head(15), color='skyblue')
    plt.xticks(rotation=30, ha='right')
    plt.title('Company Ratings (Top 15)')
    plt.ylabel('Rating')
    plt.show()

    # 5. Line Chart [companies year wise]
    # Sorting by 'years_old' to show progression or comparison
    df_age = df.sort_values(by='years').head(15)
    plt.figure(figsize=(12, 8))
    plt.plot(df_age['name'], df_age['years'], marker='o', color='orange', linewidth=2)
    plt.xticks(rotation=30, ha='right')
    plt.title('Company Age Comparison')
    plt.ylabel('Years Old')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

# Run the program
if __name__ == "__main__":
    analyze_companies(DATASET_PATH)
