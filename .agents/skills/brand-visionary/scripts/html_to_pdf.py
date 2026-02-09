import sys
import asyncio
from playwright.async_api import async_playwright
import os

async def html_to_pdf(input_file, output_file):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Load the HTML file
        abs_input = os.path.abspath(input_file)
        await page.goto(f"file://{abs_input}")
        
        # A4 format, Print Background for colors
        await page.pdf(path=output_file, format="A4", print_background=True, margin={
            "top": "0px",
            "bottom": "0px",
            "left": "0px",
            "right": "0px"
        })
        
        await browser.close()
        print(f"Successfully created PDF: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python html_to_pdf.py <input_html> <output_pdf>")
        sys.exit(1)
        
    input_html = sys.argv[1]
    output_pdf = sys.argv[2]
    
    asyncio.run(html_to_pdf(input_html, output_pdf))
