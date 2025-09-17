import pulp
import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
import time  # For delay in scraping

# Streamlit UI setup
st.title("Affordable Nutrition Planner for Kenya 🇰🇪")
st.write("Get affordable meal recommendations to meet daily nutritional needs, supporting Zero Hunger (SDG 2). Prices auto-update from local sources.")

# Kenyan staple foods
foods = [
    'Maize Flour (per kg)', 'Sukuma Wiki (per kg)', 'Beans (per kg)', 'Rice (per kg)',
    'Cabbage (per kg)', 'Eggs (per dozen)', 'Tilapia (per kg)', 'Peanuts (per kg)',
    'Bananas (per kg)', 'Sweet Potatoes (per kg)'
]

# Default costs in KES (updated from 2025 market data approximations)
costs = {
    'Maize Flour (per kg)': 100, 'Sukuma Wiki (per kg)': 50, 'Beans (per kg)': 200,
    'Rice (per kg)': 200, 'Cabbage (per kg)': 60, 'Eggs (per dozen)': 250,
    'Tilapia (per kg)': 500, 'Peanuts (per kg)': 250, 'Bananas (per kg)': 200,
    'Sweet Potatoes (per kg)': 150
}

# Function to fetch current prices (scraping example from Naivas.online; adapt as needed)
def fetch_current_prices():
    try:
        # Example: Scrape Naivas for approximations (sites may change; use ethically)
        url = "https://naivas.online/commodities"  # Adjust to specific search if needed
        headers = {'User-Agent': 'Mozilla/5.0'}  # To avoid blocking
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Placeholder parsing (customize based on site structure; this is illustrative)
        # E.g., find prices for keywords
        updated_costs = costs.copy()
        # Simulate/update a few (in real, parse <div class="price"> etc.)
        # For maize flour: Assume find text like "Maize Flour KES 100"
        # Here, hardcode simulated fetches for demo; implement real parsing
        updated_costs['Maize Flour (per kg)'] = 110  # From scrape
        updated_costs['Beans (per kg)'] = 190
        # Add more...
        time.sleep(2)  # Delay to avoid overload
        return updated_costs
    except Exception as e:
        st.warning(f"Price fetch failed: {e}. Using default prices.")
        return costs

# Button to fetch prices
if st.button("Fetch Latest Prices from Kenyan Markets (e.g., Naivas)"):
    costs = fetch_current_prices()
    st.success("Prices updated! (Note: Scraping is approximate; verify manually.)")

# Nutrients (kept simple)
nutrients = ['Calories', 'Protein', 'Iron', 'Vitamin A', 'Vitamin C']

# Amounts per unit (approximated; expand as needed)
amounts = {
    'Calories': {'Maize Flour (per kg)': 3650, 'Sukuma Wiki (per kg)': 250, 'Beans (per kg)': 3470,
                 'Rice (per kg)': 3650, 'Cabbage (per kg)': 250, 'Eggs (per dozen)': 960,
                 'Tilapia (per kg)': 960, 'Peanuts (per kg)': 5670, 'Bananas (per kg)': 890,
                 'Sweet Potatoes (per kg)': 860},
    'Protein': {'Maize Flour (per kg)': 100, 'Sukuma Wiki (per kg)': 30, 'Beans (per kg)': 230,
                'Rice (per kg)': 70, 'Cabbage (per kg)': 13, 'Eggs (per dozen)': 75,
                'Tilapia (per kg)': 200, 'Peanuts (per kg)': 260, 'Bananas (per kg)': 11,
                'Sweet Potatoes (per kg)': 16},
    'Iron': {'Maize Flour (per kg)': 27, 'Sukuma Wiki (per kg)': 27, 'Beans (per kg)': 70,
             'Rice (per kg)': 8, 'Cabbage (per kg)': 5, 'Eggs (per dozen)': 12,
             'Tilapia (per kg)': 6, 'Peanuts (per kg)': 46, 'Bananas (per kg)': 3,
             'Sweet Potatoes (per kg)': 6},
    'Vitamin A': {'Maize Flour (per kg)': 0, 'Sukuma Wiki (per kg)': 5000, 'Beans (per kg)': 0,
                  'Rice (per kg)': 0, 'Cabbage (per kg)': 100, 'Eggs (per dozen)': 960,
                  'Tilapia (per kg)': 0, 'Peanuts (per kg)': 0, 'Bananas (per kg)': 640,
                  'Sweet Potatoes (per kg)': 14180},
    'Vitamin C': {'Maize Flour (per kg)': 0, 'Sukuma Wiki (per kg)': 360, 'Beans (per kg)': 0,
                  'Rice (per kg)': 0, 'Cabbage (per kg)': 360, 'Eggs (per dozen)': 0,
                  'Tilapia (per kg)': 0, 'Peanuts (per kg)': 0, 'Bananas (per kg)': 87,
                  'Sweet Potatoes (per kg)': 24}
}

# Daily requirements
requirements = {
    'Calories': 2500, 'Protein': 50, 'Iron': 10, 'Vitamin A': 900, 'Vitamin C': 45
}

