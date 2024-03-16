from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import cv2
import time


def list_contributors(driver):
    """此專案裡有幾個合作者，並且分別列出他們的名字"""
    driver.get('https://github.com/hahow/hahow-recruit')
    contributors_title_link = driver.find_element(By.XPATH,
                                                  '//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[2]/div/div[5]/div/h2/a')
    contributors_total = int(contributors_title_link.find_element(By.XPATH, './span').text)
    print(f'此專案總共有 {contributors_total} 位合作者，名單如下：')
    contributors_title_link.click()
    contributors_list = driver.find_elements(By.XPATH, '//a[@data-hovercard-type="user"][@class="text-normal"][text()]')

    for person in contributors_list:
        print(person.text)


def check_wireframe_images(driver):
    """檢查Wireframe的圖片是否存在。"""
    driver.get('https://github.com/hahow/hahow-recruit/blob/master/frontend.md')
    time.sleep(2)
    wireframe_image1 = driver.find_element(By.XPATH,
                                           '//img[@src="/hahow/hahow-recruit/raw/master/assets/hero-list-page.png"]')
    wireframe_image2 = driver.find_element(By.XPATH,
                                           '//img[@src="/hahow/hahow-recruit/raw/master/assets/hero-profile-page.png"]')

    wireframe_image1.screenshot('Ui_test/compare/hero-list-page.png')
    wireframe_image2.screenshot('Ui_test/compare/hero-profile-page.png')

    compare_images_pixel('Ui_test/assets/hero-list-page.png', 'Ui_test/compare/hero-list-page.png')
    compare_images_pixel('Ui_test/assets/hero-profile-page.png', 'Ui_test/compare/hero-profile-page.png')


def compare_images_pixel(compare1, compare2):
    """比較兩張圖片的像素差異，如果差異像素少於100則認為圖片存在。"""
    file_name = compare1.split('/')[-1]
    img1 = cv2.imread(compare1)
    img2 = cv2.imread(compare2)
    diff_image = cv2.absdiff(img1, img2)
    diff_pixels = np.sum(diff_image)
    different_pixel_count = np.count_nonzero(diff_pixels)

    if different_pixel_count < 100:
        print(f'{file_name} 圖片存在')
    else:
        print(f'{file_name} 圖片不存在')


def find_last_non_merge_commit(driver):
    """找出最後一個 commit 的人是誰"""
    driver.get('https://github.com/hahow/hahow-recruit/commits/master/')
    all_commits = driver.find_elements(By.XPATH, '//div[@data-testid="listview-item-title-container"]')
    merge_commit = driver.find_element(By.XPATH, '//*[text()="Merge pull request"]')
    commits_person = driver.find_elements(By.XPATH, '//*[@data-testid="commit-row-item"]//div[3]//a[2]')

    for i in range(len(all_commits)):
        commit = all_commits[i]
        if merge_commit.text not in commit.text:
            print(f'最後一個 commit 的人是 {commits_person[i].text}， commit 標題是: {commit.text}')
            break


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    # 列出所有合作者及數量
    list_contributors(driver)

    # 確認 Wireframe 圖是否存在
    check_wireframe_images(driver)

    # 找到最後一個 commit 的人
    find_last_non_merge_commit(driver)
    driver.quit()