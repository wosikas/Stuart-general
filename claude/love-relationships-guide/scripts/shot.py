import sys,os
from playwright.sync_api import sync_playwright
src=sys.argv[1]; out=sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome')
    pg=b.new_page(viewport={'width':1000,'height':1200},device_scale_factor=1)
    pg.goto('file://'+os.path.abspath(src)); pg.wait_for_timeout(1500)
    if out.endswith('.png'): pg.locator('main').screenshot(path=out)
    else: pg.pdf(path=out,format='A4',print_background=True,margin={'top':'10mm','bottom':'10mm','left':'0','right':'0'})
    b.close()
