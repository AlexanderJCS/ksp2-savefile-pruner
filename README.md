# ksp2-savefile-pruner

This simple Python program is designed to solve a Kerbal Space Program 2 bug that makes the save file size balloon to hundreds of megabytes if not gigabytes, which can cause the save/load times to become very long. This issue is caused by repeated logging of the same event. This program deletes the repeated entries.

![image](https://user-images.githubusercontent.com/98898166/228409816-dcbf4472-b0bc-4a12-b47d-e35322820160.png)

## Disclaimer

Creating a savefile backup is strongly recommended before running this program. While I do my best to make this program safe to use, it is not guaranteed to be stable. The best way to prevent this is to keep a save of the game before this program is ran. If you encounter any issues after running this program, open a GitHub issue.

## Running the Program

### Prerequisites

If you haven't already, install Python 3.11 at [python.org](https://www.python.org/).

Then, download the code by clicking on Code -> Download Zip. Finally, extract the zip file.

### Inside Kerbal Space Program

Launch Kerbal Space Program 2. Open the save with the ballooning save file, and press F5 to quicksave. This will be the save to modify.

Then, press `escape -> load` and take note of the two circled values.

The upper circle highlights the campaign name, and the lower circle shows the name of the save you just created. You will need these values for the next step.

![image](https://user-images.githubusercontent.com/98898166/229261246-0e5e1ff3-cdf5-4e0a-80a8-607aaa7dffd5.png)

### Prune the savefile

Run `main.py` and type the name of the save file to prune (this will be the quicksave created in the last step). Then, click the "Prune" button and the program will lower the save file size.

An example input to the program to prune a save file named `quicksave_1035` with a campaign named `Default`:

![image](https://user-images.githubusercontent.com/98898166/229261287-5dd34d38-a932-4d0e-abc3-19ccd68dd65c.png)

### Error: Could not find savefile name inside campaign

If you encounter this error, it is likely the name or capitalization of either the campaign name or the save name is incorrect.

This error will also occur if you are not on Windows.

If both of these values are correct, please open an issue.

### Final Steps

Finally, load your pruned savefile and you're done.

## Contributing

Contributions are welcome, just make a pull request.
