from playwright.sync_api import Playwright, sync_playwright, expect
import sys
import time

username = sys.argv[1]
password = sys.argv[2]

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html", timeout = 0)
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").click()
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").fill(username)
    page.locator("[placeholder=\"密码\"]").click()
    page.locator("[placeholder=\"密码\"]").press("CapsLock")
    page.locator("[placeholder=\"密码\"]").fill("D")
    page.locator("[placeholder=\"密码\"]").press("CapsLock")
    page.locator("[placeholder=\"密码\"]").fill(password)
    page.locator("text=5天内自动登录 登 录 >> input[name=\"submit\"]").click()
    with context.expect_page() as page_info:
        page.click("text=查看更多+"),
    page1 = page_info.value
    with context.expect_page() as page_info:
        page1.click("text=健康卡填报"),
    page2 = page_info.value 
    time.sleep(5)
    with context.expect_page() as page_info:
        page2.click("a:has-text(\"我要办理\")"),
    page3 = page_info.value
    time.sleep(5)
    page3.locator("text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins").click()
    page3.locator("text=下一步").click()
    page3.locator("#select2-select_pcode-container").click()
    page3.locator("li[role=\"treeitem\"]:has-text(\"广东省\")").click()
    page3.locator("#select2-select_ccode-container").click()
    page3.locator("li[role=\"treeitem\"]:has-text(\"珠海市\")").click()
    page3.locator("#select2-select_dcode-container").click()
    page3.locator("li[role=\"treeitem\"]:has-text(\"金湾区\")").click()
    page3.locator("#hsjcsj i").click()
    page3.locator("text=确定").nth(1).click()
    page3.locator("text=本人承诺登记后、到校前不再前往其他地区 >> ins").click()
    page3.locator("button:has-text(\"提交\")").click()
    page3.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
    print("GOOD!!!!")
