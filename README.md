# 🇰🇪 Affordable Nutrition Planner for Kenya

[Live App](https://nutri-app.streamlit.app/)  

An **AI-powered web application** designed to deliver affordable meal recommendations for Kenyan households, aligned with **SDG 2: Zero Hunger**.  
This project was developed as a **PLP Academy Python Programming final project** and uses **linear programming** to optimize daily nutrition—prioritizing user-owned foods, staying within budget, and incorporating Kenyan staples.

---

## ✨ Features

- **Custom Food Input**: Add owned foodstuffs (e.g., *Maize Flour, 1 kg*) and set costs for extra quantities.  
- **Dynamic Price Updates**: Scrapes real-time prices from **Naivas.online** (fallback to default prices if scraping fails).  
- **Custom Food Nutrients**: Retrieves nutrient data for new foods via the **USDA FoodData Central API**.  
- **Dietary Preferences**: Supports vegetarian diets and food exclusions (e.g., peanuts for allergies, fish for cultural reasons).  
- **Visualization**: Interactive nutrient bar chart (calories, protein, iron, vitamins A/C).  
- **Kenyan Recipes**: Suggests familiar dishes like *ugali na sukuma wiki* based on recommendations.  
- **Public Hosting**: Deployed on **Streamlit Community Cloud**, free and accessible worldwide.  

---

## 🛠️ Setup Instructions

### Prerequisites
- [Python 3.10+](https://www.python.org)  
- [Git](https://git-scm.com)  
- [VS Code](https://code.visualstudio.com) with Python extension  

### Local Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/nutrition-app.git
cd nutrition-app

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
Access locally at: http://localhost:8501

🚀 Deployment
You can deploy for free on Streamlit Community Cloud:

Push to GitHub

bash
Copy code
git add .
git commit -m "Deploy nutrition app"
git push origin main
Go to share.streamlit.io

Connect your GitHub repo

Select main branch

Set app.py as the entry file

Click Deploy!

Your app will be live at a URL like:
👉 https://nutrition-app.streamlit.app

📖 Usage
Set Budget – Choose a daily budget (e.g., KES 300).

Add Owned Foods – Input items you already have (e.g., Maize Flour, 1kg @ KES 110).

Set Preferences – Choose vegetarian or exclude foods (e.g., peanuts, fish).

Get Recommendations – View optimized diet plan, nutrient chart, and suggested recipes.

Update Prices – Fetch the latest Naivas prices (optional).

🧑‍💻 Tech Stack
Python – Core programming

PuLP – Linear programming for optimization

Streamlit – Web interface

Pandas – Data handling & visualization

Requests + BeautifulSoup – Price scraping

USDA API – Nutrient data

📊 Data Sources
Foods: Kenyan staples (maize flour, sukuma wiki, beans)

Costs: 2025 estimates from Naivas, KNBS, and market trends (maize flour ~KES 110/kg)

Nutrients: USDA / FAO data (Calories, Protein, Iron, Vitamins A & C)

ℹ️ For more accuracy, update with local market data or APIs.

⚠️ Limitations
Web scraping may fail if Naivas.online changes its structure.

USDA API uses a demo key (limited requests); obtain a free key here.

Currently tracks a simplified nutrient set – expand with Kenyan food composition data for precision.

🌱 Future Enhancements
Add more Kenyan recipes (githeri, ndengu curry).

Optimize UI for mobile access in rural areas.

Track carbon footprint for sustainable eating.

Integrate additional APIs (e.g., Numbeo for pricing).

🌍 SDG 2 Impact
This app empowers low-income Kenyan households to:
✅ Maximize nutrition from foods they already own
✅ Minimize waste and costs
✅ Access affordable, culturally relevant meal plans

By promoting nutrient-rich, affordable diets, the tool directly supports SDG 2: Zero Hunger.

👤 Author
John Muli
PLP Python Programming Final Project – September 2025

📜 License
MIT License – Free to use, modify, and share.
