页头动画生成：header.html 是 WebGL 片元着色器场景（循环等高线和字节流，周期 T=0..1 无缝循环）。
运行 `pip install playwright && playwright install chromium` 后执行 `python render_header.py`，输出 ../header.webp（72 帧，24fps）。
