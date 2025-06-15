import pandas as pd
import os
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
import xml.dom.minidom

# Load Excel file
df_path = os.path.join("Dictionary", "dictionary.xlsx")
df = pd.read_excel(df_path, sheet_name="UNDP version", header=0)

print(df.head())

# Create root XML element
root = Element("dictionary")

# Loop through rows
for _, row in df.iterrows():
    entry = SubElement(root, "entry")
    entry.text = str(row["Official terms (EN)"])
    
    source = SubElement(entry, "source")
    source.text = str(row["Source"])
    
    SubElement(source, "translation").text = str(row["Translation (MN)"])
    SubElement(source, "definition").text = str(row["Definition (MN)"])

    source2 = SubElement(entry, "source")
    source2.text = str(row["Source2"])
    
    SubElement(source2, "translation").text = str(row["Translation (MN)2"])
    SubElement(source2, "definition").text = str(row["Definition (MN)2"])

# Pretty-print and save
xml_str = xml.dom.minidom.parseString(tostring(root)).toprettyxml()
with open("dictionary.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)
