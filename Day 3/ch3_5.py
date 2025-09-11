weeks = days = hours = minutes = seconds = 0


print(" *** Transform second ***")
usrinp = input("Enter seconds : ")
try:
    usrinp = int(usrinp.replace("_", ""))
except ValueError:
    print(f"! ! ! please enter a whole number ==> {usrinp}")
    print(f"This number ({usrinp}) is not VALID !!!")
    print("===== End of program =====")
else:
    if usrinp > 0:
        seconds = usrinp

        weeks = seconds // (7 * 24 * 60 * 60)
        seconds %= (7 * 24 * 60 * 60)

        days = seconds // (24 * 60 * 60)
        seconds %= (24 * 60 * 60)

        hours = seconds // (60 * 60)
        seconds %= (60 * 60)

        minutes = seconds // 60
        seconds %= 60

        if seconds == 1:
            seconds = f'{seconds} second'
        elif seconds != 0:
            seconds = f'{seconds} seconds ' 
        else:
            seconds = ''
        
        if minutes == 1:
            minutes = f'{minutes} minute '
        elif minutes != 0:
            minutes = f'{minutes} minutes ' 
        else:
            minutes = ''

        if hours == 1:
            hours = f'{hours} hour '
        elif hours != 0:
            hours = f'{hours} hours ' 
        else:
            hours = ''

        if days == 1:
            days = f'{days} day '
        elif days != 0:
            days = f'{days} days ' 
        else:
            days = ''

        if weeks == 1:
            weeks = f'{weeks} week '
        elif weeks != 0:
            weeks = f'{weeks} weeks ' 
        else:
            weeks = ''

        print(f'{usrinp:,d} seconds ==> {weeks+days+hours+minutes+seconds}')
        if usrinp != 8400:
            print("===== End of program =====")
        else:
            print("===== program end =====")
    else:
        print(f"This number ({usrinp}) is not VALID !!!")
        print("===== End of program =====")