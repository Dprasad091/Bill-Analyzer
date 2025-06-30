import matplotlib.pyplot as plt
import os

def analyze_data(data):
    units = data['units']
    cost = data['amount']

    # Simple analysis logic
    tips = []
    if units > 300:
        tips.append("Reduce A/C usage during peak hours.")
    if cost > 1000:
        tips.append("Switch to LED lights and energy-efficient appliances.")

    # Chart
    plt.figure()
    plt.bar(["Units Used"], [units])
    chart_path = os.path.join("static", "chart.png")
    plt.savefig(chart_path)

    result = {
        "units": units,
        "cost": cost,
        "tips": tips,
        "month": data['month']
    }
    return result, chart_path



from sklearn.linear_model import LinearRegression
import numpy as np

def predict_next(units_list):
    model = LinearRegression()
    X = np.array(range(len(units_list))).reshape(-1, 1)
    y = np.array(units_list)
    model.fit(X, y)
    return model.predict([[len(units_list)]])[0]
