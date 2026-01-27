"""
Paper Weight (GSM) Conversion Examples
=======================================

This module demonstrates GSM (grams per square meter) conversions for paper,
fabric, and other sheet materials.

Units Covered:
- GSM (g/m²) - International standard for paper weight
- kg/m² - Heavier materials
- lb/ft² - Imperial unit
- oz/yd² - Fabric weight (US)

Author: Unifyt Team
Date: 2025-01-27
"""

from unifyt import Quantity
import sys


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def paper_types_gsm():
    """Show common paper types and their GSM values."""
    print_header("Common Paper Types and GSM Values")
    
    papers = [
        ("Tissue Paper", 10, 20, "Facial tissue, gift wrap"),
        ("Newsprint", 40, 50, "Newspapers"),
        ("Copy Paper (Standard)", 70, 80, "Office printing, photocopying"),
        ("Bond Paper", 80, 90, "Letterhead, forms"),
        ("Brochure Paper", 90, 120, "Marketing materials"),
        ("Lightweight Cardstock", 130, 170, "Business cards, postcards"),
        ("Medium Cardstock", 180, 220, "Greeting cards, invitations"),
        ("Heavy Cardstock", 250, 300, "Covers, packaging"),
        ("Poster Board", 300, 400, "Posters, displays"),
        ("Corrugated Cardboard", 400, 800, "Shipping boxes")
    ]
    
    print(f"\n{'Paper Type':<30} {'GSM Range':<15} {'kg/m²':<15} {'Application'}")
    print("-" * 90)
    
    for paper_type, gsm_low, gsm_high, application in papers:
        gsm_mid = (gsm_low + gsm_high) / 2
        # GSM = g/m² = kg/m² * 0.001
        kg_m2_value = gsm_mid * 0.001
        
        print(f"{paper_type:<30} {gsm_low}-{gsm_high} GSM{'':<5} {kg_m2_value:<15.3f} {application}")


def gsm_conversions():
    """Demonstrate GSM conversions to other units."""
    print_header("GSM Conversion Table")
    
    print("\n--- Common GSM Values to kg/m² and lb/ft² ---")
    
    gsm_values = [60, 70, 80, 90, 100, 120, 150, 180, 200, 250, 300, 400, 500]
    
    print(f"\n{'GSM':<10} {'kg/m²':<15} {'lb/ft²':<15} {'oz/yd²':<15}")
    print("-" * 60)
    
    for gsm in gsm_values:
        # GSM = g/m² = kg/m² * 0.001
        kg_m2_value = gsm * 0.001
        
        # Convert to lb/ft²: 1 kg/m² = 0.2048 lb/ft²
        lb_ft2_value = kg_m2_value * 0.2048
        
        # Convert to oz/yd²: 1 g/m² = 0.0295 oz/yd²
        oz_yd2_value = gsm * 0.0295
        
        print(f"{gsm:<10} {kg_m2_value:<15.3f} {lb_ft2_value:<15.4f} {oz_yd2_value:<15.2f}")


def calculate_paper_weight():
    """Calculate total weight of paper sheets."""
    print_header("Paper Weight Calculations")
    
    print("\n--- Weight of Paper Reams ---")
    print("Standard paper sizes and ream weights")
    
    # A4 paper: 210mm × 297mm = 0.062370 m²
    a4_area = 0.210 * 0.297  # m²
    
    # Letter paper: 8.5" × 11" = 0.060387 m²
    letter_area = 0.2159 * 0.2794  # m²
    
    paper_configs = [
        ("A4", a4_area, 80, 500, "Standard office paper"),
        ("A4", a4_area, 100, 500, "Premium copy paper"),
        ("Letter", letter_area, 75, 500, "US standard paper"),
        ("Letter", letter_area, 90, 500, "US premium paper"),
        ("A3", a4_area * 2, 80, 250, "Large format"),
        ("Cardstock A4", a4_area, 200, 250, "Business cards")
    ]
    
    print(f"\n{'Size':<15} {'GSM':<8} {'Sheets':<10} {'Total Weight':<20} {'Application'}")
    print("-" * 80)
    
    for size, area, gsm, sheets, application in paper_configs:
        # GSM = g/m², so weight per sheet = gsm * area / 1000 (in kg)
        weight_per_sheet_kg = (gsm * area) / 1000.0
        total_weight_kg = weight_per_sheet_kg * sheets
        total_weight = Quantity(total_weight_kg, 'kilogram')
        
        print(f"{size:<15} {gsm:<8} {sheets:<10} {total_weight_kg:<8.2f} kg ({total_weight.to('pound').magnitude:.2f} lb)  {application}")


