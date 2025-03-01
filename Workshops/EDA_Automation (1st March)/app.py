import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def eda_analysis(file_path):
    df = pd.readd_csv(file_path)
    
    #filling numerical values
    for col in df.select_dtypes(include = ["numbers"]).columns:
        df[col].fillna(df[col].median, inplace = True)
        
    for col in df.select_dtypes(include = ["object"]).columns:
        df[col].fillna(df[col].mode()[0], inplace = True)
        
    summary = df.describe(include = "all").to_string()
    
    missing_values = df.issnull().sum().to_string()        
    insights = generate_ai_insights(summary)
    
    plot_paths = generate_visualization(df)
    
    return f"\n Data Loaded Successfully \n\n Summary: \n {summary} \n\n Missing Values: \n {missing_values} \n\n Insights: \n {insights} \n\n Plots: \n {plot_paths}"