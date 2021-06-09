import wave
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

print("\nPlease set the default settings!")

change_time = int(input(f"Enter time (in seconds): "))
change_say = input(f"Enter what to say: ")

while True:

    print(f"_______________________________________________________")
    print(f"\n1: Entry")
    print(f"2: Check")
    print(f"3: Settings")

    command = input(f"\nEnter command: ")

    if command == "1":
    
        full_name = input(f"\nEnter your name (ex- Ishank_Kumar): ")
        fs = 44100

        seconds = change_time

        print(f"Recording for {seconds} seconds...")
        say = f"Say: {change_say}"
        print(say)

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)
        sd.wait()
        write(f"./entry_data/{full_name}.wav", fs, myrecording)
        print(f"\nAudio Data is saved with the name {full_name}.wav")

    elif command == "2":

        check_name = input("Please enter the name of the person to confirm: ")

        fs = 44100

        seconds = change_time

        print(f"Recording for {seconds} seconds...")
        say = f"Say: {change_say}"
        print(say)

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)
        sd.wait()
        write(f"./validate_data/{check_name}.wav", fs, myrecording)

        try:
            file_entry = wave.open(f"./entry_data/{check_name}.wav")
            file_validate = wave.open(f"./validate_data/{check_name}.wav")

#########################################################################################################################
            #it is not for speaker verification, it is sound verification, I coudent complete it, if you can do this then please tell me and dm me on instagram https://instagram.com/opishank
            entry_data = file_entry.getnframes(), file_entry.getframerate(), file_entry.getnchannels()
            validate_data = file_validate.getnframes(), file_validate.getframerate(), file_validate.getnchannels()
#########################################################################################################################
            if entry_data == validate_data:
                print(f"Match confirm!")
            else:
                print(f"Match not found!")
        except IOError:
            print("File not in Entry")


    elif command == "3":

        while True:

            print(f"_______________________________________________________")
            print(f"\n-Entry\n")
            print(f"11: Change recording time (in seconds)")
            print(f"12: Change what to say")
            print(f"13: Exit")

            setting_command = input(f"\nEnter command: ")

            if setting_command == "11":

                change_time = int(input(f"Enter time (in seconds): "))

            elif setting_command == "12":

                change_say = input(f"Enter what to say: ")
                say = change_say
            elif setting_command == '13':
                break
            else:
                print(f"No such command!")
    
    else:
        print(f"No such command!")