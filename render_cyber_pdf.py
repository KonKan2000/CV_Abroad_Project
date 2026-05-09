from playwright.sync_api import sync_playwright
import pathlib

root = pathlib.Path(__file__).parent.resolve()
input_html = root / "Cybersecurity_CV" / "CV_One_Page.html"
output_pdf = root / "Cybersecurity_CV" / "Konstantinos_Kanellopoulos_Cybersecurity_CV.pdf"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(input_html.as_uri())
    page.pdf(path=str(output_pdf), format="A4", print_background=True, margin={"top":"8mm","bottom":"8mm","left":"8mm","right":"8mm"})
    browser.close()

print(f"PDF created: {output_pdf}")
