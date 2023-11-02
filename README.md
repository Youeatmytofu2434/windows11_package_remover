# Windows 11 package remover

This is a basic program that removes any packages that can be found using *winget* command. **Tested in python 3.10.6**.

# ***DISCLAIMER***
**I am not responsible for any damanges done to your computer. Only use this if you know what you are doing.**

# Usage
1. Download all files in this repos to your computer and put them in a folder.
2. Open powershell, navigate to the folder you just created, and type "winget list" to get all installed packages.
3. Copy the IDs of the packages you wish to remove from your computer and paste them in the "packages.txt" file.
    1. Each package's ID must occupy 1 line. **Do NOT paste all IDs into the same line.**
    2. If an ID is not fully revealed, copy the exact name of a package as shown by the *winget list* command and type:
        ```powershell
        winget list --name "<name-of-the-package>" 
        ```
4. Run the script:
    ```python
    python3 windows11_package_remover.py
    ```