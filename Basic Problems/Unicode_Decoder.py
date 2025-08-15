import requests
import re
from bs4 import BeautifulSoup

def decode_unicode_grid(doc_url):
    original_url = doc_url
    
    if '/pub' in doc_url:
        # Keeping the original published URL as it is, but also try export format
        export_url = doc_url.replace('/pub', '/export?format=txt')
    elif '/edit' in doc_url:
        doc_url = doc_url.replace('/edit#gid=0', '/export?format=txt')
        doc_url = doc_url.replace('/edit', '/export?format=txt')
    elif 'docs.google.com' in doc_url and 'export' not in doc_url and 'pub' not in doc_url:
        # Extracting document ID and creating export URL
        doc_id_match = re.search(r'/d/([a-zA-Z0-9-_]+)', doc_url)
        if doc_id_match:
            doc_id = doc_id_match.group(1)
            doc_url = f'https://docs.google.com/document/d/{doc_id}/export?format=txt'
    
    try:
        urls_to_try = [doc_url]
        if '/pub' in original_url:
            urls_to_try.append(export_url)
        
        content = None
        for url in urls_to_try:
            try:
                response = requests.get(url)
                response.raise_for_status()
                content = response.text
                print(f"Successfully fetched from: {url}")
                break
            except:
                continue
        
        if content is None:
            raise Exception("Could not fetch content from any URL format")
        
        characters = []
        
        from bs4 import BeautifulSoup
        try:
            soup = BeautifulSoup(content, 'html.parser')
            tables = soup.find_all('table')
            
            for table in tables:
                rows = table.find_all('tr')
                header_found = False
                
                for row in rows:
                    cells = row.find_all(['td', 'th'])
                    if len(cells) >= 3:
                        cell_texts = [cell.get_text().strip().lower() for cell in cells]
                        if any('coordinate' in text or 'character' in text for text in cell_texts):
                            header_found = True
                            continue
                        
                        if header_found:
                            try:
                                x = int(cells[0].get_text().strip())
                                char_text = cells[1].get_text().strip()
                                y = int(cells[2].get_text().strip())
                                
                             
                                if char_text:
                                    if char_text.startswith('U+'):
                                        # Unicode code point format
                                        unicode_hex = char_text[2:]
                                        char = chr(int(unicode_hex, 16))
                                    elif len(char_text) == 1:
                                        # Direct character
                                        char = char_text
                                    else:
                                        # Try to interpret as hex
                                        try:
                                            char = chr(int(char_text, 16))
                                        except:
                                            char = char_text[0] if char_text else ' '
                                    
                                    characters.append((char, x, y))
                            except (ValueError, IndexError):
                                continue
        except:
            pass
        
        # If no characters found 
        if not characters:
            # Looking for patterns like "U+XXXX at (x, y)" or similar formats
            pattern = r'U\+([0-9A-Fa-f]+).*?[\(\[](\d+),\s*(\d+)[\)\]]'
            matches = re.findall(pattern, content)
            
            if not matches:
                # Trying alternative pattern formats
                pattern = r'([0-9A-Fa-f]{4,}).*?[\(\[](\d+),\s*(\d+)[\)\]]'
                matches = re.findall(pattern, content)
            
            if not matches:
                # Trying parsing line by line for different formats
                lines = content.split('\n')
                for line in lines:
                    # Looking for various formats that might contain unicode and coordinates
                    if 'U+' in line and '(' in line:
                        unicode_match = re.search(r'U\+([0-9A-Fa-f]+)', line)
                        coord_match = re.search(r'\((\d+),\s*(\d+)\)', line)
                        if unicode_match and coord_match:
                            matches.append((unicode_match.group(1), coord_match.group(1), coord_match.group(2)))
            
            for unicode_hex, x_str, y_str in matches:
                try:
                    # Converting hex to integer and then to character
                    unicode_int = int(unicode_hex, 16)
                    char = chr(unicode_int)
                    x = int(x_str)
                    y = int(y_str)
                    characters.append((char, x, y))
                except (ValueError, OverflowError):
                    continue
        
        if not characters:
            print("No valid Unicode characters with coordinates found in the document.")
            print("Document content preview:")
            print(content[:500] + "..." if len(content) > 500 else content)
            return
        
        # Finding the grid dimensions
        max_x = max(pos[1] for pos in characters)
        max_y = max(pos[2] for pos in characters)
        
        # Creating and populating the grid
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        
        for char, x, y in characters:
            grid[y][x] = char
        
        # Print the grid
        print("Decoded Unicode Grid:")
        print("=" * (max_x + 3))
        for row in grid:
            print(''.join(row))
        print("=" * (max_x + 3))
        print("Grid dimensions: {}x{}".format(max_x + 1, max_y + 1))
            
    except requests.RequestException as e:
        print(f"Error fetching document: {e}")
        print("Make sure the Google Doc is publicly accessible or shared with viewing permissions.")
    except Exception as e:
        print(f"Error processing document: {e}")


# main function
if __name__ == "__main__":
    input_url = input("Enter the Google Doc URL: ").strip()
    
    print("Google Doc Unicode Grid Decoder")
    print("=" * 50)
    
    decode_unicode_grid(input_url)