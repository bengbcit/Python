
'''
def BMI_Calculator():
    weight = float(input("Please enter the weight(Kg): "))
    #weight = int(weight)
    height = float(input("Please enter the height(m): "))

    BMI_value = weight / (height ** 2)
    
    if BMI_value < 18.5:
        print("Your BMI is " + str(BMI_value) + ". You are underweight.")
    elif BMI_value >= 18.5 and BMI_value < 25:
        print("Your BMI is " + str(BMI_value) + ". You are normal weight.")
    elif BMI_value >= 25 and BMI_value < 30:
        print("Your BMI is " + str(BMI_value) + ". You are overweight.")
    else:
        print("Your BMI is " + str(BMI_value) + ". You are obese.")
    

BMI_Calculator()
'''
def calculate_bmi():
    try:
        # 身長(cm)と体重(kg)を入力
        height_cm = float(input("身長を入力してください（cm）："))
        weight = float(input("体重を入力してください（kg）："))

        # 身長をmに変換
        height_m = height_cm / 100

        # BMI計算
        bmi = weight / (height_m ** 2)

        # 結果表示
        print(f"あなたのBMIは {bmi:.1f} です。")

        # 判定
        if bmi < 18.5:
            print("判定：低体重（やせ型）")
        elif 18.5 <= bmi < 25:
            print("判定：普通体重")
        elif 25 <= bmi < 30:
            print("判定：肥満（1度）")
        else:
            print("判定：肥満（2度以上）")

    except ValueError:
        print("数値を入力してください。")

# 実行
calculate_bmi()