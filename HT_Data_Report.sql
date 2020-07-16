--Organize cases per STATE_ABBR
SELECT COUNT(STATE_ABBR), STATE_ABBR FROM HT_2013_2018
GROUP BY 2
ORDER BY 1 DESC;

--Looks like Texas has the highest amount of cases, maybe there are regions with high case density
SELECT COUNT(*) AS CASES_PER_COUNTY, COUNTY_NAME, REGION_NAME FROM HT_2013_2018 WHERE STATE_ABBR = 'TX'
GROUP BY 2
ORDER BY 1 DESC;

--Finding the percent of cleared reports in Texas
SELECT SUM(ACTUAL_COUNT) AS SUM_REPORTED, 
	SUM(UNFOUNDED_COUNT) AS SUM_FALSE_REPORTS, 
	SUM(CLEARED_COUNT) AS SUM_CLEARED, 
	(SUM(CLEARED_COUNT)*100)/SUM(ACTUAL_COUNT) AS PERCENT_SOLVED,
	(SUM(UNFOUNDED_COUNT)*100)/SUM(ACTUAL_COUNT) AS PERCENT_FALSE
	FROM HT_2013_2018 WHERE STATE_ABBR = 'TX';
	
--Check the same but for all reported cases
SELECT SUM(ACTUAL_COUNT) AS SUM_REPORTED, 
	SUM(UNFOUNDED_COUNT) AS SUM_FALSE_REPORTS, 
	SUM(CLEARED_COUNT) AS SUM_CLEARED, 
	(SUM(CLEARED_COUNT)*100)/SUM(ACTUAL_COUNT) AS PERCENT_SOLVED,
	(SUM(UNFOUNDED_COUNT)*100)/SUM(ACTUAL_COUNT) AS PERCENT_FALSE
	FROM HT_2013_2018;