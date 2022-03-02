# **FINAL PROJECT**

Project 3  
Presentation Date: March 5, 2022  
Prepared by: Rachel Pierce and Margee Lancaster 

#

## Project Title:
Cryptocurrency, Open Banking, and Banking Sentiment Analysis

![Image](./Images/blockchainvstraditional.png)

#

## Project Team Members:
- Rachel Pierce
- Margee Lancaster

#

## Executive Summary

Fintechs have transformed the way we do banking, transforming payments, lending, and more. Traditional banking is becoming a way of the past, and banks are partnering with Fintech companies to offer innovative products and services to meet consumer demand.  Open banking has become the new way to bank, with third party providers (Fintechs) gaining open access to consumer banking, transaction, and financial data through the use of APIs to provide more innovative products and better customer service. Open banking has also leveraged blockchain technology, and allows customers to connect with the crypto world, such as funding crypto wallets directly from their bank accounts.  
  
While innovative technologies are taking over the banking industry, there is still hesitation to trust new technology.  Our goal for this project is to measure the overall sentiment across three concepts: Cryptocurrency, Open Banking, and Traditional Banking, which will give us insight regarding how the public feels about these three types of banking.  Are consumers still more comfortable with traditional banking?  Or is society embracing technological change and moving towards Open Banking or even crypto?  We shall find out!  

#

## Project Objective and Hypothesis  
  
Our objective is to research news articles using the News API to determine the overall sentiment analysis of three main concepts:
1. Cryptocurrency
2. Open banking 
3. Traditional banking
  
Given cryptocurrency and blockchain technology have entered the banking system, we want to determine how the banking industry views these three concepts.  We want to know which concept is most popular, which is least popular, and which is the future of banking.

Our hypothesis is that the banking industry is more risk averse and less supportive of cryptocurrency (more negative sentiment). While some banks are offering crypto services, we believe that banks are more comfortable partnering with fintechs to offer crypto services and other innovative technologies rather than developing and offering them through the bank.  We predict that open banking will have the most favorable sentiment of the three concepts.

We plan to answer the following questions:  
1. Does the public have a positive, negative, or neutral sentiment surrounding crypto in banking?
2. Does the public have a positive, negative, or neutral sentiment surrounding open banking?
3. Does the public have a positive, negative, or neutral sentiment surrounding traditional banking?
4. How do these three concepts compare (sentiment analysis)?
5. How do our sentiment analysis results compare to AWS Comprehend?

Techniques used to accomplish our objectives include utilizing applicable pandas libraries, such as nltk, and using a new technology (AWS Comprehend/Sagemaker) to compare our sentiment analysis results.

#

## Datasets Used:
We used data obtained from the News API.  
https://newsapi.org/

#

##  Data Phases:
Our process consisted of data exploration,  data preparation, and data cleanup. 
  
- *Data Exploration:* Researched various news APIs.  Selected the NewsAPI and exported crypto, open banking, and banking articles.  
- *Data Preparation:* Sorted through articles for relevant content.  Used Spyder to dig into variables needed.  Exported articles to txt for use in AWS Comprehend. 
- *Data Cleanup:*  Tokenized data and filtered out stop words.

Data Issues: 
- NewsAPI limited in characters when pulling content.
- Banking and Open Banking news articles could overlap.

#

## Presentation 
Our presentation includes the following slides, which cover background information related to crypto, open banking, and traditional banking, project objectives and hypothesis, sentiment analysis results, AWS Comprehend demo, and conclusions.  Please refer to the html presentation in GitHub for the presentation deck.  
  
1. Evolution of Banking
2. The Innovation of Banking (No longer just a brick and mortor bank, moving towards blockchain technology and fintech innovation to provide better banking services to meet consumer demand)
3. Banking Improvements and Challenges of Fintech Partnerships
4. Bank Use Cases (cattle tracking with blockchain, bank crypto custody services, JP in the metaverse, Visa/MC offering crypto conversion, TassatPay/Network, USDF Consortium, CBDCs, Milo crypto mortgages, etc.)
5. Banks currently using blockchain technology
6. Risks associated with new technologies in banking (BSA/AML, Fair Lending, price risk, operational risks, etc.)
7. Benefits of new technologies in banking (faster payments, regulation/public trust, expansion of bank services/customer base, financial inclusion)
8. Project Overview and Hypothesis - Analyze sentiment across three main concepts: Crypto, Open Banking, and Traditional Banking.  Answer 5 Main Questions.
9. Background Slides: What is Crypto?  What is Open Banking? What is Traditional Banking?
10. Techniques Used to Accomplish Objective - Utilizing applicable pandas libraries, such as nltk, and AWS Comprehend/Sagemaker
11. Sentiment Analysis Results
12. Ngrams and Frequency Analysis Results
13. AWS Comprehend Demo
14. Overall Conclusion/Answers to 5 Main Questions/Future of Banking
15. Data Issues/Improvements/Potential Next Steps

#

## Conclusion:

Our hypothesis that Open Banking would achieve the highest sentiment was inaccurate, while our prediction that crypto would achieve the lowest sentiment was accurate.  Based on our sentiment analysis, the most positive sentiment scores were tied to Traditional Banking. However, these results could be skewed based on overlap between Banking/Open Banking news articles.  Crypto had the lowest sentiment across most analysis results.  
  
