import json
import os


def remove_duplicates(object_events: list[dict]):
    for i in reversed(range(len(object_events))):
        for j in reversed(range(len(object_events))):
            if i == j:
                continue

            if object_events[i] == object_events[j]:
                object_events.pop(i)
                break


def main():
    print("While unlikely that this program will corrupty your save file, it is still recommended to keep a save of"
          " your campaign before this program is ran.")

    advanced = input("Input 1 for simple mode and 2 for advanced mode: ") == "2"

    if advanced:
        filepath = input("Input the filepath of the ballooning save file:\n")

    else:
        savename = input("Input the name of the ballooning save file (e.g. quicksave_431): ")
        filepath = os.getenv("APPDATA") + \
            "/../LocalLow/Intercept Games/Kerbal Space Program 2/Saves/SinglePlayer/Default/" \
            + savename + ".json"

    print("\nLoading the save file. This may take some time depending on its size.")
    with open(filepath, "r") as f:
        savefile = json.load(f)

    print("Removing duplicate entires in TravelLogData")
    remove_duplicates(savefile["TravelLogData"]["ObjectEvents"])
    print("Duplicate entries removed. Writing the file.")

    with open(filepath, "w") as f:
        json.dump(savefile, f)

    print("Complete")


if __name__ == "__main__":
    main()
