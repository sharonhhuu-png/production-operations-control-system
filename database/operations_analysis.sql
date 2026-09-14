-- QUERY 1: Which suppliers have the most high-risk orders?
-- Business Value: Identifies vendor performance bottlenecks.
SELECT 
    Supplier,
    COUNT(Order_ID) AS Total_Orders,
    SUM(CASE WHEN Risk_Level IN ('CRITICAL', 'HIGH') THEN 1 ELSE 0 END) AS High_Risk_Orders,
    SUM(Quantity) AS Units_At_Risk
FROM production_orders
GROUP BY Supplier
ORDER BY High_Risk_Orders DESC;


-- QUERY 2: What is causing our production delays?
-- Business Value: Highlights systemic operational failures.
SELECT 
    Risk_Reason,
    COUNT(Order_ID) AS Frequency,
    AVG(Risk_Score) AS Avg_Risk_Severity
FROM production_orders
WHERE Risk_Level != 'LOW'
GROUP BY Risk_Reason
ORDER BY Frequency DESC;


-- QUERY 3: The Action Queue (Who needs to do what today?)
-- Business Value: Replaces manual chasing with automated prioritization.
SELECT 
    Order_ID,
    Supplier,
    Risk_Level,
    Risk_Reason,
    Owner AS Action_Owner,
    Ex_Factory_Date
FROM production_orders
WHERE Risk_Level IN ('CRITICAL', 'HIGH')
ORDER BY Risk_Score DESC;