Questions Answered:
1. Does the public have a positive, negative, or neutral sentiment surrounding crypto in banking?  
Neutral/Slightly Positive
2. Does the public have a positive, negative, or neutral sentiment surrounding open banking?  
Positive
3. Does the public have a positive, negative, or neutral sentiment surrounding traditional banking?  
Positive
4. How do these three concepts compare (sentiment analysis)?  
Based on our analysis, traditional banking has the highest positive scores in most categories.  Crypto and Open Banking were mixed, with some positive, some negative, but crypto was clearly the lowest overall.
5. How does our sentiment analysis results compare to AWS Comprehend?  
AWS Comprehend results were neutral across all three concepts.

![Image](./Images/cryptoplot.png)  
  
![Image](./Images/openbankingplot.png)  
  
![Image](./Images/bankingplot.png)  
  
#

## Difficulties/Implications/Potential Next Steps:  
  
A few difficulties we encountered during this project was that the NewsAPI limited character content in articles obtained; stop words may not include all necessary stop words; and open banking and banking articles may overlap.  
Potential next steps could include changing "Open Banking" to "Fintechs" to determine if results would be clearer, rather than having the potential for overlap with Banking. Also finding a better news API with more content would result in more accurate sentiment analyses.

#

## Workpapers in GitHub
Please refer to the following workpapers in GitHub:
- This **ReadMe** file (Includes a summary of the project)
- **Project3_Presentation.html** file (Class Presentation)
- **Sentiment_Analysis.ipynb** file (Includes all code details)
- **comprehend-banking.ipynb, comprehend-crypto.ipynb, and comprehend-openbanking.ipynb** files (Includes notebooks for use in AWS Comprehend)
- **project3banking.txt, project3crypto.txt, and project3openbanking.txt** files (Used in AWS Comprehend)  
- **project3.py** file (Includes Spyder file for use in data prep)
- **Images** folder (Includes various images included in the project)
- **AWS Instructions for Amazon Comprehend** file (Includes a walk-through of how to use AWS Comprehend, as shown in our demo)
#

## References:
- [News API Page](https://newsapi.org/)
- [Fintech Advisory Article](https://www.fintech-advisory.com/news/2021/5/19/why-more-people-choose-crypto-over-traditional-banking)
- [Investopedia](https://www.investopedia.com/articles/07/banking.asp)
- [US Bank Article](https://www.usbank.com/financialiq/manage-your-household/personal-finance/evolution-of-banking-technology.html
)
- [Forbes Article](https://www.forbes.com/sites/ronshevlin/2022/01/19/bank-fintech-partnerships-are-under-performing-whats-going-wrong/?sh=74c0e2c5559a)
- [Forbes Article](https://www.forbes.com/sites/forbesbusinesscouncil/2021/12/03/banks-and-fintech-a-partnership-with-a-future/?sh=5e52ef0d6aab)
- [Deloitte Article](https://www2.deloitte.com/us/en/pages/center-for-board-effectiveness/articles/information-technology-risks-financial-services.html)
- [Deloitte Article](https://www2.deloitte.com/us/en/pages/center-for-board-effectiveness/articles/information-technology-risks-financial-services.html)
- [Beefchain](https://beefchain.com/about/)
- [FNB Omaha Agriculture of Tomorrow](https://www.fnbo.com/insights/commercial-business/three-new-trends-in-agribusiness/)
- [US Bank launches bitcoin custody service as institutions race to cater to crypto demand](https://www.cnbc.com/2021/10/05/bitcoin-custody-us-bank-launches-service-as-institutions-race-to-cater-to-crypto-demand.html)
- [CBDC Tracker](https://www.atlanticcouncil.org/cbdctracker/)
- [USDF Consortium](https://www.usdfconsortium.com/)
- [Tassat Group executes real-time digital payment between two banks](https://ibsintelligence.com/ibsi-news/tassat-group-executes-real-time-digital-payment-between-two-banks/)
- [Visa says crypto-linked card usage hit $2.5 billion in its first quarter](https://www.cnbc.com/2022/01/28/visa-says-crypto-linked-card-usage-hit-2point5-billion-in-its-first-quarter.html)
- [JP Morgan is first leading back to launch in the metaverse](https://fintechmagazine.com/banking/jp-morgan-becomes-the-first-bank-to-launch-in-the-metaverse)
- [Top Crypto-Friendly Banks](https://fortunly.com/banking/best-crypto-friendly-banks/#gref)
- [Milo Launches Crypto Mortgage Product](https://www.housingwire.com/articles/milo-launches-a-crypto-mortgage-product/)
-[Russia May Use Cryptocurrency to Evade Sanctions](https://www.investopedia.com/russia-may-use-cryptocurrency-to-evade-sanctions-5220265)
- [World's biggest crypto exchange Binance says it will not block all Russian accounts despite Ukraine request](https://www.cnbc.com/2022/02/28/binance-will-not-block-russian-accounts-after-ukraine-request.html)
#
