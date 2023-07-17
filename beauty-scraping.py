from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://beauty.hotpepper.jp/svcSA/macAD/salon/')
elements = driver.find_elements(By.CLASS_NAME,"message")

elemnt = elements[1].find_element(By.TAG_NAME, 'a')
elemnt.click()

# 平均点
review_rating = driver.find_element(By.CLASS_NAME,"reviewRating")
average_score = review_rating.find_element(By.CLASS_NAME,"reviewRatingMeanScore.jscReviewRatingMeanScore")

# 件数
review_count = driver.find_element(By.CLASS_NAME,"numberOfResult")

# サロン名
salon_title = driver.find_element(By.CLASS_NAME,"detailTitle")

# URL
salon_url = driver.current_url


# パンクズリストをクリックしてlistページに遷移する
pankuzu_element = driver.find_element(By.CLASS_NAME, "pankuzu.cFix")
pankuzu_list = pankuzu_element.find_element(By.XPATH, "//a[contains(text(), '検索結果一覧')]")

pankuzu_list.click()