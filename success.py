# coding=utf-8
import requests
import traceback
def msg_push(title, content, key):
    try:
        url = 'https://sc.ftqq.com/%s.send' % key
        requests.post(url, data={'text': title, 'desp': content})
    except Exception as e:
        traceback.format_exc()
if __name__ == '__main__':
    key = 'SCT141777TMdanYQN2dKeDiaNAfll6FdRE'
    msg_push('今日打卡成功', '自动填写健康卡填报', key)
