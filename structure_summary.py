import os

def count_python_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                count += 1
    return count

international_count = count_python_files('versalaw2/international_law')
specialized_count = count_python_files('versalaw2/indonesian_law/specialized_law')

print("📊 VERSALAW2 MODULE SUMMARY:")
print(f"🌍 International Law Modules: {international_count}")
print(f"🇮🇩 Specialized Crime Modules: {specialized_count}")
print(f"📈 Total Operational Modules: {international_count + specialized_count}")

print("\n📁 INTERNATIONAL LAW MODULES:")
for file in os.listdir('versalaw2/international_law'):
    if file.endswith('.py') and file != '__init__.py':
        print(f"   • {file}")

print("\n📁 SPECIALIZED CRIME MODULES:")  
for file in os.listdir('versalaw2/indonesian_law/specialized_law'):
    if file.endswith('.py') and file != '__init__.py':
        print(f"   • {file}")
