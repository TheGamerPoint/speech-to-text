# https://github.com/TheGamerPoint/speech-to-text
# If you have any bugs you want to report DM thegamerpoint on discord user id: 1076614414276493362

# Don't edit below this line unless you know what your doing
import speech_recognition as sr, traceback

recognizer = sr.Recognizer()

try:
    microphone = sr.Microphone()
except OSError:
    print("Error: Could not access the microphone.")
    print("Make sure a microphone is connected and available.")
    exit()

try:
    with microphone as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ready!\n")

except:
    traceback.print_exc()
    exit()


while True:
    try:
        with microphone as source:
            print("Say something...")

            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=10
                )

            except sr.WaitTimeoutError:
                print("No speech detected. Try again.\n")
                continue

        try:
            print("Processing speech...")
            text = recognizer.recognize_google(audio)

            print("You said:", text)
            print()

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.\n")
            continue

        except sr.RequestError as e:
            print("Could not connect to the speech recognition service.")
            print(f"Details: {e}\n")
            continue

    except KeyboardInterrupt:
        print("\nExiting...")
        break

    except OSError:
        print("Microphone error. Please check your microphone.\n")
        break

    except Exception as e:
        print(f"Unexpected error: {e}\n")
        continue
