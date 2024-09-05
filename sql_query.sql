/* 1. Выберите уникальные регионы сбора грибов.*/
SELECT distinct r."name" as "УНИКАЛЬНЫЕ РЕГИОНЫ"
FROM mushrooms m
INNER JOIN regions r 
ON m.primary_region_id = r.region_id 

/* 2. Выведите название, сезон сбора и съедобность грибов, которые относятся к категории «Трубчатые».*/
SELECT m."name" as "НАЗВАНИЕ", m.season as "СЕЗОН", m.edible as "СЪЕДОБНОСТЬ"
FROM mushrooms m
INNER JOIN categories ca 
ON m.category_id = ca.category_id  
where ca."name" = 'Трубчатые грибы'
group by "НАЗВАНИЕ", "СЕЗОН", "СЪЕДОБНОСТЬ"

/* 3. Посчитайте количество грибов для каждой категории. Выведите название категории и количество в порядке убывания.*/
SELECT ca."name" as "НАЗВАНИЕ", count(*) as "КОЛЧИЧЕСТВО"
FROM mushrooms m
INNER JOIN categories ca 
ON m.category_id = ca.category_id  
group by "НАЗВАНИЕ"
order by "КОЛЧИЧЕСТВО" desc 

/* 4. Выведите название и описание съедобных грибов, которые лучше всего собирать в пяти самых больших по размеру (size) регионах.*/
SELECT m."name" as "НАЗВАНИЕ", m.description as "ОПИСАНИЕ"
FROM mushrooms m
INNER JOIN regions re
ON m.primary_region_id  = re.region_id 
where m.edible = true and re."size" in (select reg."size" from regions reg order by reg."size" desc limit 5)
group by "НАЗВАНИЕ", "ОПИСАНИЕ"

/* 5. Выведите названия всех грибов, которые растут весной, относятся к категории "Пластинчатые" и которые лучше всего
собирать в местах размером до 6000 условных единиц (size).*/
SELECT m."name" AS "НАЗВАНИЕ"
FROM mushrooms m 
INNER JOIN regions re
ON m.primary_region_id  = re.region_id 
INNER JOIN categories ca
ON m.category_id = ca.category_id 
WHERE m.season = 'Весна' AND ca."name" = 'Пластинчатые грибы' AND re."size" < 6000
GROUP BY "НАЗВАНИЕ"