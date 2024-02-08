import random
import string

#ASCII art logos
logo1 = """

 $$$$$$\                      $$\   $$\ $$$$$$$\                                        
$$  __$$\                     $$ |  $$ |$$  __$$\                                       
$$ /  $$ |$$$$$$$\   $$$$$$\  $$ |  $$ |$$ |  $$ |                                      
$$ |  $$ |$$  __$$\ $$  __$$\ $$ |  $$ |$$$$$$$  |                                      
$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$  ____/                                       
$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |                                            
 $$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$  |$$ |            Code                        
 \______/ \__|  \__| \_______| \______/ \__|            Generator                                         
 
           Made By An0m < / >                                                                                
           Discord : cyber_anom                                                                             
                                                                                        

"""

logo2 = """

 $$$$$$\                  $$\               $$\        $$$$$$\                
$$  __$$\                 \$$\             $$  |      $$$ __$$\               
$$ /  $$ |$$$$$$$\         \$$\           $$  /       $$$$\ $$ |$$$$$$\$$$$\  
$$$$$$$$ |$$  __$$\         \$$\ $$$$$$\ $$  /        $$\$$\$$ |$$  _$$  _$$\ 
$$  __$$ |$$ |  $$ |        $$  |\______|\$$<         $$ \$$$$ |$$ / $$ / $$ |
$$ |  $$ |$$ |  $$ |       $$  /          \$$\        $$ |\$$$ |$$ | $$ | $$ |
$$ |  $$ |$$ |  $$ |      $$  /            \$$\       \$$$$$$  /$$ | $$ | $$ |
\__|  \__|\__|  \__|      \__/              \__|       \______/ \__| \__| \__|
                                                                              
             Made By An0m < / > 
             Discord : cyber_anom
                                                                              
                                                                              

                                 
"""

#generate random codes
def generate_codes(num_codes):
    codes = []
    for _ in range(num_codes):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        codes.append(code)
    return codes

#validation
def get_num_codes():
    while True:
        try:
            num_codes = int(input("How many codes do you want to generate? "))
            if num_codes <= 0:
                print("Please enter a positive number.")
            else:
                return num_codes
        except ValueError:
            print("Please enter a valid number.")

#Random logo
chosen_logo = random.choice([logo1, logo2])
print(chosen_logo)

#How Many Codes?????????
num_codes = get_num_codes()

#Generate random codes
codes = generate_codes(num_codes)

#Print generated codes
print("\nGenerated codes:")
for code in codes:
    print(code)

