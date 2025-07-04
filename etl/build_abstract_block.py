import os
import pandas as pd

# Step 0:  Define file paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(BASE_DIR, "data", "intermediate", "cleaned", "ethereum", "blocks", "ethereum__blocks__cleaned__16308189_to_16315360.csv")
output_path = os.path.join(BASE_DIR, "data", "intermediate", "abstract",  "ethereum", "abstract_block", "ethereum__abstract_block__16308189_to_16315360.csv")

# Step 1: Load cleaned data 
df = pd.read_csv(input_path)

# Step 2: Build 'block_sid' column
df["block_sid"] = df["chain_id"].astype(str) + "_" + df["block_number"].astype(str)

# Step 3: Rearrange columns
abstract_block = df[[
    "block_sid",
    "block_number",
    "timestamp"
]]

# Step 4: Save
abstract_block.to_csv(output_path, index=False)
print(f"✅ AbstractBlock written to {output_path}")