def fabric_weights():
    """Show fabric weights in GSM."""
    print_header("Fabric Weights (GSM)")
    
    fabrics = [
        ("Sheer Chiffon", 30, 50, "Scarves, overlays"),
        ("Lightweight Cotton", 80, 120, "Summer shirts, dresses"),
        ("Medium Cotton", 130, 180, "T-shirts, casual wear"),
        ("Denim (Light)", 200, 280, "Light jeans, jackets"),
        ("Denim (Medium)", 300, 400, "Regular jeans"),
        ("Denim (Heavy)", 450, 600, "Heavy-duty jeans, workwear"),
        ("Canvas (Light)", 200, 300, "Bags, light upholstery"),
        ("Canvas (Heavy)", 400, 600, "Tents, heavy bags"),
        ("Fleece", 200, 300, "Jackets, blankets"),
        ("Terry Cloth", 400, 600, "Towels, bathrobes")
    ]
    
    print(f"\n{'Fabric Type':<25} {'GSM Range':<15} {'oz/yd²':<15} {'Application'}")
    print("-" * 80)
    
    for fabric_type, gsm_low, gsm_high, application in fabrics:
        gsm_mid = (gsm_low + gsm_high) / 2
        # Convert GSM to oz/yd²
        # 1 g/m² = 0.0295 oz/yd²
        oz_yd2_value = gsm_mid * 0.0295
        
        print(f"{fabric_type:<25} {gsm_low}-{gsm_high} GSM{'':<5} {oz_yd2_value:<15.2f} {application}")


def printing_specifications():
    """Show printing industry GSM specifications."""
    print_header("Printing Industry GSM Specifications")
    
    print("\n--- Print Product Specifications ---")
    
    products = [
        ("Business Card", 300, 350, "Standard thickness"),
        ("Postcard", 250, 300, "Mailing postcards"),
        ("Flyer", 130, 170, "Promotional materials"),
        ("Brochure (Inside)", 115, 150, "Multi-page brochures"),
        ("Brochure (Cover)", 200, 250, "Brochure covers"),
        ("Magazine (Inside)", 80, 115, "Magazine pages"),
        ("Magazine (Cover)", 150, 200, "Magazine covers"),
        ("Book (Pages)", 70, 90, "Novel pages"),
        ("Book (Cover)", 200, 300, "Paperback covers"),
        ("Poster", 150, 200, "Indoor posters"),
        ("Banner", 300, 500, "Outdoor banners"),
        ("Packaging", 250, 400, "Product boxes")
    ]
    
    print(f"\n{'Product':<25} {'GSM Range':<15} {'kg/m²':<15} {'Notes'}")
    print("-" * 80)
    
    for product, gsm_low, gsm_high, notes in products:
        gsm_mid = (gsm_low + gsm_high) / 2
        kg_m2_value = gsm_mid * 0.001
        
        print(f"{product:<25} {gsm_low}-{gsm_high} GSM{'':<5} {kg_m2_value:<15.3f} {notes}")


def cost_calculations():
    """Calculate paper costs based on GSM and area."""
    print_header("Paper Cost Calculations")
    
    print("\n--- Cost per Sheet Based on GSM ---")
    print("Assuming paper cost of $5.00 per kg")
    
    cost_per_kg = 5.00  # dollars
    a4_area = 0.210 * 0.297  # m²
    
    gsm_values = [70, 80, 90, 100, 120, 150, 200, 250, 300]
    
    print(f"\n{'GSM':<10} {'Weight/Sheet':<15} {'Cost/Sheet':<15} {'Cost/500 Sheets':<20}")
    print("-" * 70)
    
    for gsm in gsm_values:
        # GSM = g/m², weight per sheet in kg = gsm * area / 1000
        weight_per_sheet_kg = (gsm * a4_area) / 1000.0
        cost_per_sheet = weight_per_sheet_kg * cost_per_kg
        cost_per_ream = cost_per_sheet * 500
        
        print(f"{gsm:<10} {weight_per_sheet_kg*1000:<15.2f} g {cost_per_sheet:<15.4f} $ ${cost_per_ream:<20.2f}")


