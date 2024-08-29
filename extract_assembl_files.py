import os, re

def find_sequences(folder_path):
  sequences = {}

  for root, dirs, files in os.walk(folder_path):
    for file in files:
      if file.endswith('.jpg'):
        name = os.path.splitext(file)[0]
        match = re.match(r"(.+?)(\d+)$", name)
        if match:
          prefix = match.group(1)
          frame_number = int(match.group(2))

          if prefix not in sequences:
            sequences[prefix] = []
          sequences[prefix].append((frame_number, os.path.join(root, file)))

  for prefix in sequences:
    sequences[prefix].sort(key=lambda x: x[0])
    sequences[prefix] = [f for _, f in sequences[prefix]]

  return sequences