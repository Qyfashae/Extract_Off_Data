from bs4 import BeautifulSoup

print("This script locate links in html files and extract them to a new file")
input_file = input("i_File: ")
output_file = input("o_File: ")

def extract_links(html_file, tag="a", attribute="href"):
	try:
		with open(html_file, "r", encoding="UTF-8") as file:
			soup = BeautifulSoup(file, "html.parser")
			links = []
			for link in soup.find_all(tag):
				if link.has_attr(attribute):
					links.append(link.get(attribute))
			return links
	except Exception as e:
			print(f"Error: {e}")
			return []

def save_links_to_file(links, output_file):
	try:
		with open(output_file, "w", encoding="UTF-8") as file:
			for link in links:
				file.write(link + "\n")
		print(f"Links saved to {output_file}")
	except Exception as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	links = extract_links(input_file)

	save_links_to_file(links, output_file)

	print(f"Found {len(links)} links in the file.")
