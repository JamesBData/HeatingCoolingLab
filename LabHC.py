def heating_cooling(actual, desired):

    while actual != desired:
        if actual > desired:
            actual -= 1
            print(f"Run AC:  {actual}")

        elif actual < desired:
            actual += 1
            print(f"Run Heat:  {actual}")

    if actual == desired:
        print("Standby")

heating_cooling(50, 40)