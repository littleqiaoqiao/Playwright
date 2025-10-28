from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False) #启动浏览器，返回 Browser 类型对象
    context = browser.new_context() #创建一个独立的新浏览器窗口

    context.tracing.start(screenshots=True, snapshots=True, sources=True) #开启跟踪 结果会生成一个zip文件，包含页面操作的所有细节，方便调试和分析有疑问的步骤

    page = context.new_page() #在新浏览器窗口中创建新页面，返回 Page 类型对象
    page.goto("https://www.byhy.net/cdn2/files/selenium/stock1.html") #打开网页
    print(page.title())  # 打印网页标题栏
    page.locator('#kw').fill('通讯')  # 输入通讯
    page.locator('#go').click()      # 点击查询
    #page.get_by_text('test').nth(1).click() #点击第二个test链接

    page.wait_for_timeout(2000) #playwright中等待的用法 不要用time.sleep()

    lcs = page.locator(".result-item").all() #打印所有搜索内容
    #edit
    for lc in lcs:
        print(lc.inner_text())

    context.close() #关闭一个独立的新浏览器窗口
    browser.close()