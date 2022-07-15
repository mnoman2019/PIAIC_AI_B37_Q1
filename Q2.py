# 2. Below statements define the second assignment.
# a. Input max marks for Physics, Chemistry, Math, English, Urdu e.g. 100.

phy_marks = int(input('Please enter max marks for Physics\n'))
chem_marks = int(input('Please enter max marks for Chemistry\n'))
math_marks = int(input('Please enter max marks for Math\n'))
eng_marks = int(input('Please enter max marks for English\n'))
urdu_marks = int(input('Please enter max marks for Urdu\n'))

# b. Input obtained marks for above mentioned subjects e.g. 89

obt_phy_marks = int(input('Please enter obtained marks for Physics\n'))
obt_chem_marks = int(input('Please enter obtained marks for Chemistry\n'))
obt_math_marks = int(input('Please enter obtained marks for Math\n'))
obt_eng_marks = int(input('Please enter obtained marks for English\n'))
obt_urdu_marks = int(input('Please enter obtained marks for Urdu\n'))

# c. Calculate total for max and obtained marks e.g. 500 and 482, respectively.

total_marks = phy_marks + chem_marks + math_marks + eng_marks + urdu_marks
obt_total_marks = obt_phy_marks + obt_chem_marks + obt_math_marks + obt_eng_marks + obt_urdu_marks

# d. Print a mark sheet e.g. as below

print("Subject"," Max Marks","  Obtained marks\n")
print(f'Physics     {phy_marks}          {obt_phy_marks}')
print(f'Chemistry   {chem_marks}         {obt_chem_marks}')
print(f'Math        {math_marks}         {obt_math_marks}')
print(f'English     {eng_marks}          {obt_eng_marks}')
print(f'Urdu        {urdu_marks}         {obt_urdu_marks}')
print(f'Total.      {total_marks}        {obt_total_marks}')
print(f'Obtained percentage: {(obt_total_marks*100)/total_marks}')