import os

def create_knowledge_base_structure():
    """Create the full folder structure and sample placeholder Markdown files for the FarmSakha AI knowledge base"""

    # Define main folder structure with subfolders
    folders = [
        "knowledge_base/01_crop_advisory/crop_selection_by_soil",
        "knowledge_base/01_crop_advisory",
        "knowledge_base/02_soil_health",
        "knowledge_base/03_pest_disease_management/common_pests",
        "knowledge_base/03_pest_disease_management",
        "knowledge_base/04_weather_climate",
        "knowledge_base/05_fertilizer_nutrition/npk_ratios",
        "knowledge_base/05_fertilizer_nutrition",
        "knowledge_base/06_market_economics",
        "knowledge_base/07_government_schemes/subsidies",
        "knowledge_base/07_government_schemes",
        "knowledge_base/08_sustainable_practices",
        "knowledge_base/09_regional_specific/north_india",
        "knowledge_base/09_regional_specific",
        "knowledge_base/10_multilingual_content/hindi",
        "knowledge_base/10_multilingual_content/punjabi",
        "knowledge_base/10_multilingual_content/bengali",
        "knowledge_base/10_multilingual_content/tamil",
        "knowledge_base/10_multilingual_content/telugu",
        "knowledge_base/10_multilingual_content/marathi",
        "knowledge_base/10_multilingual_content/gujarati"
    ]

    # Create folders recursively
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    # Define sample placeholder Markdown files with minimal content
    sample_files = {
        "knowledge_base/01_crop_advisory/crop_selection_by_soil/clay_soil.md": "# Clay Soil Crop Recommendations\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/01_crop_advisory/crop_selection_by_soil/sandy_soil.md": "# Sandy Soil Crop Recommendations\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/01_crop_advisory/crop_selection_by_soil/loamy_soil.md": "# Loamy Soil Crop Recommendations\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/01_crop_advisory/seasonal_recommendations.md": "# Seasonal Recommendations\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/01_crop_advisory/nutrient_management.md": "# Nutrient Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/01_crop_advisory/irrigation_guidelines.md": "# Irrigation Guidelines\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/02_soil_health/soil_types_india.md": "# Soil Types of India\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/02_soil_health/soil_testing.md": "# Soil Testing\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/02_soil_health/organic_matter.md": "# Organic Matter\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/02_soil_health/ph_management.md": "# pH Management\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/03_pest_disease_management/common_pests/aphids.md": "# Aphid Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/03_pest_disease_management/common_pests/bollworm.md": "# Bollworm Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/03_pest_disease_management/plant_diseases.md": "# Plant Diseases\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/03_pest_disease_management/integrated_pest_management.md": "# Integrated Pest Management (IPM)\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/03_pest_disease_management/biological_control.md": "# Biological Control\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/04_weather_climate/seasonal_patterns.md": "# Seasonal Patterns\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/04_weather_climate/climate_risk_management.md": "# Climate Risk Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/04_weather_climate/drought_management.md": "# Drought Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/04_weather_climate/flood_preparedness.md": "# Flood Preparedness\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/05_fertilizer_nutrition/npk_ratios/rice_nutrition.md": "# Rice Nutrition Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/05_fertilizer_nutrition/npk_ratios/wheat_nutrition.md": "# Wheat Nutrition Management\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/05_fertilizer_nutrition/micronutrients.md": "# Micronutrients\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/05_fertilizer_nutrition/organic_fertilizers.md": "# Organic Fertilizers\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/05_fertilizer_nutrition/application_timing.md": "# Fertilizer Application Timing\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/06_market_economics/price_trends.md": "# Price Trends\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/06_market_economics/value_addition.md": "# Value Addition\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/06_market_economics/storage_techniques.md": "# Storage Techniques\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/06_market_economics/supply_chain.md": "# Supply Chain Optimization\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/07_government_schemes/subsidies/pm_kisan.md": "# PM Kisan Subsidy Scheme\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/07_government_schemes/insurance.md": "# Crop Insurance Schemes\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/07_government_schemes/loan_schemes.md": "# Loan Schemes\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/07_government_schemes/support_programs.md": "# Government Support Programs\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/08_sustainable_practices/organic_farming.md": "# Organic Farming\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/08_sustainable_practices/water_conservation.md": "# Water Conservation\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/08_sustainable_practices/crop_rotation.md": "# Crop Rotation\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/08_sustainable_practices/agroforestry.md": "# Agroforestry\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/09_regional_specific/north_india/punjab.md": "# Punjab Regional Agriculture\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/09_regional_specific/south_india.md": "# South India Regional Agriculture\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/09_regional_specific/west_india.md": "# West India Regional Agriculture\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/09_regional_specific/east_india.md": "# East India Regional Agriculture\n\n(TODO: Add detailed content here)\n",
        "knowledge_base/09_regional_specific/northeast_india.md": "# Northeast India Regional Agriculture\n\n(TODO: Add detailed content here)\n",

        "knowledge_base/10_multilingual_content/hindi/basic_farming_terms.md": "# Hindi Basic Farming Terms\n\n(TODO: Add detailed content here)\n",
        # Other language folders can have placeholder README.md or index.md if you want to create
    }

    # Write placeholder files
    for filepath, content in sample_files.items():
        # Ensure the folder exists (in case)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {filepath}")

    print("\nKnowledge base folder structure and sample files created successfully!")
    print(f"Total folders created: {len(folders)}")
    print(f"Total sample files created: {len(sample_files)}")

if __name__ == "__main__":
    create_knowledge_base_structure()
