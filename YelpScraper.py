from selenium import webdriver
import csv

def scrape_yelp():
    # Create new csv doc
    with open("bonchondata.csv", "w") as f:
        f.write("Data, Review,\n")

    # open webpage
    driver_path = "~/chromedriver"
    driver = webdriver.Chrome(driver_path)

    # Create loop to scrape all reviews
    for pagenumber in range(0,540,20):
        driver.get("https://www.yelp.com/biz/bonchon-silver-creek-san-jose-2?start=" + str(pagenumber))
        reviewdate = driver.find_elements_by_xpath('//span[@class="rating-qualifier"]')
        review = driver.find_elements_by_xpath('//p[@lang="en"]')
        length_of_items = len(review)
        # Open the Csv created above, append the data we scraped into text format
        with open('bonchondata.csv', 'a') as f:
            for items in range(length_of_items):
                cleandate = reviewdate[items].text 
                cleantext = review[items].text
                cleandate.replace(',','')
                var = cleantext.replace('\n','').replace(',','').replace('\r','')
                print(var)
                # write to the csv and close.
                f.write(cleandate + ',' + var + "\n")
    driver.close()

def main():
    scrape_yelp()

if __name__ == '__main__':
    main()