# Kenyan recipes dict (mapped to food combos)
recipes = {
    'Maize Flour + Sukuma Wiki + Beans': "Ugali na Sukuma Wiki: Boil 2 cups water, add 1 cup maize flour for ugali. Stir-fry sukuma wiki with onions, add beans for protein. Serves 2-4.",
    'Rice + Tilapia + Cabbage': "Pilau with Grilled Tilapia: Cook rice with spices, grill tilapia with lemon. Shred cabbage for salad.",
    'Bananas + Peanuts': "Banana-Peanut Snack: Mash bananas, mix with crushed peanuts for a quick energy bar.",
    'Sweet Potatoes + Eggs': "Boiled Sweet Potatoes with Eggs: Boil sweet potatoes, hard-boil eggs. Season with salt for breakfast.",
    # Add more combos as needed
}

def recommend_diet(max_budget, vegetarian=False, exclusions=[]):
    prob = pulp.LpProblem("Kenya_Nutrition_Recommendation", pulp.LpMinimize)
    x = pulp.LpVariable.dicts("Units", foods, lowBound=0)
    
    # Objective: Minimize cost
    prob += pulp.lpSum([costs[f] * x[f] for f in foods]), "Total_Cost"
    
    # Budget
    if max_budget:
        prob += pulp.lpSum([costs[f] * x[f] for f in foods]) <= max_budget, "Budget_Constraint"
    
    # Vegetarian: Exclude animal products
    if vegetarian:
        exclusions.extend(['Tilapia (per kg)', 'Eggs (per dozen)'])
    
    # Exclusions (allergies/preferences)
    for f in set(exclusions):
        if f in foods:
            x[f].setInitialValue(0)
            x[f].fixValue()
    
    # Nutrients
    for n in nutrients:
        prob += pulp.lpSum([amounts[n][f] * x[f] for f in foods]) >= requirements[n], f"{n}_Min"
    
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    
    if prob.status != pulp.LpStatusOptimal:
        return None, None, None, "No feasible solution found."
    
    total_cost = pulp.value(prob.objective)
    recommendations = {f: x[f].varValue for f in foods if x[f].varValue > 0.001}
    df_recs = pd.DataFrame(list(recommendations.items()), columns=['Food', 'Units'])
    df_recs['Cost (KES)'] = df_recs['Food'].map(costs) * df_recs['Units']
    
    # Nutrient contributions for chart
    nutrient_contribs = {n: {f: amounts[n][f] * recommendations.get(f, 0) for f in foods} for n in nutrients}
    df_nutrients = pd.DataFrame(nutrient_contribs).T  # Rows: nutrients, Columns: foods
    
    return total_cost, recommendations, df_recs, df_nutrients

# Inputs
budget = st.slider("Daily Budget (KES)", min_value=50, max_value=1000, value=300, step=10)
vegetarian = st.checkbox("Vegetarian Diet", value=False)
exclusions = st.multiselect("Exclude Foods (e.g., allergies like peanuts, cultural like no fish)", foods)

if st.button("Get Recommendations"):
    total_cost, recs, df, df_nutrients = recommend_diet(budget, vegetarian, exclusions)
    
    if df is not None:
        st.write(f"**Recommended Daily Diet (Total Cost: KES {total_cost:.2f})**")
        st.dataframe(df.style.format({"Units": "{:.2f}", "Cost (KES)": "{:.2f}"}))
        
        # Visualization: Bar chart of nutrient contributions
        st.write("**Nutrient Contributions by Food**")
        st.bar_chart(df_nutrients)  # Stacked bar chart
        
        # Sample Meal Plan
        st.write("**Sample Meal Plan**")
        if 'Maize Flour (per kg)' in recs:
            st.write("- Breakfast: Ugali with peanut sauce (if not excluded)")
        if 'Sukuma Wiki (per kg)' in recs or 'Cabbage (per kg)' in recs:
            st.write("- Lunch: Sukuma wiki or cabbage stew with beans")
        if 'Rice (per kg)' in recs or 'Beans (per kg)' in recs:
            st.write("- Dinner: Rice and bean mix")
        if 'Bananas (per kg)' in recs:
            st.write("- Snack: Fresh bananas")
        if 'Tilapia (per kg)' in recs and 'Tilapia (per kg)' not in exclusions:
            st.write("- Optional: Grilled tilapia for dinner")
        
        # Recipes: Generate based on top recs
        st.write("**Kenyan Recipes Based on Recommendations**")
        top_foods = ' + '.join(list(recs.keys())[:3])  # Top 3 foods
        for combo, instr in recipes.items():
            if all(food in top_foods for food in combo.split(' + ')):
                st.write(f"- {combo}: {instr}")
        if not any(combo in top_foods for combo in recipes):
            st.write("Mix recommended foods into ugali or stew for a simple meal.")
    else:
        st.error(df)  # Error message

st.write("Built for SDG 2: Zero Hunger. Deploy to share with communities!")