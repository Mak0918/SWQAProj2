def calculate_bmi(height_feet, height_in, weight_lbs):
    """
    Calculate BMI using height in feet and inches, and weight in pounds.
    """
    height = height_feet * 12 + height_in  # convert feet and inches to total inches
    weight_kg = weight_lbs / 2.205  # convert pounds to kilograms
    bmi = weight_kg / ((height/100) ** 2)  # calculate BMI using kg and meters
    return round(bmi, 1)  # round to 1 decimal place

def get_bmi_category(bmi):
    """
    Returns BMI category based on BMI value
    """
    if bmi < 18.50:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function that prompts the user for their weight and height and calculates BMI
    """
    weight_lbs = float(input("Enter your weight in Pounds: "))
    height_feet = float(input("Enter your height in feet: "))
    height_in = float(input("Enter your height in inches: "))
    bmi = calculate_bmi(weight_lbs, height_in, height_feet)
    bmi_category = get_bmi_category(bmi)
    print("Your BMI is {:.2f}, which is {}".format(bmi, bmi_category))

if __name__ == '__main__':
    main()
