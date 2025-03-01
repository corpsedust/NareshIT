import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama


def eda_analysis(file_path):
    df = pd.read_csv(file_path)

    # Filling missing values
    for col in df.select_dtypes(include=["number"]).columns:
        df[col].fillna(df[col].median(), inplace=True)

    for col in df.select_dtypes(include=["object"]).columns:
        df[col].fillna(df[col].mode()[0], inplace=True)

    summary = df.describe(include="all").to_string()
    missing_values = df.isnull().sum().to_string()
    
    insights = generate_insights(summary)
    plot_paths = generate_visualizations(df)

    return f"\n Data Loaded Successfully \n\n Summary: \n {summary} \n\n Missing Values: \n {missing_values} \n\n Insights: \n {insights} \n\n Plots: \n {plot_paths}"


def generate_insights(df_summary):
    prompt = f"Analyze the dataset summary and provide insights: \n\n {df_summary}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']


def generate_visualizations(df):
    plot_paths = []

    for col in df.select_dtypes(include=['number']).columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], bins=30, kde=True, color='blue')
        plt.title(f"Distribution of {col}")
        path = f"{col}_distribution.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        plt.figure(figsize=(8, 5))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
        plt.title("Correlation Heatmap")
        path = "correlation_heatmap.png"
        plt.savefig(path)
        plot_paths.append(path)
        plt.close()

    return plot_paths


app = gr.Interface(
    fn=eda_analysis(),
    inputs=gr.File(type="filepath"),
    outputs=[gr.Textbox(label="EDA Report"), gr.Gallery(label="Data Visualization")],
    title="LLM-powered EDA App",
    description="Upload any dataset to view the EDA report and data visualization"
)

app.launch(share=True)
