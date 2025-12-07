import os
import shutil
import msvcrt
from time import sleep
from colorama import init, Fore

init(autoreset=True)

# counters
total_removed = []
total_Skipped = []

class TempCleaning:
    def __init__(self):
        self.paths = [os.getenv("TEMP"), os.path.join(os.getenv("SystemRoot"), "Temp")]
        
    def clean(self):
        print(Fore.YELLOW+"[*] Cleaning Temp Files...\n")
        sleep(1)
        
        for path in self.paths:
            if os.path.exists(path):
                for file in os.listdir(path):
                    file_path = os.path.join(path, file)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            
                            os.remove(file_path)
                            total_removed.append(file_path)

                        else:

                            total_removed.append(file_path)
                            shutil.rmtree(file_path)
                
                    except:
                        total_Skipped.append(file_path)


        for file_name in total_Skipped:
            if file_name in total_removed:
                total_removed.remove(file_name)

        for x in total_removed:
            print(f"File:> {x}"+Fore.GREEN+" [Removed]")
            sleep(0.01)

        print(Fore.GREEN+"[✓] Temp cleaned.\n")

class CustomClean:
    def __init__(self):
        self.paths = [
            # Prefetch
            os.path.join(os.getenv("WINDIR") or r"C:\\Windows", "Prefetch"),

            # Windows Update Cache
            os.path.join(os.getenv("WINDIR") or r"C:\\Windows", "SoftwareDistribution", "Download"),

            # Recent Documents (shortcuts)
            os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Recent"),

            # Thumbnail Cache
            os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Windows", "Explorer"),

            # Crash Dumps
            os.path.join(os.getenv("WINDIR") or r"C:\\Windows", "Minidump")
        ]
    def clean(self):
        print(Fore.YELLOW+"[*] Cleaning Custom Paths...\n")
        sleep(1)

        for path in self.paths:
            if os.path.exists(path):
                for file in os.listdir(path):
                    files_loc = os.path.join(path, file)
                    try:

                        if os.path.isfile(files_loc) or os.path.islink(files_loc):

                            total_removed.append(files_loc)
                            os.remove(files_loc)

                        else:
                            total_removed.append(files_loc)
                            shutil.rmtree(files_loc)
                    except:
                        total_Skipped.append(files_loc)
                
                for file_name in total_Skipped:
                    if file_name in total_removed:
                        total_removed.remove(file_name)
    
                for x in total_removed:
                    print(f"File:> {x}"+Fore.GREEN+" [Removed]")
                    sleep(0.01)
        print(Fore.GREEN+"-----------------------------------------------------")
        print(Fore.GREEN+"\n[✓] Custom paths cleaned.\n")
                

def Main():
    print(Fore.GREEN+"# ==== Running System Cleanup ====\n")
    sleep(1)

    temp_cleaner = TempCleaning()
    custom_cleaner = CustomClean()

    temp_cleaner.clean()

    ask_for_custom_clean = input("Do you wanna run the custom clean?: ").strip().lower()

    if ask_for_custom_clean in ("yes","y"):
        custom_cleaner.clean()

    if len(total_removed) > 0:
        print(Fore.GREEN+"==== All Cleaning Done! ====\n")

        # Output
        print(Fore.GREEN+f"[{len(total_removed)}] Files Removed...")
        print(Fore.RED+f"[{len(total_Skipped)}] Files Skipped...")

        total_removed.clear()
        total_Skipped.clear()

    print("Press any key to exit...")
    msvcrt.getch()   

if __name__ == "__main__":
    Main()