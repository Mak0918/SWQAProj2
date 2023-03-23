def calculate_bmi(height_feet, height_in, weight_lb):
    """
    Calculate BMI using height in feet and inches, and weight in pounds.
    """
    weight_kg = 70
    height_m = 1.75

    height_feet = height_in / 12  # convert feet and inches to total inches
    weight_lb = weight_kg * 2.20462  # convert pounds to kilograms
    height_in = height_m * 39.3701  #convert meters to inches
    bmi = (weight_lb / (height_in ** 2)) * 703  # calculate BMI using kg and meters
    return bmi

UNDERWEIGHT = '<18.5'
NORMAL_WEIGHT = '18.5–24.9'
OVERWEIGHT = '25–29.9'
OBESE = '>=30'


def get_bmi_category(bmi):
    """
    Returns BMI category based on BMI value
    """
    if bmi < 18.50:
        return UNDERWEIGHT
    elif bmi < 24.9:
        return NORMAL_WEIGHT
    elif bmi <= 30.0:
        return OVERWEIGHT
    else:
        return OBESE

def main():
    """
    Main function that prompts the user for their weight and height and calculates BMI
    """
    weight_lb = float(input("Enter your weight in Pounds: "))
    height_feet = float(input("Enter your height in feet: "))
    height_in = float(input("Enter your height in inches: "))
    bmi = calculate_bmi(weight_lb, height_in, height_feet)
    bmi_category = get_bmi_category(bmi)
    #print("Your BMI is {:.2f}, which is {}".format bmi 12 ** 2), bmi_category
    print("BMI: {:.2f} (lbs/inch^2)".format(bmi, bmi_category))
if __name__ == '__main__':
    main()