# ⚡ WattWise – AI-Powered Electricity Bill Analyzer

WattWise is a simple yet powerful web app that analyzes your electricity bill and breaks down your estimated energy usage by appliances. It gives actionable saving tips and shows visual charts — helping you reduce power consumption and cut costs.

---

## 🧠 Features

- 🔍 Input total units and bill amount
- 🔌 Estimate energy usage by appliance (fan, lights, fridge, AC, TV)
- 📊 Visualize consumption with bar and pie charts
- 💡 Get smart, personalized power-saving tips
- 🧮 All logic is transparent and explainable — no black box

---

## 🚀 Live Demo

*(Optional: Add GitHub Pages / Streamlit link)*  
**Coming soon...**

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Visualization**: Matplotlib
- **Frontend**: HTML, Jinja2 Templates
- **Optional**: pdfplumber (if parsing bills later)

---

## 📁 Folder Structure

wattwise/
├── app.py # Flask app runner
├── utils/
│ └── analyze.py # Core logic for breakdown, tips, and charts
├── templates/
│ └── result.html # Result display template
├── static/
│ ├── chart.png # Units bar chart
│ └── appliance_pie.png # Appliance usage pie chart


---

## 🧪 How to Run

1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/wattwise.git
cd wattwise 

```
2 Create a virtual environment and install dependencies:

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install flask matplotlib

```
Run the app:
```
python app.py

```

Upcoming Features
User-editable appliance usage sliders

₹ Cost per appliance

Export report as PDF

PDF bill reading via OCR

 Contributing
PRs are welcome! Feel free to suggest ideas, submit fixes, or request features.

Authors
D.Durga Prasad
