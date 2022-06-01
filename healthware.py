from playwright.sync_api import Playwright, sync_playwright, expect
import sys
import time

username = sys.argv[1]
password = sys.argv[2]

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html
    page.goto("https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html")

    # Go to https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fmy.zcst.edu.cn%2FportalRedirect.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__
    page.goto("https://authserver.zcst.edu.cn/cas/login?service=https%3A%2F%2Fmy.zcst.edu.cn%2FportalRedirect.jsp%3F_p%3DYXM9MSZwPTEmbT1OJg__")

    # Click [placeholder="用户名\/手机号\/邮箱"]
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").click()

    # Fill [placeholder="用户名\/手机号\/邮箱"]
    page.locator("[placeholder=\"用户名\\/手机号\\/邮箱\"]").fill(username)

    # Click [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").click()

    # Press CapsLock
    page.locator("[placeholder=\"密码\"]").press("CapsLock")

    # Fill [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").fill("D")

    # Press CapsLock
    page.locator("[placeholder=\"密码\"]").press("CapsLock")

    # Fill [placeholder="密码"]
    page.locator("[placeholder=\"密码\"]").fill(password)

    # Click text=5天内自动登录 登 录 >> input[name="submit"]
    page.locator("text=5天内自动登录 登 录 >> input[name=\"submit\"]").click()
    # expect(page).to_have_url("https://my.zcst.edu.cn/_web/sopplus/sopplus/index.html")

    # Click text=查看更多+
    with page.expect_popup() as popup_info:
        page.locator("text=查看更多+").click()
    page1 = popup_info.value
    
    # Click text=健康卡填报
    with page1.expect_popup() as popup_info:
        page1.locator("text=健康卡填报").click()
    page2 = popup_info.value    
    time.sleep(5)
    # Click a:has-text("我要办理")
    with page2.expect_popup() as popup_info:
        page2.locator("a:has-text(\"我要办理\")").click()
    page3 = popup_info.value
    time.sleep(5)
    # Click text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins
    page3.locator("text=为了全力做好学校新型冠状病毒感染的肺炎疫情防控工作，我承诺以下内容填写属实。 30s 已阅读并同意 >> ins").click()

    # Click text=下一步
    page3.locator("text=下一步").click()

    # Click #select2-select_pcode-container
    page3.locator("#select2-select_pcode-container").click()

    # Click li[role="treeitem"]:has-text("广东省")
    page3.locator("li[role=\"treeitem\"]:has-text(\"广东省\")").click()

    # Click #select2-select_ccode-container
    page3.locator("#select2-select_ccode-container").click()

    # Click li[role="treeitem"]:has-text("珠海市")
    page3.locator("li[role=\"treeitem\"]:has-text(\"珠海市\")").click()

    # Click #select2-select_dcode-container
    page3.locator("#select2-select_dcode-container").click()

    # Click li[role="treeitem"]:has-text("金湾区")
    page3.locator("li[role=\"treeitem\"]:has-text(\"金湾区\")").click()

    # Click #hsjcsj i
    page3.locator("#hsjcsj i").click()

    # Click text=确定 >> nth=1
    page3.locator("text=确定").nth(1).click()

    # Click text=本人承诺登记后、到校前不再前往其他地区 >> ins
    page3.locator("text=本人承诺登记后、到校前不再前往其他地区 >> ins").click()

    # Click button:has-text("提交")
    page3.locator("button:has-text(\"提交\")").click()

    # Close page
    page3.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
    print("GOOD!!!!")
