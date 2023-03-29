import tkinter as tk
import threading
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


def prune(entry: tk.Entry, output_label: tk.Label):
    filepath = os.getenv("APPDATA") + \
               "/../LocalLow/Intercept Games/Kerbal Space Program 2/Saves/SinglePlayer/Default/" \
               + entry.get() + ".json"

    output_label.config(text=f"Opening save {entry.get()}")

    try:
        with open(filepath, "r") as f:
            savefile = json.load(f)

    except FileNotFoundError:
        output_label.config(text=f"Could not find save {entry.get()}")
        return

    remove_duplicates(savefile["TravelLogData"]["ObjectEvents"])

    with open(filepath, "w") as f:
        json.dump(savefile, f)

    output_label.config(text="Complete")
    entry.delete(0, tk.END)


def main():
    gui = tk.Tk()
    gui.title("KSP2 Savefile Pruner")

    disclaimer = tk.Label(gui, text="NOTE: While unlikely that this program will corrupt your save file, it is still" +
                          "\nrecommended to keep a save of your campaign before this program is ran.")
    disclaimer.grid(column=0, row=0, padx=10, pady=20, columnspan=3)

    savename_label = tk.Label(gui, text="Save name:")
    savename_label.grid(column=0, row=1, padx=10, pady=10)

    savename_entry = tk.Entry(gui, width=50)
    savename_entry.grid(column=1, row=1, padx=10, pady=10, columnspan=2)

    prune_button = tk.Button(gui, text="Prune", width=50,
                             command=lambda: threading.Thread(target=prune, args=(savename_entry, output)).start())
    prune_button.grid(column=0, row=2, padx=10, pady=10, columnspan=3)

    output = tk.Label(gui)
    output.grid(column=0, row=3, padx=10, pady=10, columnspan=3)

    gui.mainloop()


if __name__ == "__main__":
    main()
