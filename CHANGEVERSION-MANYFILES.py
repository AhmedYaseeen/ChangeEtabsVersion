import os

# Get folder path and new version
folder_path = input("Folder path: ")
new_version = input("New version (e.g. 18.0.0): ")

# Process all .E2K files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith('.e2k'):
        file_path = os.path.join(folder_path, filename)
        
        # Read file
        with open(file_path, 'r') as file:
            content = file.read()
            
        # Backup
        with open(file_path + '.backup', 'w') as file:
            file.write(content)
            
        # Find and replace version
        pos = content.find('  PROGRAM  "ETABS"  VERSION "')
        if pos != -1:
            # Find the current version number
            start = pos + len('  PROGRAM  "ETABS"  VERSION "')
            end = content.find('"', start)
            old_version = content[start:end]
            
            # Replace version
            old_line = f'  PROGRAM  "ETABS"  VERSION "{old_version}"'
            new_line = f'  PROGRAM  "ETABS"  VERSION "{new_version}"'
            new_content = content.replace(old_line, new_line)
            
            # Save changes
            with open(file_path, 'w') as file:
                file.write(new_content)
                
            print(f"File: {filename}")
            print(f"Changed version from {old_version} to {new_version}")
            print(f"Backup created as {filename}.backup")
            print("-" * 50)
        else:
            print(f"Warning: Version line not found in {filename}")
            print("-" * 50)

print("\nAll .E2K files processed!")