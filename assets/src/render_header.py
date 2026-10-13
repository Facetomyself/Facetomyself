# 用法: python render_header.py  (需要 playwright + ffmpeg)
import asyncio,os,subprocess
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__));F=os.path.join(D,'frames');os.makedirs(F,exist_ok=True)
N=72
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg=await b.new_page(viewport={'width':1200,'height':360})
        await pg.goto('file://'+D+'/header.html');await pg.wait_for_timeout(800)
        for i in range(N):
            await pg.evaluate(f'draw({i/N})');await pg.screenshot(path=f'{F}/{i:03d}.png')
        await b.close()
asyncio.run(main())
out=os.path.join(D,'..','header.webp')
subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate','24','-i',f'{F}/%03d.png','-loop','0','-c:v','libwebp','-quality','72','-compression_level','6',out],check=True)
print(out,os.path.getsize(out))
