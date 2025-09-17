Affordable Nutrition Planner for Kenya 🇰🇪| [https://nutri-app.streamlit.app/]
An AI-powered web application designed to deliver affordable meal recommendations for Kenyan households, aligning with SDG 2: Zero Hunger. Developed as a bootcamp final project, this tool uses linear programming to optimize daily nutrition by prioritizing user-owned foods, staying within budget constraints, and incorporating Kenyan staples.

✨ Features

Custom Food Input: Users can input owned foodstuffs (e.g., "Maize Flour, 1 kg") and costs for purchasing additional quantities.
Dynamic Price Updates: Scrapes real-time prices from Naivas.online, with fallback to default prices if scraping fails.
Custom Food Nutrients: Retrieves nutritional data for new foods via the USDA FoodData Central API.
Dietary Preferences: Supports vegetarian diets and food exclusions (e.g., peanuts for allergies or fish for cultural preferences).
Visualization: Displays a bar chart of nutrient contributions (calories, protein, iron, vitamins A/C).
Kenyan Recipes: Suggests culturally relevant dishes like ugali na sukuma wiki based on recommendations.
Public Hosting: Deployed on Streamlit Community Cloud for free, accessible worldwide.


🛠️ Setup Instructions
Prerequisites

Python 3.10+ (python.org)
Git (git-scm.com)
VS Code (code.visualstudio.com) with Python extension

Local Setup

Clone the Repository:git clone https://github.com/yourusername/nutrition-app.git
cd nutrition-app


Create a Virtual Environment:python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt


Run the App:streamlit run app.py

Access at http://localhost:8501.


🚀 Deployment
Deploy the app publicly for free using Streamlit Community Cloud:

Push to GitHub:
Ensure requirements.txt and app.py are in your repo.
Run:git add .
git commit -m "Deploy nutrition app"
git push origin main




Deploy on Streamlit Cloud:
Visit share.streamlit.io.
Connect your GitHub repo, select main branch, set app.py as the main file.
Click "Deploy!" to get a public URL (e.g., https://nutrition-app.streamlit.app).


Manage: Monitor logs or reboot via the Streamlit dashboard if needed.


📖 Usage

Set Budget: Choose a daily budget (e.g., KES 300) using the slider.
Add Owned Foods: Input foods you have (e.g., "Maize Flour", 1 kg, cost KES 110 for more).
Set Preferences: Select vegetarian or exclude foods (e.g., peanuts for allergies).
Get Recommendations: Click "Get Recommendations" to view diet plan, nutrient chart, and recipes.
Update Prices: Click "Fetch Latest Prices" to scrape from Naivas (optional).


🧑‍💻 Tech Stack

Python: Core programming language.
PuLP: Linear programming for diet optimization.
Streamlit: Interactive web interface.
Pandas: Data processing and visualization.
Requests/BeautifulSoup: Web scraping for prices.
USDA FoodData Central API: Nutrient data for custom foods.


📊 Data Sources

Foods: Kenyan staples (e.g., maize flour, sukuma wiki, beans).
Costs: Estimated 2025 prices (e.g., maize flour ~KES 110/kg) from Naivas.online, KNBS, and market trends.
Nutrients: Calories, protein, iron, vitamins A/C, sourced from USDA/FAO data.
Note: Update costs/nutrients with local market data or APIs for higher accuracy.


⚠️ Limitations

Web scraping may fail if Naivas.online changes structure (defaults used as fallback).
USDA API uses a demo key (limited requests; obtain a free key for production at fdc.nal.usda.gov).
Simplified nutrient set; expand with local Kenyan food composition data for precision.


🌱 Future Enhancements

Add more Kenyan recipes (e.g., ndengu curry, githeri).
Optimize for mobile devices to reach rural users.
Include carbon footprint metrics for sustainable food choices.
Integrate additional APIs (e.g., Numbeo for prices).


🌍 SDG 2 Impact
This app empowers low-income Kenyan households to maximize nutrition using owned foods, reducing waste and costs. By recommending affordable, nutrient-rich meals tailored to local diets, it addresses malnutrition and supports Zero Hunger.

👤 Author
[John Muli]PLP Python Programming Final Project, September 2025

📜 License
MIT License. Free to use, modify, and share.
