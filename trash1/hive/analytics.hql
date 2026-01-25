CREATE TABLE daily_page_visits AS
SELECT
  page,
  COUNT(*) AS visits
FROM user_activity
GROUP BY page;
