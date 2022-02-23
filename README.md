# **FINAL PROJECT**

Project 3  
Presentation Date: March 5, 2022  
Prepared by: Rachel Pierce and Margee Lancaster 

#

## Project Title:
Cryptocurrency, Open Banking, and Banking Sentiment Analysis

![image](./Images/blockchainvstraditional.png)

#

## Project Team Members:
- Rachel Pierce
- Margee Lancaster

#

## Project Objective and Hypothesis  
  
Our objective is to research news articles using the News API to determine the overall sentiment analysis of three main concepts:
1. Cryptocurrency
2. Open banking 
3. Traditiional banking
  
Given cryptocurrency and blockchain technology is creeping into the banking system, we want to determine how the banking industry views these three concepts.  We want to know which concept is most popular, which is least popular, and which is the future of banking.

Our hypothesis is that the banking industry is more risk averse and less supportive of cryptocurrency (more negative sentiment). While some banks are offering crypto services, we believe that banks are more comfortable partnering with fintechs to offer crypto services and other innovative technologies rather than developing and offering them through the bank.  We predict that open banking will have the most favorable sentiment of the three concepts.

We plan to answer the following questions:  
1. Does the public have a positive, negative, or neutral sentiment surrounding crypto in banking?
2. Does the public have a positive, negative, or neutral sentiment surrounding open banking?
3. Does the public have a positive, negative, or neutral sentiment surrounding traditional banking?
4. How do these three concepts compare (sentiment analysis)?
5. How does our sentiment analysis results compare to AWS Comprehend?

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
We will include several background slides to add context surrounding three main concepts - crypto, open banking, and banking.  We will also prepare analysis slides based on our data.
1. Evolution of Banking Slide - moving towards blockchain and crypto.
2. How blockchain technology and partnering with Fintechs is improving banking.
3. Bank Use Cases (cattle tracking blockchain, crypto custody services, JP metaverse, Visa/MC offering crypto conversion, TassatPay/Network, USDF Consortium, CBDCs)
4. Data on how many banks are using blockchain technology.
5. Risks associated with new technologies in banking (BSA/AML, Fair Lending, price risk, operational risks, etc)
6. Benefits of new technologies in banking (faster payments, regulation/public trust, expansion of bank services/customer base, open banking for all)
7. Our Project - Analyze sentiment across three main concepts - Crypto, Open Banking, and Traditional Banking, include Hypothesis
8. What is Crypto?  What is Open Banking? What is Traditional Banking?
9. Sentiment Analysis
10. Ngrams and Frequency Analysis
11. AWS Comprehend
12. Conclusion
13. Data Issues/Improvements

#

## Conclusion:

ADD IF HYPOTHESIS WAS ACCURATE.  

Questions Answered:
1. Does the public have a positive, negative, or neutral sentiment surrounding crypto in banking?
2. Does the public have a positive, negative, or neutral sentiment surrounding open banking?
3. Does the public have a positive, negative, or neutral sentiment surrounding traditional banking?
4. How do these three concepts compare (sentiment analysis)?
5. How does our sentiment analysis results compare to AWS Comprehend?  

*Difficulties/Implications:*  
NewsAPI limited character content, stop words may not include all necessary stop words, open banking and banking articles may overlap.

#


## Additional Notes:

#

## Workpapers in GitHub
Please refer to the following workpapers in GitHub:
- This **ReadMe** file (Includes a summary of the project)
- **Project3_Presentation.html** file (Class Presentation)
- **XX.ipynb** file (Includes all code details)
- **Images** folder (Includes various images included in the project)
#

## References:
- [News API Page](https://newsapi.org/)

#