def environmental_impact():
    """Show environmental impact based on paper weight."""
    print_header("Environmental Impact - Paper Weight")
    
    print("\n--- CO2 Emissions by Paper Weight ---")
    print("Estimated CO2 emissions: 1.3 kg CO2 per kg of paper produced")
    
    co2_per_kg = 1.3  # kg CO2 per kg paper
    a4_area = 0.210 * 0.297  # m²
    sheets_per_year = 10000  # typical office usage
    
    gsm_values = [70, 80, 90, 100]
    
    print(f"\n{'GSM':<10} {'Paper/Year':<15} {'CO2/Year':<15} {'Trees/Year':<15}")
    print("-" * 65)
    print("(Based on 10,000 sheets per year)")
    
    for gsm in gsm_values:
        # GSM = g/m², weight per sheet in kg = gsm * area / 1000
        weight_per_sheet_kg = (gsm * a4_area) / 1000.0
        total_paper_kg = weight_per_sheet_kg * sheets_per_year
        total_co2_kg = total_paper_kg * co2_per_kg
        trees = total_paper_kg / 8.0  # Rough estimate: 8kg paper per tree
        
        print(f"{gsm:<10} {total_paper_kg:<15.1f} kg {total_co2_kg:<15.1f} kg {trees:<15.2f}")
    
    print("\nNote: Using lighter weight paper can significantly reduce environmental impact!")


def interactive_mode():
    """Interactive GSM converter."""
    print_header("Interactive GSM Converter")
    
    print("\nConversion options:")
    print("  1. GSM to other units")
    print("  2. Calculate paper ream weight")
    print("  3. Calculate fabric weight for area")
    
    try:
        choice = input("\nSelect option (1-3): ").strip()
        
        if choice == '1':
            gsm = float(input("Enter GSM value: "))
            # GSM = g/m² = kg/m² * 0.001
            kg_m2 = gsm * 0.001
            # Convert to lb/ft² and oz/yd²
            lb_ft2 = kg_m2 * 0.2048  # 1 kg/m² = 0.2048 lb/ft²
            oz_yd2 = gsm * 0.0295  # 1 g/m² = 0.0295 oz/yd²
            
            print(f"\n{gsm} GSM equals:")
            print(f"  → {kg_m2:.4f} kg/m²")
            print(f"  → {lb_ft2:.4f} lb/ft²")
            print(f"  → {oz_yd2:.2f} oz/yd²")
            
        elif choice == '2':
            gsm = float(input("Enter paper GSM: "))
            sheets = int(input("Enter number of sheets: "))
            
            size_choice = input("Paper size (1=A4, 2=Letter): ").strip()
            area = 0.210 * 0.297 if size_choice == '1' else 0.2159 * 0.2794
            
            # GSM = g/m², weight per sheet in kg = gsm * area / 1000
            weight_per_sheet_kg = (gsm * area) / 1000.0
            total_weight_kg = weight_per_sheet_kg * sheets
            total_weight = Quantity(total_weight_kg, 'kilogram')
            
            print(f"\nTotal weight of {sheets} sheets:")
            print(f"  → {total_weight}")
            print(f"  → {total_weight.to('pound')}")
            
        elif choice == '3':
            gsm = float(input("Enter fabric GSM: "))
            length = float(input("Enter length (meters): "))
            width = float(input("Enter width (meters): "))
            
            area = length * width
            # GSM = g/m², total weight in kg = gsm * area / 1000
            total_weight_kg = (gsm * area) / 1000.0
            total_weight = Quantity(total_weight_kg, 'kilogram')
            
            print(f"\nFabric weight for {length}m × {width}m ({area} m²):")
            print(f"  → {total_weight}")
            print(f"  → {total_weight.to('pound')}")
        
        else:
            print("Invalid choice!")
            
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")


def main():
    """Main function to run all examples."""
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_mode()
    else:
        print("=" * 80)
        print("  PAPER WEIGHT (GSM) CONVERSION EXAMPLES")
        print("  Using Unifyt Library")
        print("=" * 80)
        
        paper_types_gsm()
        gsm_conversions()
        calculate_paper_weight()
        fabric_weights()
        printing_specifications()
        cost_calculations()
        environmental_impact()
        
        print("\n" + "=" * 80)
        print("  Run with --interactive flag for interactive mode")
        print("=" * 80)


if __name__ == "__main__":
    main()
