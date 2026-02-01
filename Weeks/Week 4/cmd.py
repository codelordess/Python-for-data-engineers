import sys
if (len(sys.argv) == 1):
    print("This module is not intended to be run as a script. Please run the appropriate example files instead.")
else:
    password = sys.argv[1] 
    print(f"Password received: {password}")    
sys.exit()