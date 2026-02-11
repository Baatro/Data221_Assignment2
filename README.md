# Data221_Assignment2
Question 1 — Word counts  
Read sample-file.txt, clean tokens (lowercase, strip edge punctuation, keep tokens with ≥2 letters), count words, print top 10 as word -> count.

Question 2 — Bigrams  
Same cleaning as Q1, build consecutive word pairs, count bigrams, print top 5 as word1 word2 -> count.

Question 3 — Near-duplicate lines  
Normalize lines (lowercase, remove whitespace and punctuation), find sets of near-duplicate lines, print the number of sets and the first two sets with line numbers and original text.

Question 4 — Filter students  
Load student.csv, filter rows where studytime >= 3, internet == 1, and absences <= 5. Save filtered rows to high_engagement.csv and print the count and average grade.

Question 5 — Grade bands  
Add grade_band (Low ≤9, Medium 10–14, High ≥15). Produce grouped summary: count, average absences, % with internet per band. Save as student_bands.csv.

Question 6 — Crime risk vs unemployment  
Load crime.csv, create risk = "HighCrime" if ViolentCrimesPerPop >= 0.50 else "LowCrime". Group by risk and print average PctUnemployed for each group.

Question 7 — Page title and paragraph  
Scrape https://en.wikipedia.org/wiki/Data_science. Print the page <title> and the first paragraph from div#mw-content-text that has ≥ 50 characters.

Question 8 — Headings extraction  
From the same Data Science page, extract all <h2> headings inside div#mw-content-text, exclude headings containing References, External links, See also, Notes, remove [edit], and save to headings.txt (one per line).

Question 9 — Table extraction  
Scrape https://en.wikipedia.org/wiki/Machine_learning. Find the first table in div#mw-content-text with ≥ 3 data rows, extract headers from <th> (or create col1, col2, …), pad short rows with empty strings, and save to wiki_table.csv.

Question 10 — Line search function  
Implement find_lines_containing(filename, keyword) returning a list of (line_number, line_text) for case-insensitive matches 
