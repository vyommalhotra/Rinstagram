-- 8
INSERT INTO Friend 
VALUES ('503442187183', '521026065681');

SELECT * FROM Friend 
WHERE id = '503442187183';
 
-- 12. query to return groups for a user
SELECT groupname.gid, groupname.groupname 
FROM persongroup 
join groupname on persongroup.gid = groupname.gid
WHERE id = 521026065681;

-- 13

INSERT INTO PersonGroup VALUES ('','');

-- 14
SELECT PostLike.response, Person.username
FROM Post INNER JOIN PostLike ON Post.pid = PostLike.pid
LEFT JOIN GroupName ON GroupName.gid = Post.gid 
LEFT JOIN Person ON Person.id = PostLike.id
WHERE Person.username IS NOT NULL AND Post.pid = '1172919682829981000197413325778';

-- 15
insert into groupname
values (NULL, 'test')


