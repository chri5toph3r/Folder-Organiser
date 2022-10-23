# Folder-Organiser

### Usage:
```
path:
```
Give a path of the directory to organise (absolute or relative to the directory the file is inside).
If you write a wrong directory or don't write any, the program will take the file's directory.

```
Current directory: C:/Users
```
Then the targetted directory will be printed in the console.

```
Available extensions: ['pdf', 'jpeg', 'png', 'wav']
extensions:
```
After that, the program reads all file extensions that appear in the directory and lets you choose which ones you want to select.
If you want to write more than one, write them after space.

```
Destination: C:/Users/
```
Lastly you have to give a destination dictionary that is relative to the current one.
If given directory does not exit, it will get created.

At the end, the amount of moved files will be printed out.
To exit the program you have to click enter.
