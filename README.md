## UPPRAISAL: Optimize your sales pitch to get the maximum return.

[Nov. 24]: This was the project that I completed as a Data Science Fellow at Insight. I'm currently updating this repo to reflect the fuller and more up-to-date version of it.

Problem
-

eBay sellers have no way of knowing whether their listing titles and descriptions are helping them to earn the highest possible return for their product. This impacts sellers who have few other ways to stand out — for example, sellers of MacBook Pro laptops, which all look very similar and are generally non-customizable.

Solution
-

My solution to this problem is an app that helps eBay sellers get the most for their MacBook Pro laptops. It offers advice for improving their listing titles and descriptions, together with an estimate of how much more they would receive for their laptops if they take the advice.
- Designed Streamlit web interface, deployed on Heroku, that delivers text improvement advice that appears and disappears according to a string-matching system monitoring user text edits
- Estimated price increase with a Lasso regression model of 10K scraped eBay listings, with hand-engineered and LDA-derived features pertaining to title, description, and Macbook specs
- Demonstrated that model surpasses specs-only baseline according to R², RMSE, and MAPE

Demo
-
See [here](https://docs.google.com/presentation/d/1mcprzRBa3owQ9Xrx9ByNCmMEQ23Mzk-FyndLD1KpxIU/edit#slide=id.g9c1e6b6e08_0_214).