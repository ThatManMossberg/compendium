# Associates name with code and code with name
hardwareList = {"276-1028-001": "8-32 nut", "8-32 nut": "276-1028-001", "276-4991-001": "8-32*.375 in screw", "8-32 .375 screw": "276-4991-001", "276-5007-001": "8-32*.5 in screw", "276-4996-001": "8-32*1 in screw", "8-32*1 in screw": "276-4996-001"}
electricalList = {"276-4810": "Brain", "brain": "276-4810", "276-4840": "Reg. Servo Motor", "motor": "276-4840", "276-4811": "battery", "battery": "276-4611", "276-4831": "Transmitter", "Transmitter": "276-4831"}
constructionList = {"test": "test"}
while True:
    mode = input("Select Mode: ")
#! Searches hardware
    while True:
        if mode == "hardware":
            print("Enter Part name/code:")
            x = str(input())
            if x in hardwareList:
                print(hardwareList[x])
                print("")
            elif x == "change mode":
                break
            else:
                print("Not registered")
                print("")
#! Searches Electrical
        elif mode == "electrical":
            print("Enter Part name/code: ")
            x = str(input())
            if x in electricalList:
                print(electricalList[x])
                print("")
#! Searches constuction
        elif mode == "construction":
            print("Enter Part name/code: ")
            x = str(input())
            if x in constructionList:
                print(constructionList[x])
                print("")
#? Allows user to see what each mode does
                #Working on it, I promise
        
        if mode == "mode?":
            print("Enter hardware, electrical, construction, or change mode")
            print("")
            x = str(input())
            if x == "hardware":
                print("Hardware")
                break
            x = str(input())
            if x == "electrical":
                print("Electrical")
                break
            x = str(input())
            if x == "construction":
                print("construction")
                break
            x = str(input())
            if x == "change mode":
                break

        

    
# Basic commands 
        elif x == "change mode":
             break
                
        elif mode == "Stop":
            quit()
        else:
            print("Not registered")
            print("")
