# Surfs_up
Using jupyter notebook, SQLIte and VS Code to conduct weather analysis for surfing shop 

## Overview 
  W. Avy likes your analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.
  
## Analysis 

  1. Deliverable 1: Determine the Summary Statistics for June
     *  Write a query that filters the Measurement table to retrieve the temperatures for the month of June. 
     june_query.png![june_query](https://user-images.githubusercontent.com/82353749/122121289-6fbadc80-cdf9-11eb-87f6-545f03ee0227.png)
     *  Convert the June temperatures to a list 
      june_list.png![ june_list](https://user-images.githubusercontent.com/82353749/122121415-9aa53080-cdf9-11eb-95e2-6600d7234627.png)
     *  Create a DataFrame from the list of temperatures for the month of June
     June_df.png![June_df](https://user-images.githubusercontent.com/82353749/122121529-c1fbfd80-cdf9-11eb-8c81-963a4c8fd332.png)
     *  Calculate and print out the summary statistics for the June temperature DataFrame
     june_stats.png![june_stats](https://user-images.githubusercontent.com/82353749/122121695-ee177e80-cdf9-11eb-9639-3e7509e8c506.png)

  2. Deliverable 2: Determine the Summary Statistics for December
     * Write a query that filters the Measurement table to retrieve the temperatures for the month of December.
     dec_results.png![dec_results](https://user-images.githubusercontent.com/82353749/122121894-2323d100-cdfa-11eb-9b93-d935e6848620.png)
     * Convert the December temperatures to a list.
     dec_list.png![dec_list](https://user-images.githubusercontent.com/82353749/122122533-ec9a8600-cdfa-11eb-9c76-e143729639a3.png)
     *  Create a DataFrame from the list of temperatures for the month of December. 
     dec_df.png![dec_df](https://user-images.githubusercontent.com/82353749/122122743-2ff4f480-cdfb-11eb-89e8-e1865746ba3d.png)
     *  Calculate and print out the summary statistics for the Decemeber temperature DataFrame.
     dec_stats.png![dec_stats](https://user-images.githubusercontent.com/82353749/122122867-5d41a280-cdfb-11eb-94b1-52f0f9393831.png)
     
## Summary 
  There is less than 3 degrees difference between the average tempature in June (74.94) and December (71.04), and there is not much difference between highest temperature in June and December, so it would be consistently warm to have surf and ice cream the whole year around. 
  
