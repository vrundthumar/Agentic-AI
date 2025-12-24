# 🔐 OTP Verification Logic using Python

import random

Generate_otp = random.randint(100000, 999999)
print(f"Your OTP: {Generate_otp}")

User_otp = int(input("Enter OTP : "))

if Generate_otp == User_otp:
    print("✅ OTP verified successfully")
else:
    print("❌ Invalid OTP")  

# OUTPUT
# Your OTP: 835153
# Enter OTP : 835153
# ✅ OTP verified successfully    

# Your OTP: 355964
# Enter OTP : 123456
# ❌ Invalid OTP