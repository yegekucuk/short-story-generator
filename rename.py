import os

folder_path = './dataset'

files = [f for f in os.listdir(folder_path)]
print(files)

os.makedirs(f"./{folder_path}_2", exist_ok=True)

for i, file in enumerate(files):
    new_name = f"{i}.txt"
    os.system(f"touch {folder_path}_2/{new_name}")
    os.system(f'cp "{folder_path}/{file}" "{folder_path}_2/{new_name}"')

os.system(f"rm -rf {folder_path}")
os.system(f"mv {folder_path}_2 {folder_path}")

print("Successfully renamed.")
