# sqlcalss_db데이터베이스 사용
use sqlclass_db

drop table if exists world;

# 테이블 world 생성
create table world
	(country VARCHAR(30),
	continent varchar(30),
	area int,
	population int,
	capital varchar(30),
	top_level_domain varchar(3),
	primary key (country));
#데이터 확인	
desc world

#데이터 추가
insert into world(country, continent, area, population, capital,top_level_domain)
values
('Afghanistan', 'Asia', 652230, 25500100, 'Kabul', '.af'),
('Algeria', 'Africa', 2381741, 38700000, 'Algiers', '.dz'),
('New Zealand', 'Oceania', 270467, 4538520, 'Wellington', '.nz'),
('Australia', 'Oceania', 7692024, 23545500, 'Canberra', '.au'),
('Brazil', 'South America', 8515767, 202794000, 'Brasilia', '.br'),
('China', 'Asia', 9596961, 1365370000, 'Beijing', '.cn'),
('India', 'Asia', 3166414, 1246160000, 'New Delhi', '.in'),
('Russia', 'Eurasia', 17125242, 146000000, 'Moscow', '.ru'),
('France', 'Europe', 640679, 659060000, 'Paris', '.fr'),   
('Germany', 'Europe', 357114, 807160000, 'Berlin', '.de'),
('Denmark', 'Europe', 43094, 5634437, 'Copenhagen', '.dk'),
('Norway', 'Europe', 323802, 5124383, 'Oslo', '.no'),
('Sweden', 'Europe', 450295, 9675885, 'Stockholm', '.se'),
('South Korea', 'Asia', 100210, 50423955, 'Seoul', '.kr'),
('Canada', 'North America', 9984670, 35427524, 'Ottawa', '.ca'),
('United States', 'North America', 9826675, 318320000, 'Washington, D.C.', '.us'),
('Armenia', 'Eurasia', 29743, 30174000, 'Yerev', '.am');


#테이블 내용 출력
select*from world

# 유럽 국가의 country, capital, top_level_domain 컬럼 출력
select country, capital, top_level_domain from world where continent = 'Europe';

#아시아 국가들의 인구수를 내림차순으로 출력. (country, population 컬럼 출력)
select country, population from world 
where continent = 'Asia' order by population desc;

# 전체 국가의 국가명, 대륙, 면적 컬럼을 출력하는데 면적의 내림차순으로 정렬하여 출력.
select country, continent, area from world
order by area desc;

# 전체 국가의 국가명, 도메인 이름을 출력
select country, top_level_domain from world
order by top_level_domain asc;
