# ==========================================================
#             PASSWORD STRENGTH CHECKER PRO v1.0
#               Developed by: Dharani
# ==========================================================

print("=" * 60)
print("              PASSWORD STRENGTH CHECKER PRO")
print("=" * 60)

print()

password = input("Enter Password: ")

print()
print("Analyzing Password...")
print("-" * 60)

# ----------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------

length = len(password)

upper_count = 0
lower_count = 0
number_count = 0
special_count = 0

# ----------------------------------------------------------
# COUNT CHARACTERS
# ----------------------------------------------------------

for char in password:

    if char.isupper():
        upper_count += 1

    elif char.islower():
        lower_count += 1

    elif char.isdigit():
        number_count += 1

    else:
        special_count += 1

# ----------------------------------------------------------
# SECURITY CHECKS
# ----------------------------------------------------------

length_ok = length >= 8
upper_ok = upper_count > 0
lower_ok = lower_count > 0
number_ok = number_count > 0
special_ok = special_count > 0

print("Security Checks")

print()

print("Length (8+)            :", "PASS" if length_ok else "FAIL")
print("Uppercase Letter       :", "PASS" if upper_ok else "FAIL")
print("Lowercase Letter       :", "PASS" if lower_ok else "FAIL")
print("Number                 :", "PASS" if number_ok else "FAIL")
print("Special Character      :", "PASS" if special_ok else "FAIL")

print("-" * 60)

# ----------------------------------------------------------
# PASSWORD STATISTICS
# ----------------------------------------------------------

print("Password Statistics")

print()

print("Password Length        :", length)
print("Uppercase Letters      :", upper_count)
print("Lowercase Letters      :", lower_count)
print("Numbers                :", number_count)
print("Special Characters     :", special_count)

print("-" * 60)

# ----------------------------------------------------------
# SCORE
# ----------------------------------------------------------

score = 0

if length_ok:
    score += 30

if upper_ok:
    score += 20

if lower_ok:
    score += 15

if number_ok:
    score += 15

if special_ok:
    score += 20

# ----------------------------------------------------------
# RATING
# ----------------------------------------------------------

if score >= 95:
    rating = "★★★★★"

elif score >= 80:
    rating = "★★★★☆"

elif score >= 60:
    rating = "★★★☆☆"

elif score >= 40:
    rating = "★★☆☆☆"

else:
    rating = "★☆☆☆☆"

# ----------------------------------------------------------
# PASSWORD STRENGTH
# ----------------------------------------------------------

if score >= 80:
    strength = "VERY STRONG"

elif score >= 60:
    strength = "STRONG"

elif score >= 40:
    strength = "MEDIUM"

else:
    strength = "WEAK"

# ----------------------------------------------------------
# STRENGTH METER
# ----------------------------------------------------------

bars = score // 10

meter = "█" * bars + "░" * (10 - bars)

print("Password Score         :", score, "/100")

print("Password Rating        :", rating)

print("Password Strength      :", strength)

print()

print("Strength Meter")

print(meter, str(score) + "%")

print("-" * 60)

# ----------------------------------------------------------
# SUGGESTIONS
# ----------------------------------------------------------

print("Suggestions")

suggestions = []

if not length_ok:
    suggestions.append("Increase password length to at least 8 characters.")

if not upper_ok:
    suggestions.append("Add at least one uppercase letter.")

if not lower_ok:
    suggestions.append("Add at least one lowercase letter.")

if not number_ok:
    suggestions.append("Add at least one number.")

if not special_ok:
    suggestions.append("Add at least one special character.")

if len(suggestions) == 0:

    print()

    print("Excellent Password!")

    print("No improvements required.")

else:

    print()

    for item in suggestions:

        print("-", item)

print("-" * 60)

# ----------------------------------------------------------
# FINAL REPORT
# ----------------------------------------------------------

print("PASSWORD SECURITY REPORT")

print()

print("Password Length        :", length)

print("Uppercase Letters      :", upper_count)

print("Lowercase Letters      :", lower_count)

print("Numbers                :", number_count)

print("Special Characters     :", special_count)

print()

print("Final Score            :", score, "/100")

print("Rating                 :", rating)

print("Strength               :", strength)

print("=" * 60)

print("Thank You For Using Password Strength Checker Pro")

print("=" * 60)