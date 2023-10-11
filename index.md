# Selected Projects in Data Science and Econometrics

---

## [Web Scraper for Subsidized Housing Transaction Data](https://github.com/johnthwong/housing-authority-scraper)
The Housing Authority's data on subsidized housing transactions is notoriously difficult to access as the data must be requested by month, each with a separate web form. So I developed a scraper that automatically submits forms and gathers transaction count in each month into one spreadsheet. 

Built with Python and Selenium. Check it out here: [https://github.com/johnthwong/housing-authority-scraper](https://github.com/johnthwong/housing-authority-scraper)
<br>
<br>
<img src="images/thumbnail_ha_scraper.png"/>
<br>
<br>

---

## [Mandate Banks to Use the Discount Window](https://johnthwong.github.io/pdf/paper_dw.pdf)
I wrote in a policy memo in December 2022 that the HKMA (Hong Kong's central bank) should regularly mandate random banks to use the discount window (DW). This would prevent fluctuations in interbank borrowing costs, which hurts both mortgage borrowers and banks. [Read more](https://johnthwong.github.io/pdf/paper_dw.pdf)

**When HIBOR (red) Breaches the Base Rate (blue)**
<img src="images/thumbnail_dw_1.png"/>
<br>
<br>

---

## [Do Societies With Greater Populations Innovate More?](https://johnthwong.github.io/pdf/Wong_Man_Li_Population_and_Technological_Growth.pdf)
In this paper, we estimate how variations in population sizes across US states causally impacted these states’ capacity to produce patents. To rule out the endogeneity of fertility decisions, we estimate the difference-in-difference in births before and after the Roe ruling, and then use estimated births as an instrumental variable to predict patents per capita. [Read more](https://johnthwong.github.io/pdf/Wong_Man_Li_Population_and_Technological_Growth.pdf)
<br>
<br>
**Estimating Patents Granted per Capita on Births Using Roe as an Instrumental Variable**
<img src="images/thumbnail_roe_2.png"/>
<br>
<br>

---

## [Visualization of the Hong Kong's Forex Reserves](https://github.com/johnthwong/hkma)
After a drop in the balances of accounts held at the central bank by commercial banks (aka "Aggregate Balance") in the summer of 2022, there was [panic](https://www.bloomberg.com/news/articles/2022-07-26/hong-kong-liquidity-shrinks-50-since-may-amid-currency-defense) that Hong Kong's currency peg with the USD would break. In response, I wrote an internal report on why "Aggregate Balance" is insignificant and not worth freaking out about.
<br>
<br>
This project parses JSON data from the Hong Kong Monetary Authority. Data manipulation and visualization are done with R's dplyr and ggplot libraries.
<br>
<br>
Check out a similar coding file that generated the visualization below here: [https://github.com/johnthwong/hkma](https://github.com/johnthwong/hkma)
<br>
<br>
<img src="images/thumbnail_viz_reserves.png"/>
<br>
<br>

---

## [Give US Public Housing Residents the Right to Buy Their Flat](https://johnthwong.github.io/page_tpo)
I recently wrote a policy memo for the Federation of American Scientists' call for federal policy ideas for increasing housing supply. By selling public housing units, we can unlock currently non-transferrable land value, increase homeownership, create new wealth that accrues to the poor, improve state and local public finances, free up units under the Faircloth Limit, and most of all, increase housing supply. [Read more](https://johnthwong.github.io/page_tpo)
<br>
<br>
<img src="images/thumbnail_tpo_1.jpg"/>
Photo by <a href="https://unsplash.com/@sigmund?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sigmund</a> on <a href="https://unsplash.com/photos/CwTfKH5edSk?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

---

## [Equal Liberal Rights Drive Growth](https://johnthwong.github.io/page_ajr)
I estimated the effect of liberal rights on economic growth using an instrumental variable model, drawing inspiration from Acemoglu et al.'s classic study on the institution hypothesis. I use an updated dataset on growth and Freedom House's country-level indices on both the quality of democracy and civil liberties as treatment variables. 
<br>
<br>
Turns out, better political and civil rights on their own can drive even more growth than just better property rights alone. [Read more](https://johnthwong.github.io/page_ajr)
<br>
<br>
<img src="images/thumbnail_ajr_table_2_small.png?raw=true"/>
<br>
<br>

---

## [Predicting Conflict in Developing Regions Using Machine Learning Decision Trees](https://johnthwong.github.io/pdf/Li_Wong_Pye_Ling_Conflict_Prediction.pdf)
As part of a term assignment, we predicted the likelihood of armed conflicts within 50-kilometer squares by fitting a large panel of predictors to both a decision tree model specifically designed for panel data (RE-EM tree) and an artificial neural network. [Read more](https://johnthwong.github.io/pdf/Li_Wong_Pye_Ling_Conflict_Prediction.pdf)
<br>
<br>
This project used R's dplyr and data.table libraries and also Google's Python package—Keras—for interfacing with Tensorflow.
<br>
<br>
**RE-EM Tree for Predicting Conflict**
<img src="images/thumbnail_conflict_pred.png"/>
<br>
<br>

---
