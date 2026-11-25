from pathlib import Path

# One sentence, one small moment: a weed does in a second what a blocked writer could not do in a week.
ENTRY = "A dandelion seed landed on my keyboard and typed the one letter I had been trying to write all week, and I still could not write the second one."

out = Path("/output/entry.txt")
out.write_text(ENTRY, encoding="utf-8")
