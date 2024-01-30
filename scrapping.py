import requests
from bs4 import BeautifulSoup
import csv
import re 

base_url = 'https://www.oliveyoung.co.kr/store/main/getSaleList.do?dispCatNo=900000100090001&fltDispCatNo=&prdSort=01&pageIdx={}&rowsPerPage=24&searchTypeSort=btn_thumb&t_page=%EC%84%B8%EC%9D%BC&t_click=%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B0&t_1st_category_type=&t_product_fliter_type=%EB%B6%84%EB%A5%98%ED%95%84%ED%84%B0_%EC%9D%B8%EA%B8%B0%EC%88%9C&t_view_fliter_type=%EB%B7%B0%EC%88%98%EB%9F%89%ED%95%84%ED%84%B0_24&t_type_fliter_type=%ED%83%80%EC%9E%85%EB%B6%84%EB%A5%98_1'

# Open a CSV file in write mode
with open('OliveYoung_Results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Company', 'Title', 'Original Price', 'Current Price', 'Number of Reviews']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    for page_number in range(1, 50):  
        url = base_url.format(page_number)
        resp = requests.get(url)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            companies = soup.find_all('span', class_='tx_brand')
            titles = soup.find_all('p', class_="tx_name")
            org_prices = soup.find_all('span', class_='tx_org')
            cur_prices = soup.find_all('span', class_='tx_cur')
            reviews = soup.find_all('p', class_='prd_point_area tx_num')

            print(f"Page {page_number} Results:")

            for company, title, org_price, cur_price, review in zip(companies, titles, org_prices, cur_prices, reviews):
                company_text = company.text.strip()
                title_text = title.text.strip()
                org_price_text = org_price.find('span', class_='tx_num').text.strip()
                cur_price_text = cur_price.find('span', class_='tx_num').text.strip()

                # Extracting the number of reviews, handling "999+"
                if review:
                    match_reviews = re.search(r'\((\d+|\d+\+?)\)', review.text)
                    num_reviews = match_reviews.group(1) if match_reviews else 'None'
                else:
                    num_reviews = 'None'

                # Write the data to the CSV file
                writer.writerow({'Company': company_text, 'Title': title_text, 'Original Price': org_price_text,
                                 'Current Price': cur_price_text,
                                 'Number of Reviews': num_reviews})

                print(f"Company: {company_text}")
                print(f"Title: {title_text}")
                print(f"Original Price: {org_price_text}")
                print(f"Current Price: {cur_price_text}")
                print(f"Number of Reviews: {num_reviews}")

                print("----------------------")
        else:
            print(f"Error {resp.status_code} occurred for page {page_number}.")
