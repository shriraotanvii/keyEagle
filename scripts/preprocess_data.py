import pandas as pd

df = pd.read_csv("data/keystrokes_data.csv")

# Filter out invalid keystrokes (e.g., None or empty strings)
df = df[df["Keystroke"].notna() & (df["Keystroke"] != "")]

# Label suspicious behavior
df["Label"] = 0
df.loc[df["CPU Usage (%)"] > 40, "Label"] = 1

df.to_csv("data/labeled_keystrokes_data.csv", index=False)
print("✅ Labeled dataset saved to data/labeled_keystrokes_data.csv")