data_of_packet = input("enter the 8 bites. P.S. 1 or 0:")

# определяем корректность введенных данных и четность бит
while data_of_packet != "":
    if len(data_of_packet) == 8:

        if data_of_packet.count("1") % 2 == 0:
            print(1)
            data_of_packet = input("enter the 8 bites. P.S. 1 or 0:")
            break

        else:
            print(0)
            data_of_packet = input("enter the 8 bites. P.S. 1 or 0:")
            break

    else:
        print("ur number of bites is incorrect")
        break

# Evaluation: NOT OK. Не работает, когда бит нечётный.
# enter the 8 bites. P.S. 1 or 0:10001000
# 1
# enter the 8 bites. P.S. 1 or 0:00010000
#
# Process finished with exit code 0