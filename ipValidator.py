ipAddress = input("Enter IP V4 address")
if ipAddress.count(".") == 3:
    segments = ipAddress.split(".")
    if segments[0].isdigit():
        if 0 <= int(segments[0]) <= 255:
            if segments[1].isdigit():
                if 0 <= int(segments[1]) <= 255:
                    if segments[2].isdigit():
                        if 0 <= int(segments[2]) <= 255:
                            if segments[3].isdigit():
                                if 0 <= int(segments[3]) <= 255:
                                    print("valid IP IP, enter int")
                                else:
                                    print("Not valid IP, enter num between 0-255")
                            else:
                                print("Not valid IP, enter int")
                        else:
                            print("Not valid IP, enter num between 0-255")
                    else:
                        print("Not valid IP, enter int")
                else:
                    print("Not a valid IP,enter num between 0-255")
            else:
                print("Not valid IP, enter int")
        else:
            print("Not a valid IP, enter num between 0-255")
    else:
        print("Not valid IP, enter int")
else:
    print("Not a valid IP, enter 3 parts")
