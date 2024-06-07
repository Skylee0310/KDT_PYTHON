create database scraping;

use scraping;

drop table if exists pages;

create table pages(
	id BIGINT(7) not null auto_increment,
	title VARCHAR(200),
	content VARCHAR(10000),
	created TIMESTAMP default CURRENT_TIMESTAMP,
	primary KEY(id)
	);
	

insert into pages(title, content)
values("Test page title", "This is some test page content. It can be up to 10,000 characters long.");

select *from pages;

insert into pages(title, content)
values("Second page title", "This is the second test page content");

select * from pages 
where id = 2;

select * from pages 
where title like "%test%";

select id, title, created from pages
where content like "%second%";

select count(*) from pages;