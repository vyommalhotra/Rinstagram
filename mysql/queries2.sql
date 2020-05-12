-- 1
select pw from login
where username = 'AaronBass15164';

-- 4
select person.username
from friend left join person on friend.friendID = person.ID
where friend.ID = '544889637987';

-- 5
select person.username, postcomment.msg, postcomment.commentTimeStamp from postcomment
join person on postcomment.id = person.id
where pid = '1172919682829981218917638120420';

-- 2
select post.pid, person.username, groupname.groupname, msg, post.postTimeStamp, post.likes from post
left join friend on post.id = friend.friendID
left join groupname on post.gid = groupname.gid
left join person on post.id = person.id
where friend.id = '660791208540' and person.username IS NOT NULL;

-- 3
select post.pid, person.username, groupname.groupname, msg, post.postTimeStamp, post.likes from post
left join persongroup on post.gid = persongroup.gid
left join person on post.id = person.id
left join groupname on post.gid = groupname.gid
where persongroup.id = '660791208540' and person.username IS NOT NULL;

-- 11
delete from friend
where friend.id = '660791208540' and friend.friendID = '1460241457335169';

-- 10

-- increment like
update post
set likes = likes + 1
where pid = '1172919682829981218917638120420';

-- insert reaction
insert into postlike
values ('117291968282998', '1172919682829981218917638120420', 'TEST', '660791208540');

-- 7
insert into postcomment
values ('117291968282998', '1172919682829981218917638120420', NOW(), '660791208540' , 'test message from the testiest tester around');

-- 9

-- login table
insert into login
values ('vyom', 'password');

-- person table
insert into person
values ('117291968282998', NULL , 'vyom');

-- 6

-- get the highest pid
select pid from post order by pid desc limit 1;

-- insert post with incremented pid
insert into post
values ('117291968282998',  '335787510131917590585471318787' , '10216646959432839', NOW(), 'welcome to rinstagram, from its creator.', 0);

-- rough
select likes from postlike
where pid = '1172919682829981218917638120420';

select * from postlike
where pid = '1172919682829981218917638120420' AND gid = '117291968282998';

select * from postcomment
where pid = '1172919682829981218917638120420' AND gid = '117291968282998';

select * from login where username='vyom';
select * from person where username='vyom';
select * from person order by id desc;
select * from post order by CAST(pid as unsigned) desc;
select count(id) as cnt from person where cnt > 1;

select count(username) as cnt from login
group by username having cnt > 1;

select count(pid) as cnt from post
group by gid;

select id from person
order by id desc limit 10;

select * from post where pid = '1172919682829981218917638120420';

select * from postlike where pid = 1172919682829981218917638120420;

select * from groupname
order by gid desc;

select id from person where id = '1' limit 1;

select * from post
where pid = '9000000000000000000000000000000002';

select * from person where username = 'sarthak';

select * from post where gid = '1443890352589740'