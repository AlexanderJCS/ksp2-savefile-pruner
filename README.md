# ksp2-savefile-pruner

This simple Python program is designed to solve a Kerbal Space Program 2 bug that makes the save file size balloon to hundreds of megabytes if not gigabytes, which can cause the save/load times to become very long. This issue is caused by repeated logging of the same event. This program deletes the repeated entries, leaving only one logging entry.

![image](https://user-images.githubusercontent.com/98898166/228409816-dcbf4472-b0bc-4a12-b47d-e35322820160.png)

## Disclaimer

Creating a savefile backup is strongly recommended before running this program. While I do my best to make this program safe to use, it is not guaranteed to be stable. The best way to prevent this is to keep a save of the game before this program is ran. If you encounter any issues after running this program, open a GitHub issue.

## Running the Program

### Create a new save

Launch Kerbal Space Program 2. Open the save with the ballooning save file, and press F5 to quicksave. This will be the save to modify. Then, press escape -> load and take note of the name of the quicksave you just created, since this will be needed later.

### Clean up the savefile

Run the program and input `1` for simple mode. Then, input the name of the save that you want to clean up (this will be the quicksave made in the last step). For example, if the quicksave name was `quicksave_431`, you would input `quicksave_431`.


## Contributing

Contributions are welcome. Currently, I am planning on adding error handling and a GUI.