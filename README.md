# webpy-converter


A Python program to convert WebP images to PNG format. This program supports conversion from both **local file paths** and **URLs**.  

## Features  
- Convert a WebP image from a local file path to PNG.  
- Download a WebP image from a URL and convert it to PNG.  

## Prerequisites  
Ensure you have the requirements installed:  
  ```bash  
  pip install -r requirements.txt  
  ```  

## Usage  
Run the program using the command line.  

### Local File Conversion  
```bash  
python conv.py -f image_file_path desired_png_file_path  
```  
**Example:**  
```bash  
python conv.py -f /home/lahh/lahh.webp /home/lahh/lahh.png  
```  

### URL Conversion  
```bash  
python conv.py -u image_url desired_png_file_path  
```  
**Example:**  
```bash  
python conv.py -u https://lahh.com/lahh.webp /home/lahh/lahh.png  
```  

## Output  
The converted PNG file will be saved to the path you provide as the second argument. If u use url-mode, the webp that being downloaded will be removed after converting 


Feel free to modify as needed!
# webpy-converter
