temp = int(input("Please enter the current temperature: "))
if temp > 90:
    print("Wear shorts")
else:

    if 90 > temp > 70:
        print("Short Sleeves are fine")
    else:
    
        if 70 > temp > 50:
            print("Wear a jacket")
        else:

            if 50 > temp > 32:
                print("Wear a heavy coat")
            else:

                if 32 > temp:
                    print("Stay inside")
                
