# Amazon Vine Analysis

## Overview
The purpose of this analysis was to understand if paying influencers actually resulted in better reviews in the footwear industry.

## Resources
The dataset used for this analysis consisted of over 4 millions rows of data and was obtained from [Amazon Shoe Reviews]
(https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Shoes_v1_00.tsv.gz).
PySpark was used to evaluate and clean the dataset to provide the appropriate subset of data for the analysis.

## Results
The results of this analysis started with determining the true influencers in reviews. This was done by extracting the data for those reviewers with equal to or more than 20 reviews (these are our influencers). The dataframe and total number are shown below:

![Influencers](https://github.com/Bscheinin/Amazon_Vine_Analysis/blob/main/Influncer%20dataframe.PNG)

The next part of the analysis looks at the total number of influencer reviews, the total number of 5-Star reviews and then a breakdown of the number and percentage of 5-star reviews by influencers paid by Vine and unpaid influencers.

![Data Summary](https://github.com/Bscheinin/Amazon_Vine_Analysis/blob/main/Data%20Summary.PNG) 

#Summary
For this dataset from the footwear industry, there is very little influence on rating trends by the paid Vine influencers. In fact, the number of 5-Star reviews by paid Vine influencers is less than 1% of all 5-star reviews. It is apparent from this analysis that paid Vine influencers have very little sway over general population ratings in this industry. Further analysis into the amount of money invested by Vine to influencers in this industry may reveal how ineffective paying influencers in this industry appears to be.  