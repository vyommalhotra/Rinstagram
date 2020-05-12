LOAD DATA INFILE "reduced_comments.csv"
INTO TABLE postcomment
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "reduced_post.csv"
IGNORE INTO TABLE post
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "reduced_like.csv"
INTO TABLE postlike
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "reduced_member.csv"
IGNORE INTO TABLE person
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "reduced_login.csv"
IGNORE INTO TABLE login
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

LOAD DATA INFILE "reduced_friend.csv"
IGNORE INTO TABLE friend
COLUMNS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

INSERT INTO PersonGroup
SELECT gid, id FROM Person

BEGIN;
INSERT INTO groupname VALUES ('25160801076', 'Unoffical Cheltenham Township');
INSERT INTO groupname VALUES ('117291968282998', 'Elkin Park Happenings!');
INSERT INTO groupname VALUES ('1443890352589739', 'Free Speech Zone');
INSERT INTO groupname VALUES ('1239798932720607', 'Cheltenham Lateral Solutions');
INSERT INTO groupname VALUES ('335787510131917', 'Cheltenham Township Residents');
INSERT INTO groupname VALUES ('1', 'New Members');
COMMIT;

BEGIN;
INSERT INTO person values ('1', '1', 'vyom');
COMMIT;

BEGIN;
INSERT INTO persongroup values ('1', '1');
commit;

BEGIN;
INSERT INTO login values ('vyom', 'password');
COMMIT;

BEGIN;
INSERT INTO post VALUES ('1', '9000000000000000000000000000000000', '1', NOW(), 'Welcome New Members. This social media platform was made by Vyom Malhotra and Sarthak Bhatnager as a proof of concept', '9000');
COMMIT;